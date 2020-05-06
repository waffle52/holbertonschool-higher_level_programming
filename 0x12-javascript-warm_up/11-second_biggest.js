#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log('0');
} else {
  let biggest = parseInt(myArgs[0], 10);
  let nextBig = parseInt(myArgs[0], 10);
  for (let i = 0; i < myArgs.length; i++) {
    if (myArgs[i] > biggest) {
      nextBig = parseInt(biggest, 10);
      biggest = parseInt(myArgs[i], 10);
    } else if (parseInt(myArgs[i], 10) > nextBig && parseInt(myArgs[i], 10) !== biggest) {
      nextBig = parseInt(myArgs[i], 10);
    }
  }
  console.log(nextBig);
}
