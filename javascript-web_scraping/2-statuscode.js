#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
request(args[0], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});
