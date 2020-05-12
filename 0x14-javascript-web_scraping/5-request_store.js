#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const filename = process.argv[3];
const url = process.argv[2];
request.get(url, 'utf8', function (err, response, body) {
  if (err) throw err;
  fs.appendFile(filename, body, 'utf8', function (err) {
    if (err) throw err;
  });
});
