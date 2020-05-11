#!/usr/bin/node
let t = 0;

exports.logMe = function (item) {
  console.log(t + ': ' + item);
  t = t + 1;
};
