#!/usr/bin/node
exports.esrever = function (list) {
  const temp = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    temp[j] = list[i];
    j++;
  }
  return (temp);
};
