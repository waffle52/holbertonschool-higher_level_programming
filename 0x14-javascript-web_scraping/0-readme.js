#!/usr/bin/node
'use strict';
const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data.toString());
  }
});
