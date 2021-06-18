function hex2bin(hexString) {
  var result = [];

  for (let index = 0; index < hexString.length; index += 2) {
    let hex = hexString.substring(index, index + 2);
    let code = parseInt(hex, 16);
    let char = String.fromCharCode(code);

    result.push(char);
  }

  return result;
}

let secret = "3d3d516343746d4d6d6c315669563362";
let binary_array = hex2bin(secret);
let reversed_binary = binary_array.reverse();
let decoded_secret = atob(reversed_binary.join(''));

console.log(decoded_secret);
