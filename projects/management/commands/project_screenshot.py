import tempfile
import time
from django.core.files.images import ImageFile
from PIL import Image as PILImage
from splinter.browser import Browser
from django.core.management.base import BaseCommand, CommandError
from wagtail.wagtailimages.models import Image

from projects.models import ProjectPage


class Command(BaseCommand):
    help = 'Take project screenshots'

    def handle(self, *args, **options):
        browser = Browser('phantomjs')
        browser.driver.set_window_size(1600, 900)

        for project in ProjectPage.objects.all():
            links = project.links.filter(public=True, type='main')
            if not links:
                continue
            # Use only the first link for now
            link = links[0]
            print("Visiting %s (%s)" % (link.url, link))
            browser.visit(link.url)
            assert browser.status_code.is_success()
            time.sleep(5)

            with tempfile.NamedTemporaryFile(suffix='.png', prefix='project') as tmpf:
                browser.driver.save_screenshot(tmpf.name)

                pil_image = PILImage.open(tmpf)
                pil_image = pil_image.crop((0, 0, 1600, 900))
                tmpf.seek(0)
                tmpf.truncate(0)
                pil_image.save(tmpf, format='PNG')

                title = '%s screenshot' % project.title
                try:
                    image = Image.objects.get(title=title)
                except Image.DoesNotExist:
                    image = Image(title=title)
                image.file = ImageFile(tmpf)
                image.save()

            project.image = image
            project.save(update_fields=['image'])
        browser.quit()
