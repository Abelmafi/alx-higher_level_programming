#!/usr/bin/node

const fs = require('fs')
const process = require('process')
var file_path = process.argvi[2];

fs.readFile(file_path, 'utf8', function(err, data){
	if (err) { console.log(err); } else { console.log(data); }
});
