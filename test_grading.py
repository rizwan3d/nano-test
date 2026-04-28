"""
Unit tests for student grading application.
Tests all components following SOLID principles.
"""

import unittest
from models import Student, Grade
from interfaces import IGradingStrategy, IGradeRepository, IStudentRepository
from grading_strategies import StandardGradingStrategy, PercentageGradingStrategy, EuropeanGradingStrategy
from storage import InMemoryGradeRepository, InMemoryStudentRepository
from services import GradeService


class TestStudent(unittest.TestCase):
    """Test cases for Student model."""
    
    def test_student_creation(self):
        """Test basic student creation."""
        student = Student("S001", "John Doe")
        self.assertEqual(student.student_id, "S001")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(len(student.get_grades()), 0)
    
    def test_add_grade_to_student(self):
        """Test adding grades to a student."""
        student = Student("S001", "John Doe")
        grade = Grade(95, "Math")
        student.add_grade(grade)
        self.assertEqual(len(student.get_grades()), 1)
        self.assertEqual(student.get_grades()[0].value, 95)
    
    def test_student_string_representation(self):
        """Test student string representation."""
        student = Student("S001", "John Doe")
        self.assertIn("S001", str(student))
        self.assertIn("John Doe", str(student))


class TestGrade(unittest.TestCase):
    """Test cases for Grade model."""
    
    def test_grade_creation(self):
        """Test basic grade creation."""
        grade = Grade(85, "Math")
        self.assertEqual(grade.value, 85)
        self.assertEqual(grade.subject, "Math")
        self.assertEqual(grade.max_value, 100.0)
    
    def test_grade_percentage(self):
        """Test percentage calculation."""
        grade = Grade(85, "Math")
        self.assertEqual(grade.get_percentage(), 85.0)
        
        grade_50 = Grade(50, "Science", 200)
        self.assertEqual(grade_50.get_percentage(), 25.0)
    
    def test_grade_string_representation(self):
        """Test grade string representation."""
        grade = Grade(90, "Math")
        self.assertIn("Math", str(grade))
        self.assertIn("90", str(grade))


class TestStandardGradingStrategy(unittest.TestCase):
    """Test cases for StandardGradingStrategy."""
    
    def setUp(self):
        self.strategy = StandardGradingStrategy()
    
    def test_calculate_gpa_empty_grades(self):
        """Test GPA calculation with no grades."""
        gpa = self.strategy.calculate_gpa([])
        self.assertEqual(gpa, 0.0)
    
    def test_calculate_gpa_with_grades(self):
        """Test GPA calculation with grades."""
        grades = [Grade(95, "Math"), Grade(85, "Science")]
        gpa = self.strategy.calculate_gpa(grades)
        # Average is 90%, which maps to 4.0
        self.assertEqual(gpa, 4.0)
    
    def test_get_letter_grade_a(self):
        """Test letter grade A."""
        grade = Grade(95, "Math")
        self.assertEqual(self.strategy.get_letter_grade(grade), 'A')
    
    def test_get_letter_grade_b(self):
        """Test letter grade B."""
        grade = Grade(85, "Science")
        self.assertEqual(self.strategy.get_letter_grade(grade), 'B')
    
    def test_get_letter_grade_f(self):
        """Test letter grade F."""
        grade = Grade(55, "English")
        self.assertEqual(self.strategy.get_letter_grade(grade), 'F')


class TestPercentageGradingStrategy(unittest.TestCase):
    """Test cases for PercentageGradingStrategy."""
    
    def setUp(self):
        self.strategy = PercentageGradingStrategy()
    
    def test_calculate_gpa_returns_percentage(self):
        """Test that GPA returns average percentage."""
        grades = [Grade(90, "Math"), Grade(80, "Science")]
        gpa = self.strategy.calculate_gpa(grades)
        self.assertEqual(gpa, 85.0)
    
    def test_get_letter_grade_returns_percentage(self):
        """Test that letter grade returns formatted percentage."""
        grade = Grade(87.5, "Math")
        letter = self.strategy.get_letter_grade(grade)
        self.assertIn("87.5%", letter)


class TestEuropeanGradingStrategy(unittest.TestCase):
    """Test cases for EuropeanGradingStrategy."""
    
    def setUp(self):
        self.strategy = EuropeanGradingStrategy()
    
    def test_calculate_gpa_european_scale(self):
        """Test GPA on European 1-10 scale."""
        grades = [Grade(100, "Math"), Grade(0, "Science")]
        gpa = self.strategy.calculate_gpa(grades)
        # Average 50% -> European grade should be around 5.5
        self.assertAlmostEqual(gpa, 5.5, places=1)
    
    def test_get_letter_grade_european(self):
        """Test letter grade on European scale."""
        grade = Grade(90, "Math")
        letter = self.strategy.get_letter_grade(grade)
        # 90% -> 9.1 on European scale
        self.assertIn("9.1", letter)


class TestInMemoryGradeRepository(unittest.TestCase):
    """Test cases for InMemoryGradeRepository."""
    
    def setUp(self):
        self.repo = InMemoryGradeRepository()
    
    def test_save_and_get_grades(self):
        """Test saving and retrieving grades."""
        grade = Grade(95, "Math")
        self.repo.save_grade("S001", grade)
        grades = self.repo.get_grades("S001")
        self.assertEqual(len(grades), 1)
        self.assertEqual(grades[0].value, 95)
    
    def test_get_grades_nonexistent_student(self):
        """Test getting grades for nonexistent student."""
        grades = self.repo.get_grades("NONEXISTENT")
        self.assertEqual(len(grades), 0)
    
    def test_get_all_students(self):
        """Test getting all student IDs."""
        self.repo.save_grade("S001", Grade(95, "Math"))
        self.repo.save_grade("S002", Grade(88, "Science"))
        students = self.repo.get_all_students()
        self.assertEqual(len(students), 2)
        self.assertIn("S001", students)
        self.assertIn("S002", students)


class TestInMemoryStudentRepository(unittest.TestCase):
    """Test cases for InMemoryStudentRepository."""
    
    def setUp(self):
        self.repo = InMemoryStudentRepository()
    
    def test_add_and_get_student(self):
        """Test adding and retrieving a student."""
        student = Student("S001", "John Doe")
        self.repo.add_student(student)
        retrieved = self.repo.get_student("S001")
        self.assertEqual(retrieved.student_id, "S001")
        self.assertEqual(retrieved.name, "John Doe")
    
    def test_get_nonexistent_student(self):
        """Test getting a nonexistent student raises error."""
        with self.assertRaises(ValueError):
            self.repo.get_student("NONEXISTENT")
    
    def test_get_all_students(self):
        """Test getting all students."""
        self.repo.add_student(Student("S001", "Alice"))
        self.repo.add_student(Student("S002", "Bob"))
        students = self.repo.get_all_students()
        self.assertEqual(len(students), 2)


class TestGradeService(unittest.TestCase):
    """Test cases for GradeService - integration tests."""
    
    def setUp(self):
        self.student_repo = InMemoryStudentRepository()
        self.grade_repo = InMemoryGradeRepository()
        self.strategy = StandardGradingStrategy()
        self.service = GradeService(self.student_repo, self.grade_repo, self.strategy)
    
    def test_enroll_student(self):
        """Test enrolling a student."""
        student = self.service.enroll_student("S001", "Alice")
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.student_id, "S001")
    
    def test_add_grade_and_get_gpa(self):
        """Test adding grades and calculating GPA."""
        self.service.enroll_student("S001", "Alice")
        self.service.add_grade("S001", Grade(95, "Math"))
        self.service.add_grade("S001", Grade(85, "Science"))
        gpa = self.service.get_student_gpa("S001")
        # Average 90% -> GPA 4.0
        self.assertEqual(gpa, 4.0)
    
    def test_get_student_letter_grades(self):
        """Test getting letter grades."""
        self.service.enroll_student("S001", "Alice")
        self.service.add_grade("S001", Grade(95, "Math"))
        self.service.add_grade("S001", Grade(85, "Science"))
        letters = self.service.get_student_letter_grades("S001")
        self.assertEqual(len(letters), 2)
        self.assertIn("A", letters)
        self.assertIn("B", letters)
    
    def test_get_student_report(self):
        """Test generating student report."""
        self.service.enroll_student("S001", "Alice")
        self.service.add_grade("S001", Grade(95, "Math"))
        report = self.service.get_student_report("S001")
        self.assertIn("Alice", report)
        self.assertIn("GPA", report)
        self.assertIn("Math", report)
    
    def test_get_all_students_report(self):
        """Test generating all students report."""
        self.service.enroll_student("S001", "Alice")
        self.service.enroll_student("S002", "Bob")
        report = self.service.get_all_students_report()
        self.assertIn("Alice", report)
        self.assertIn("Bob", report)
    
    def test_strategy_swapping(self):
        """Test swapping grading strategies (Open/Closed Principle)."""
        self.service.enroll_student("S001", "Alice")
        self.service.add_grade("S001", Grade(90, "Math"))
        
        # Standard strategy
        gpa_standard = self.service.get_student_gpa("S001")
        
        # Swap to percentage strategy using public method
        self.service.set_grading_strategy(PercentageGradingStrategy())
        gpa_percentage = self.service.get_student_gpa("S001")
        
        # They should be different
        self.assertNotEqual(gpa_standard, gpa_percentage)


if __name__ == "__main__":
    unittest.main(verbosity=2)
