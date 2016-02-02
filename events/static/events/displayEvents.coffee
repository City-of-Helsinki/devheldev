window.displayEvents = (eventData, grid = false) ->
  $list = $(".list-banner--events ul, .project-index")
  if Object.keys(eventData).length == 0
    $list.append $("<li class='event-list__item'>Our next events will appear here the instant they are available, so stay tuned.</li>")
  for event in eventData
    if event.message?
      message=event.message
    else
      message=""
    if event.details.description?
      description=event.details.description
    else
      description=""
    if grid
      $li = $("<div class='layout-project-index-item' />")
      template = """
        <div class='project-index-item'>
          <div class='project-index-item__content'>
            <a href="#{event.link}">
            <div class="project-index-image" style="background-image: url(#{event.details.cover.source})">#{event.details.name}</div>
            <h2>#{event.details.name}</h2>
            <time datetime="#{event.details.start_time}"></time> @ #{event.details.place.name}</a>
            <div class="project-description">#{description}</div>
          </div>
        </div>
      """
    else
      $li = $("<li class='event-list__item' />")
      template = """
        <span class="event-list__date"><time datetime="#{event.details.start_time}"></time></span>
        <span class="event-list__header">#{event.details.name}</span>
        <span class="event-list__description">#{message}</span>
        <span class="event-list__link"><a href="#{event.link}">Read more >></a></span>
      """
    $li.append $($.trim template)
    $list.append $li
  # format dates
  $.timeago.settings.relativeTime = true
  $("time").timeago()