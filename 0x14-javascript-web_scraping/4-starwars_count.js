#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const urll = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  let count = 0;
  for (const result of JSON.parse(body).results) {
    for (const characterURL of result.characters) {
      if (characterURL.includes(18)) {
        count++;
      }
    }
  }
  console.log(count);
});
