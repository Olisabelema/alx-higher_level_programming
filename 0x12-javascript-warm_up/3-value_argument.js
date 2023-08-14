#!/usr/bin/node

/*
 * argv[0] = path where the node.js program is located
 * argv[1] = path to the currenly executed file
 * argv[2] = the first argument provided when running the program
 */

const argument = process.argv[2];
console.log(argument ? argument : 'No argument');

