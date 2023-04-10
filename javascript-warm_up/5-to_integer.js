#!/usr/bin/node
const args = process.argv.slice(2);
number = parseInt(args[0]);
if (isNaN(number)){
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
