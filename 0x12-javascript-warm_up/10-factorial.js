#!/usr/bin/node
const num = fact(parseInt(process.argv[2], 10));

console.log(num);

function fact (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 0) {
    return 1;
  } else {
    return x * fact(x - 1);
  }
}
