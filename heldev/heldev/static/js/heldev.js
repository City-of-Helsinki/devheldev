$( document ).ready(function() {

  $('#menu-toggle').click(function (e) {
    $('body').toggleClass('active');
    e.preventDefault();
  });
  
});