

import requests

def tmpl_hri_item_list(items):
    return "\n".join(
        [
            f"""
<li class='dataset-list__item'>
    <a href="{url}">
        <span class="dataset-list__header">{header}</span>
    </a>
</li>
    """
            for header, url in items
        ]
    )

def get_hri_items(limit=5):
    try:
        response = requests.get(
            url="https://hri.fi/data/api/action/current_package_list_with_resources",
            params={
                "limit": limit,
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    data = response.json()
    if data.get("success"):
        return data.get("result")

def do_hri_items():
    data = get_hri_items()

    items = [(d["title_translated"]["en"] or d["title_translated"]["fi"] , d["name"]) for d in data]

    resp = tmpl_hri_item_list(items)

    return resp
