#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const link = url.concat(process.argv[2]);
const peopleUrl = 'https://swapi-api.hbtn.io/api/people/';
let tmp;
let jsonObject;

request.get(link, 'utf8', function (err, response, body) {
  if (err) throw err;
  jsonObject = JSON.parse(body);
  const characters = jsonObject.characters;
  for (let x = 0; x < characters.length; x++) {
    const current = characters[x].replace(/[^0-9]/g, '');
    tmp = peopleUrl.concat(current);
    request.get(tmp, 'utf8', function (err, response, body) {
      if (err) throw err;
      jsonObject = JSON.parse(body);
      console.log(jsonObject.name);
    });
  }
});
