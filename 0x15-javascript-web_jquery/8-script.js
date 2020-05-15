$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let idx = 0; idx < data.count; idx++) {
    $('UL#list_movies').prepend($('<li>%s</li>').text(data.results[idx].title));
  }
});
