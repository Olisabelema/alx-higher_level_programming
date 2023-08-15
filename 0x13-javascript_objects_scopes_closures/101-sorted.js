#!/usr/bin/node

const dict = require('./101-data.js').dict;

const invertedDict = {};

for (const key in dict) {
  if (invertedDict[dict[key]] === undefined) {
    invertedDict[dict[key]] = [];
  }
  invertedDict[dict[key]].push(key);
}
console.log(invertedDict);
