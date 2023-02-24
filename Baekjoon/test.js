let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let input = require('fs').readFileSync('test.txt').toString().split('\n');

let count = input[0];
let numbers = [];

for (let i = 1; i < input.length; i++) {
  if (input[i] !== '') {
    numbers.push(input[i].split(' '));
  }
}

const mod = 1000000007

let answer = 0

for (let i = 0; i < numbers.length; i++) {
    let numberator = parseInt(numbers[i][1])
    let denominator = parseInt(numbers[i][0])
    let x = 1
    while (true) {
        if ((x * mod + 1) % denominator == 0) {
            result = (x * mod +1) / (denominator)
            break
        } else {
            x += 1
        }
    }
    answer += (numberator * result) % mod
}

console.log(answer)