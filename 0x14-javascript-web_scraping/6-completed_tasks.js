#!/usr/bin/node

const request = require('request');
const list = {};
const url = process.argv[2];

request.get(url, 'utf8', function (err, response, body) {
  if (err) { throw (err); }

  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed === true) {
      if (!(data[i].userId in list)) {
        list[data[i].userId] = 0;
      }
      list[data[i].userId] += 1;
    }
  }
  console.log(list);
});
