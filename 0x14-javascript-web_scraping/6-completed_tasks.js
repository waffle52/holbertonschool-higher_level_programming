#!/usr/bin/node

const request = require('request');
let jsonObj;
const List = {};
let track = 0;
const url = process.argv[2];
let curNum = 0;

request.get(url, 'utf8', function (err, response, body) {
  if (err) {
    console.log(err);
  }
  jsonObj = JSON.parse(body);
  curNum = jsonObj[0].userId;
  list(jsonObj, 0, curNum);
  console.log(List);
});

function list (jsonObj, idx, curNum) {
  if (idx >= jsonObj.length) {
    List[curNum] = track;
    return;
  }
  if (curNum !== jsonObj[idx].userId) {
    List[curNum] = track;
    curNum = jsonObj[idx].userId;
    track = 0;
  }
  if (jsonObj[idx].completed === true) {
    track++;
  }
  list(jsonObj, idx + 1, curNum);
}
