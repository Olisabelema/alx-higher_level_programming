#!/usr/bin/node

const argv1 = process.argv[2];

if (!Number(argv1)) {
  console.log('Missing size');
} else {
  for (let k = 0; k < argv1; k++) {
    let output = '';
    for (let l = 0; l < argv1; l++) {
      output += 'X';
    }
    console.log(output);
  }
}
