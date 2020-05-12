#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
let url = 'https://swapi-api.hbtn.io/api/films/';
url = url.concat(id);
let jsonObject;
request(url, function (err, response, body) {
  if (err) throw err;
  jsonObject = JSON.parse(body);
  console.log(jsonObject.title);
});
