#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
fs.appendFile(filename, process.argv[3], 'utf-8', function (err) {
  if (err) throw err;
});
