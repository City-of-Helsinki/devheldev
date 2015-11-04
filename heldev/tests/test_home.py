import pytest


@pytest.mark.django_db
def test_home_page(client, index_pages):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Helsinki Region Infoshare' in str(response.content)
