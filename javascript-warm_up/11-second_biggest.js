#!/usr/bin/node
let args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  args = args.sort((a, b) => a - b);
  console.log(parseInt(args[args.length - 2]));
}
