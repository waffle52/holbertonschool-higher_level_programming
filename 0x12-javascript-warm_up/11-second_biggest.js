#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log('0');
} else {
  let biggest = myArgs[0];
  let nextBig = myArgs[0];
  for (let i = 0; i < myArgs.length; i++) {
    if (myArgs[i] > biggest) {
      nextBig = biggest;
      biggest = myArgs[i];
    } else if (myArgs[i] > nextBig && myArgs[i] !== biggest) {
      nextBig = myArgs[i];
    }
  }
  console.log(nextBig);
}
