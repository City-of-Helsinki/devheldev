

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


def fetch_github_events(organisation="City-of-Helsinki", amount=40):
    
    response = requests.get(f"https://api.github.com/orgs/{organisation}/events?per_page={amount}")
    
    if response.status_code == 200:
    
        events = response.json()
        for index, event in enumerate(events):
            event['repo']['url'] = event['repo']['url'].replace('https://api.github.com/repos/', 'https://github.com/')
    
    return events[:amount]


def github_event_tmpl(event, event_url, event_description):
    
    return f"""<li class='commit-list__item' />
    <div class="commit-list__avatar"><img src="{event['actor']['avatar_url']}&s=128" alt="{event['actor']['login']}"></div>
    <a href="{event_url}">
    <div class="commit-list__date"><time datetime="{event['created_at']}"></time></div>
    <div class="commit-list__description">
    <span class="commit-list__actor">{event['actor']['login']}</span> {event_description} <span class="commit-list__repo">{event['repo']['name']}</span>
    </div>
    </a>
</div></li>
"""


def do_github_events(events):

    out = []
    
    for event in events:
    
        if event['type'] is "PushEvent":
            event_url = event['repo']['url']
            branch = event['payload']['ref'].replace("refs/heads/", "")
            event_description = f" pushed to {branch} at "
        elif event['type'] is "IssueCommentEvent":
            event_url = event['payload']['issue']['html_url']
            event_description = f" {event['payload']['action']} comment on issue #{event['payload']['issue']['number']} at "
        elif event['type'] is "IssuesEvent":
            event_url = event['payload']['issue']['html_url']
            event_description = f" {event['payload']['action']} issue #{event['payload']['issue']['number']} at "
        elif event['type'] is "PullRequestEvent":
            event_url = event['payload']['pull_request']['html_url']
            event_description = f" {event['payload']['action']} pull request #{event['payload']['pull_request']['number']} at "
        elif event['type'] is "MemberEvent":
            event_url = event['payload']['member']['html_url']
            event_description = f" {event['payload']['action']} {event['payload']['member']['login']} to "
        elif event['type'] is "ForkEvent":
            event_url = event['payload']['forkee']['html_url']
            event_description = f" created fork {event['payload']['forkee']['full_name']} from "
        elif event['type'] is "WatchEvent":
            event_url = event['repo']['url']
            event_description = f" {event['payload']['action']} watching "
        elif event['type'] is "PullRequestReviewCommentEvent":
            event_url = event['payload']['comment']['html_url']
            event_description = f" {event['payload']['action']} comment on pull request #{event['payload']['pull_request']['number']} at "
        elif event['type'] is "CreateEvent":
            event_url = event['repo']['url']
            event_description = f" created {event['payload']['ref_type']} {event['payload']['ref']} at "
        elif event['type'] is "DeleteEvent":
            event_url = event['repo']['url']
            event_description = f" deleted {event['payload']['ref_type']} {event['payload']['ref']} at "
        else:
            event_url = event['repo']['url']
            event_description = f" - {event['type']} - "

        out.append(github_event_tmpl(event, event_url, event_description))

    return ''.join(out)
