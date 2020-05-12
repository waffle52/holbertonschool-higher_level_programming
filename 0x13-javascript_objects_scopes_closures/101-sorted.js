#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
let holder = [];

for (const [value, key] of Object.entries(dict)) {
  // new_dict[value] = key;

  if (newDict[key] !== undefined) {
    holder = newDict[key];
  }
  holder.push(value);
  newDict[key] = holder;
  holder = [];
}
console.log(newDict);
