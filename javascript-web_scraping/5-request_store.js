#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const fs = require('fs');
request(args[0]).pipe(fs.createWriteStream(args[1]));
