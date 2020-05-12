#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let jsonObject;
let length = 0;
let secLength = 0;
let total = 0;
const checkUrl = 'https://swapi-api.hbtn.io/api/people/18/';
request.get(url, 'utf8', function (err, response, body) {
  if (err) throw err;
  jsonObject = JSON.parse(body);
  length = jsonObject.count;
  for (let x = 0; x < length; x++) {
    secLength = jsonObject.results[x].characters;
    for (let y = 0; y < secLength.length; y++) {
      if (secLength[y] === checkUrl) {
        total = total + 1;
      }
    }
  }
  console.log(total);
});
