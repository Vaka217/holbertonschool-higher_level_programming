#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
if (args[0] === 'https://swapi-api.hbtn.io/api/films/') {
  args[0] = 'https://swapi-api.alx-tools.com/api/films/';
}
request(args[0], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const i in results) {
      if (results[i].characters.find(character => character.endsWith('/18/'))) {
        count++;
      }
    }
    console.log(count);
  }
});
