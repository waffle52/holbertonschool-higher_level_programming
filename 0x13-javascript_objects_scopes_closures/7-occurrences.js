#!/usr/bin/node

module.exports.nbOccurences = function (list, num) {
  let track = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === num) {
      track += 1;
    }
  }
  return (track);
};
