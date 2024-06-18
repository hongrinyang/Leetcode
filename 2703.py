function argumentsLength() {
  return arguments.length;
}

// Example usage:
console.log(argumentsLength(5)); // Output: 1
console.log(argumentsLength({}, null, "3")); // Output: 3
console.log(argumentsLength()); // Output: 0
