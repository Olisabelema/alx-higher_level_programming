#!/usr/bin/node

exports.esrever = function (list) {
  const newArr = [];
  for (let k = list.length - 1; k >= 0; k--) {
    newArr.push(list[k]);
  }
  return newArr;
};
