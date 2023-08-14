#!/usr/bin/node

const arr = 'C is fun';

if (!Number(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let k = 0; k < process.argv[2]; k++) {
    console.log(arr);
  }
}
