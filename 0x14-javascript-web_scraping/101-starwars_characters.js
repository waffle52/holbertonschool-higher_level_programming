#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const list = JSON.parse(body).characters;
    print(list, 0);
  }
});

function print (list, idx) {
  if (idx >= list.length) {
    return;
  }
  request.get(list[idx], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
    }
    return print(list, idx + 1);
  });
}
