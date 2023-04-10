#!/usr/bin/node
const args = process.argv.slice(2);
if (Array.isArray(args) && args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
