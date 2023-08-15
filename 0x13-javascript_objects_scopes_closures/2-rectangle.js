#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      /* 
	If width or height is not a positive integer or is 0,
	create an empty object
	*/
      return {};
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;

