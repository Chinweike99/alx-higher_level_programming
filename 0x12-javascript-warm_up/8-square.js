#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
	for (let i = 0; i < size; i++) {
		let row = "";
		for (let k = 0; k < size; k++) {
			row += "X";
		}
		console.log(row);
	}
} else {
	console.log("Missing size");
}
