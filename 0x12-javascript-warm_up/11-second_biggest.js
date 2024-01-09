#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number).filter(num => !isNaN(num));
const numArgs = numbers.length;

if (numArgs === 0 || numArgs === 1) {
	console.log(0);
} else {
	const sortedNumbers = numbers.sort((a, b) => b - a);
	console.log(sortedNumbers[1]);
}
