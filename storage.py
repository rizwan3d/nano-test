"""
Storage module - Contains repository implementations.
Follows Repository Pattern and Dependency Inversion Principle (DIP).
"""

from typing import List, Dict
from models import Student, Grade
from interfaces import IGradeRepository, IStudentRepository


class InMemoryGradeRepository(IGradeRepository):
    """In-memory implementation of grade repository."""
    
    def __init__(self):
        self._grades: Dict[str, List[Grade]] = {}  # student_id -> list of grades
    
    def save_grade(self, student_id: str, grade: Grade) -> None:
        """Save a grade for a student."""
        if student_id not in self._grades:
            self._grades[student_id] = []
        self._grades[student_id].append(grade)
    
    def get_grades(self, student_id: str) -> List[Grade]:
        """Retrieve all grades for a student."""
        return self._grades.get(student_id, []).copy()
    
    def get_all_students(self) -> List[str]:
        """Get all student IDs with grades."""
        return list(self._grades.keys())


class InMemoryStudentRepository(IStudentRepository):
    """In-memory implementation of student repository."""
    
    def __init__(self):
        self._students: Dict[str, Student] = {}
    
    def add_student(self, student: Student) -> None:
        """Add a new student."""
        self._students[student.student_id] = student
    
    def get_student(self, student_id: str) -> Student:
        """Get a student by ID."""
        if student_id not in self._students:
            raise ValueError(f"Student with ID {student_id} not found")
        return self._students[student_id]
    
    def get_all_students(self) -> List[Student]:
        """Get all students."""
        return list(self._students.values())
