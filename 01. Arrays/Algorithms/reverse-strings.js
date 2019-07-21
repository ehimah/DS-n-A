//Implement a function that reverses a string using iteration...and then recursion!
function reverseStringIterative(str) {
  let arr = str.split('');
  let n = arr.length;
  for (let i = 0; i < n / 2; i++) {
    let temp = arr[i];
    arr[i] = arr[n - i - 1];
    arr[n - i - 1] = temp;
  }
  return arr.join('');
}

function reverseStringRecursive(str) {
  if (str.length <= 1) return str;
  return (
    str.charAt(str.length - 1) +
    reverseStringRecursive(str.substring(0, str.length - 1))
  );
}
// reverseString('yoyo mastery')
//should return: 'yretsam oyoy'
console.log('reverseStringRecursive=>', reverseStringRecursive('yoyo mastery'));
console.log('reverseStringIterative=>', reverseStringIterative('yoyo mastery'));
