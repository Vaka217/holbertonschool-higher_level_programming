#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${args[0]}`;
console.log(url);
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(response.title);
});
