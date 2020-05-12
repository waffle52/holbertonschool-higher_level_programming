#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
// let content = fs.readFileSync(process.cwd() + '/' + filename).toString();
fs.readFile(filename, (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data.toString());
  }
});
