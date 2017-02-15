$(function () {
  $('#js-toggle').sidr({
    name: 'sidr-main',
    source: '#js-navigation',
    side: 'right',
    onOpen: function() {$('#js-toggle').toggleClass('is-open')},
    onClose: function() {$('#js-toggle').toggleClass('is-open')}
  });

  enquire.register("screen and (min-width:640px)", {
    match : function() {
      $.sidr('close', 'sidr-main');
    }
  });
});