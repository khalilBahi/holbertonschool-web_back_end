export default function cleanSet(set, startString) {
  if (startString.length === 0 || typeof startString !== 'string') {
    return '';
  }
  const result = [];

  for (const value of set) {
    if (value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    }
  }
  return result.join('-');
}
