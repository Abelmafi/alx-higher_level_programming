#!/usr/bin/node
const request = require('request');
const Movieid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + Movieid;

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  for (const urls of JSON.parse(body).characters) {
    request(urls, (error, response, body) => {
      console.log(JSON.parse(body).name);
  });
  }
});
