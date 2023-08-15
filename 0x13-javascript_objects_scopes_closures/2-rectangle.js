#!/usr/bin/node

/*
Define a Rectangle class representing a rectangle shape.
Instance attributes: width, height;
Constructor arguments: w (width), h (height);
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
