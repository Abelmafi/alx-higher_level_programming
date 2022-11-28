#!/usr/bin/node
const num = process.argv[2];
if (!Number(num)) {
  console.log('Not number');
} else {
  console.log('My number: ' + Number(num));
}
