#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
request(args[0], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const tasks = {};
    todos.forEach((todo) => {
      if (todo.completed && !tasks[todo.userId]) {
        tasks[todo.userId] = 1;
      } else if (todo.completed && tasks[todo.userId]) {
        tasks[todo.userId] += 1;
      }
    });
    console.log(tasks);
  }
});
