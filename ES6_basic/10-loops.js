export default function appendToEachArrayValue(array, appendString) {
  let newArray = [];
  for (let value of array) {
    newArray = newArray.concat(appendString + value);
  }
  return newArray;
}
