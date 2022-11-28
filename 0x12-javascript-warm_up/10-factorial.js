#!/usr/bin/node
const num = Number(process.argv[2]);

function factorial (a) {
  if (a >= 1) {
    return (a * factorial(a - 1));
  } else {
    return (1);
  }
}
console.log(factorial(num));
