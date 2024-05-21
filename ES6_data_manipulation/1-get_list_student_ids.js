export default function getlistStudentids(getListStudents) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  return getListStudents.map((student) => student.id);
}
