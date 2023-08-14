#!/usr/bin/node

const numOccurrences = parseInt(process.argv[2]);

if (isNaN(numOccurrences) || numOccurrences <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let k = 0; k < numOccurrences; k++) {
    console.log('C is fun');
  }
}

