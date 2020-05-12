#!/usr/bin/node
// console.log(process.argv[2]);
const list = [];
const fs = require('fs');
let filename = process.argv[2];
let content = fs.readFileSync(process.cwd() + '/' + filename).toString();
list.push(content);
filename = process.argv[3];
content = fs.readFileSync(process.cwd() + '/' + filename).toString();
list.push(content);

fs.appendFile(process.argv[4], list[0], function (err) {
  if (err) throw err;
});
fs.appendFile(process.argv[4], list[1], function (err) {
  if (err) throw err;
});
