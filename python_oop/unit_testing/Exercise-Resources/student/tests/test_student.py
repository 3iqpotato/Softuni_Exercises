from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student_with_no_courses = Student("bobi")
        self.student_with_courses = Student('koko', {'python': ['mql']})

    def test_initialization_student_with_no_courses(self):
        self.assertEqual('bobi', self.student_with_no_courses.name)
        self.assertEqual({}, self.student_with_no_courses.courses)

    def test_initialization_student_with_courses(self):
        self.assertEqual('koko', self.student_with_courses.name)
        self.assertEqual({'python': ['mql']}, self.student_with_courses.courses)

    def test_enroll_method_with_valid_course_name_and_notes(self):
        res = self.student_with_courses.enroll('python', ['bal'])
        self.assertEqual({'python': ['mql', 'bal']}, self.student_with_courses.courses)
        self.assertEqual("Course already added. Notes have been updated.", res)

    def test_enroll_method_with_third_atribute_y(self):
        res = self.student_with_courses.enroll('math', ['kur'], 'Y')
        self.assertEqual(['kur'], self.student_with_courses.courses['math'])
        self.assertEqual("Course and course notes have been added.", res)

    def test_enroll_method_with_third_atribute_empty_str(self):
        res = self.student_with_courses.enroll('math', ['kur'], '')
        self.assertEqual(['kur'], self.student_with_courses.courses['math'])
        self.assertEqual("Course and course notes have been added.", res)

    def test_enroll_method_with_not_added_course(self):
        res = self.student_with_no_courses.enroll('math', ['kok'], 'i')
        self.assertEqual({'math': []}, self.student_with_no_courses.courses)
        self.assertEqual("Course has been added.", res)

    def test_add_notes_method_with_invalid_course_name(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_no_courses.add_notes('math', ['kok'])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_with_valid_data(self):
        res = self.student_with_courses.add_notes('python', 'kur')
        self.assertEqual({'python': ['mql', 'kur']}, self.student_with_courses.courses)
        self.assertEqual("Notes have been updated", res)

    def test_leave_course_method_with_invalid_course_name(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course('koko')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_courses_with_valid_data(self):
        res = self.student_with_courses.leave_course('python')
        self.assertEqual({}, self.student_with_courses.courses)
        self.assertEqual("Course has been removed", res)










if __name__ == '__main__':
    main()