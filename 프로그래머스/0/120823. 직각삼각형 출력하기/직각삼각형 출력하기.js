const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    for(let i=1; i<=input[0]; i++) {
        console.log(repeat("*",i));
    }
});

const repeat = (str, num) => {
    let repeatStr = '';
    for(let i=0; i<num; i++) {
        repeatStr += str;
    }
    return repeatStr;
}