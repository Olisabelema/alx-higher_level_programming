#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let k = 0;

  while (k < x) {
    theFunction();
    k++;
  }
};
