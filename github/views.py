from django.shortcuts import render
from django.http import HttpResponse
from github.models import GithubOrgIndexPage

# Create your views here.


def github_data(request):
    amount = request.GET.get('amount', '40')
    data = GithubOrgIndexPage.objects.get().events(int(amount))
    return HttpResponse(data)
