$(function () {
  $('#toggle').sidr({
    name: 'sidr-main',
    source: '#sidr',
    onOpen: function() {$('.bar').toggleClass('animate')},
    onClose: function() {$('.bar').toggleClass('animate')}
  });
  
  enquire.register("screen and (min-width:640px)", {
    match : function() {
      $.sidr('close', 'sidr-main');
    }
  });
});