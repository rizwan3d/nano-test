"""
Interfaces module - Contains abstract base classes (interfaces).
Follows Interface Segregation Principle (ISP) and Dependency Inversion Principle (DIP).
"""

from abc import ABC, abstractmethod
from typing import List
from models import Student, Grade


class IGradingStrategy(ABC):
    """
    Interface for grading strategies.
    Follows Open/Closed Principle - can add new strategies without modifying existing code.
    """
    
    @abstractmethod
    def calculate_gpa(self, grades: List[Grade]) -> float:
        """
        Calculate GPA from a list of grades.
        
        Args:
            grades: List of Grade objects
            
        Returns:
            Calculated GPA as float
        """
        pass
    
    @abstractmethod
    def get_letter_grade(self, grade: Grade) -> str:
        """
        Convert a numeric grade to letter grade.
        
        Args:
            grade: Grade object
            
        Returns:
            Letter grade as string (A, B, C, D, F)
        """
        pass


class IGradeRepository(ABC):
    """
    Interface for grade repository (data access).
    Follows Repository Pattern and Dependency Inversion Principle.
    """
    
    @abstractmethod
    def save_grade(self, student_id: str, grade: Grade) -> None:
        """Save a grade for a student."""
        pass
    
    @abstractmethod
    def get_grades(self, student_id: str) -> List[Grade]:
        """Retrieve all grades for a student."""
        pass
    
    @abstractmethod
    def get_all_students(self) -> List[str]:
        """Get all student IDs."""
        pass


class IStudentRepository(ABC):
    """
    Interface for student repository.
    Segregated from grade repository following Interface Segregation Principle.
    """
    
    @abstractmethod
    def add_student(self, student: Student) -> None:
        """Add a new student."""
        pass
    
    @abstractmethod
    def get_student(self, student_id: str) -> Student:
        """Get a student by ID."""
        pass
    
    @abstractmethod
    def get_all_students(self) -> List[Student]:
        """Get all students."""
        pass
