export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('name must be string');
    if (typeof length !== 'number') throw TypeError('lenght must be a number');
    if (!Array.isArray(students)) throw TypeError('students must be array of string');
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(newname) {
    if (typeof newname !== 'string') throw TypeError('name must be string');
    this._name = newname;
  }

  get name() {
    return this._name;
  }

  set length(newlenght) {
    if (!Array.isArray(newstudents)) throw TypeError('lenght must be a number');
    this._length = newlenght;
  }

  get length() {
    return this._length;
  }

  set students(newstudents) {
    if (typeof newstudents !== 'string') throw TypeError('students must be array of string');
    this._students = newstudents;
  }

  get students() {
    return this._students;
  }
}