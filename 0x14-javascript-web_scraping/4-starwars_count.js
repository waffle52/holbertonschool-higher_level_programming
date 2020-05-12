#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let jsonObject;
let total = 0;
request.get(url, 'utf8', function (err, response, body) {
  if (err) throw err;
  jsonObject = JSON.parse(body);
  for (let y = 0; y < jsonObject.results.length; y++) {
    const characters = jsonObject.results[y].characters;
    if (characters.filter(str => str.includes('people/18/')).length !== 0) {
      total++;
    }
  }
  console.log(total);
});
