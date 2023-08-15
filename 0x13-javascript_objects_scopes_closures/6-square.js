#!/usr/bin/node

const BaseSquareModel = require('./5-square.js');

module.exports = class Square extends BaseSquareModel {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let k = 0; k < this.height; k++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
