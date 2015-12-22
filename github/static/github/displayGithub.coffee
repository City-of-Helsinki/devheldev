window.displayGithub = (githubData) ->
  $list = $(".list-banner--commit-watch ul, .commit-list ul")
  for event in githubData
    switch event.type
      when "PushEvent"
        eventUrl = event.repo.url
        branch = event.payload.ref.replace "refs/heads/", ""
        eventDescription = " pushed to #{branch} at "
      when "IssueCommentEvent"
        eventUrl = event.payload.issue.html_url
        eventDescription = " #{event.payload.action} comment on issue ##{event.payload.issue.number} at "
      when "IssuesEvent"
        eventUrl = event.payload.issue.html_url
        eventDescription = " #{event.payload.action} issue ##{event.payload.issue.number} at "
      when "PullRequestEvent"
        eventUrl = event.payload.pull_request.html_url
        eventDescription = " #{event.payload.action} pull request ##{event.payload.pull_request.number} at "
      when "MemberEvent"
        eventUrl = event.payload.member.html_url
        eventDescription = " #{event.payload.action} #{event.payload.member.login} to "
      when "ForkEvent"
        eventUrl = event.payload.forkee.html_url
        eventDescription = " created fork #{event.payload.forkee.full_name} from "
      when "WatchEvent"
        eventUrl = event.repo.url
        eventDescription = " #{event.payload.action} watching "
      when "PullRequestReviewCommentEvent"
        eventUrl = event.payload.comment.html_url
        eventDescription = " #{event.payload.action} comment on pull request ##{event.payload.pull_request.number} at "
      when "CreateEvent"
        eventUrl = event.repo.url
        eventDescription = " created #{event.payload.ref_type} #{event.payload.ref} at "
      when "DeleteEvent"
        eventUrl = event.repo.url
        eventDescription = " deleted #{event.payload.ref_type} #{event.payload.ref} at "
      else
        eventUrl = event.repo.url
        eventDescription = " - #{event.type} - "
    $li = $("<li class='commit-list__item' />")
    template = """
        <div class="commit-list__avatar"><img src="#{event.actor.avatar_url}&s=128" alt="#{event.actor.login}"></div>
        <a href="#{eventUrl}">
          <div class="commit-list__date"><time datetime="#{event.created_at}"></time></div>
          <div class="commit-list__description">
            <span class="commit-list__actor">#{event.actor.login}</span> #{eventDescription} <span class="commit-list__repo">#{event.repo.name}</span>
          </div>
        </a>
    """
    $li.append $($.trim template)
    $list.append $li
  # format dates
  $("time").timeago()