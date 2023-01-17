#!/usr/bin/node
const request = require('request');
const movieid = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieid;

request(url, async (error, response, body) => {
  if (error) { console.log(error); }
  const result = JSON.parse(body);

  for (const urls of result.characters) {
    await new Promise((resolve, reject) => {
      request(urls, (err, r, body) => {
        if (err) {
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
