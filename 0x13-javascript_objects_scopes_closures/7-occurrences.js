#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach(value => {
    if (value === searchElement) {
      counter++;
    }
  });
  return (counter);
};
