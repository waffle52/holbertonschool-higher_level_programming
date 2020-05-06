#!/usr/bin/node
if (parseInt(process.argv[2], 10)) {
  let i;
  let j;
  let test = '';
  for (i = 0; i < parseInt(process.argv[2], 10); i++) {
    for (j = 0; j < parseInt(process.argv[2], 10); j++) {
      test = test.concat('X');
    }
    console.log(test);
    test = '';
  }
} else {
  console.log('Missing size');
}
