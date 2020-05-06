#!/usr/bin/node
const num = add(process.argv[2], process.argv[3]);
console.log(num);

function add (a, b) {
  const testNum = parseInt(a, 10) + parseInt(b, 10);
  return testNum;
}
