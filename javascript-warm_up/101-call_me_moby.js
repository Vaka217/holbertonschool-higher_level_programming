#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  for (x; x > 0; x--) func();
};
