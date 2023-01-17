#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const fs = require('fs');
const filePath = process.argv[3];

request
  .get(url)
  .pipe(fs.createWriteStream(filePath));
