export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents
    .filter((students) => students.location === city)
    .map((students) => {
      const grade = newGrades.find((grade) => grade.studentId === students.id);
      return {
        ...students,
        grade: grade ? grade.grade : 'N/A',
      };
    });
}
