#!/usr/bin/node

/*
 * argv[0] = path where the node.js program is located
 * argv[1] = path to thecurrently executed file
 * argv[2] = the first argument passed to the program
 */

const argv1 = process.argv[2];
const argv2 = process.argv[3];
console.log(argv1 + ' is ' + argv2);
