#!/usr/bin/node
const num = Number(process.argv[2]);
let i, j, x;
if (!num) {
  console.log('Missing size');
} else {
  for (i = 0; i < num; i++) {
    x = '';
    for (j = 0; j < num; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
