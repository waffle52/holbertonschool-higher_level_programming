#!/usr/bin/node
if (parseInt(process.argv[2], 10)) {
  let i;
  for (i = 0; i < parseInt(process.argv[2], 10); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
