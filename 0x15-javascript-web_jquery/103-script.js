const url = 'https://fourtonfish.com/hellosalut/?lang=';
function docReady (fn) {
  // see if DOM is already available
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    // call on next available tick
    setTimeout(fn, 1);
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

docReady(function () {
  $('#language_code').keydown(function (e) {
    var key = e.charCode ? e.charCode : e.keyCode ? e.keyCode : 0;
    if (key === 13) {
      e.preventDefault();
      const word = $('#language_code').val();
      const link = url.concat(word);
      $.getJSON(link, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
  // DOM is loaded and ready for manipulation here
  $('#btn_translate').click(function () {
    const word = $('#language_code').val();
    const link = url.concat(word);
    $.getJSON(link, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
