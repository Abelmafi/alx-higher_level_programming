#!/usr/bin/node
const oldSquare = require('./5-square');
class Square extends oldSquare {
  charPrint (c) {
    let m = c;
    if (!c) {
      m = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(m.repeat(this.width));
    }
  }
}
module.exports = Square;
