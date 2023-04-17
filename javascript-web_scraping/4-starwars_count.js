#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
args[0] = 'https://swapi-api.alx-tools.com/api/films/'
request(args[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const i in results) {
      if (results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
