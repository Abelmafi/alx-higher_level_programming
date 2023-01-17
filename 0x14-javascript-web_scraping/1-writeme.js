#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const Fwrite = process.argv[3];

fs.writeFile(filepath, Fwrite, function (err) {
  if (err) { console.log(err); }
});
