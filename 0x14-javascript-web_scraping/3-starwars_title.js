#!/usr/bin/node
const request = require('request');
const Movieid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + Movieid;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
