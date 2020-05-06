#!/usr/bin/node
if (parseInt(process.argv[2], 10)) {
  console.log('My number: ' + parseInt(process.argv[2], 10));
} else {
  console.log('Not a number');
}
