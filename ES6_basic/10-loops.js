export default function appendToEachArrayValue(array, appendString) {
  let newArray = [];
  for (const value of array) {
    newArray = newArray.concat(appendString + value);
  }
  return newArray;
}
