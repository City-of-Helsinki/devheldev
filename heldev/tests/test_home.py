import pytest


@pytest.mark.django_db
def test_home_page_without_subpages(client, home_page):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Helsinki Region Infoshare' in str(response.content)
    # check commit watch
    assert 'City-of-Helsinki/' not in str(response.content)
    # check event watch
    assert 'Full list of events' not in str(response.content)
    # check project list
    assert 'Full list of ongoing projects' not in str(response.content)

@pytest.mark.django_db
def test_home_page_with_subpages(client, index_pages):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Helsinki Region Infoshare' in str(response.content)
    # check commit watch
    assert 'Full list of Github events' in str(response.content)
    # check event watch
    assert 'Full list of events' in str(response.content)
    # check project list
    assert 'Full list of ongoing projects' in str(response.content)
