#!/usr/bin/node
const args = process.argv.slice(2);
if (Array.isArray(args) && args[0] === undefined) {
  console.log('No argument');
}
console.log(args[0]);
