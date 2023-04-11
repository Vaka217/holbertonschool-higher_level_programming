#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let count = 0;
    for (const i in list) {
        count += list[i] == searchElement ? 1 : 0;
    }
    return count;
};
