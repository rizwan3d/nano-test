"""
Services module - Contains business logic services.
Follows Dependency Inversion Principle (DIP) and Single Responsibility Principle (SRP).
"""

from typing import List
from models import Student, Grade
from interfaces import IStudentRepository, IGradeRepository, IGradingStrategy


class GradeService:
    """
    Service for managing student grades.
    Depends on abstractions (interfaces) not concrete implementations.
    """
    
    def __init__(self, 
                 student_repo: IStudentRepository,
                 grade_repo: IGradeRepository,
                 grading_strategy: IGradingStrategy):
        """
        Initialize GradeService with dependencies.
        
        Args:
            student_repo: Repository for student data
            grade_repo: Repository for grade data
            grading_strategy: Strategy for grading calculations
        """
        self._student_repo = student_repo
        self._grade_repo = grade_repo
        self._grading_strategy = grading_strategy
    
    def add_student(self, student: Student) -> None:
        """Add a new student."""
        self._student_repo.add_student(student)
    
    def enroll_student(self, student_id: str, name: str) -> Student:
        """Create and enroll a new student."""
        student = Student(student_id, name)
        self.add_student(student)
        return student
    
    def add_grade(self, student_id: str, grade: Grade) -> None:
        """
        Add a grade for a student.
        
        Args:
            student_id: ID of the student
            grade: Grade to add
        """
        # Verify student exists
        student = self._student_repo.get_student(student_id)
        student.add_grade(grade)
        self._grade_repo.save_grade(student_id, grade)
    
    def get_student_gpa(self, student_id: str) -> float:
        """
        Get GPA for a student using the configured grading strategy.
        
        Args:
            student_id: ID of the student
            
        Returns:
            GPA as float
        """
        grades = self._grade_repo.get_grades(student_id)
        return self._grading_strategy.calculate_gpa(grades)
    
    def set_grading_strategy(self, strategy: IGradingStrategy) -> None:
        """
        Change the grading strategy at runtime.
        
        Args:
            strategy: New grading strategy to use
        """
        self._grading_strategy = strategy
    
    def get_student_letter_grades(self, student_id: str) -> List[str]:
        """
        Get letter grades for a student's grades.
        
        Args:
            student_id: ID of the student
            
        Returns:
            List of letter grades
        """
        grades = self._grade_repo.get_grades(student_id)
        return [self._grading_strategy.get_letter_grade(g) for g in grades]
    
    def get_student_report(self, student_id: str) -> str:
        """
        Generate a report for a student.
        
        Args:
            student_id: ID of the student
            
        Returns:
            Formatted report string
        """
        student = self._student_repo.get_student(student_id)
        grades = self._grade_repo.get_grades(student_id)
        gpa = self.get_student_gpa(student_id)
        letter_grades = self.get_student_letter_grades(student_id)
        
        report_lines = [
            f"Student Report for {student.name} (ID: {student.student_id})",
            f"Number of Grades: {len(grades)}",
            f"GPA: {gpa:.2f}",
            "Grades:"
        ]
        
        for grade, letter in zip(grades, letter_grades):
            report_lines.append(f"  {grade.subject}: {grade.value}/{grade.max_value} ({letter})")
        
        return "\n".join(report_lines)
    
    def get_all_students_report(self) -> str:
        """Generate a report for all students."""
        students = self._student_repo.get_all_students()
        if not students:
            return "No students enrolled."
        
        report_lines = ["All Students Report", "=" * 50]
        for student in students:
            gpa = self.get_student_gpa(student.student_id)
            report_lines.append(f"{student.name} (ID: {student.student_id}): GPA {gpa:.2f}")
        
        return "\n".join(report_lines)
