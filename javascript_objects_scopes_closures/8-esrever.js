#!/usr/bin/node
exports.esrever = function (list) {
    let rev_list = [];
    let j = 0;
    for (i = list.length - 1; i >= 0; i--) {
        rev_list[j] = list[i];
        j++;
    }
    return rev_list;
};