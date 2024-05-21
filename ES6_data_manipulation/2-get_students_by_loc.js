export default function getStudentsByLocation(getListStudents, location) {
  return getListStudents.filter((students) => students.location === location);
}
