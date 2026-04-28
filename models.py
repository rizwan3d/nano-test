"""
Models module - Contains core domain entities.
Follows Single Responsibility Principle (SRP).
"""


class Student:
    """Represents a student with their basic information."""
    
    def __init__(self, student_id: str, name: str):
        """
        Initialize a Student.
        
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
        """
        self.student_id = student_id
        self.name = name
        self._grades = []
    
    def add_grade(self, grade) -> None:
        """
        Add a grade to the student's record.
        
        Args:
            grade: A Grade object to add
        """
        self._grades.append(grade)
    
    def get_grades(self) -> list:
        """Return a copy of the student's grades."""
        return self._grades.copy()
    
    def __str__(self) -> str:
        return f"Student(id={self.student_id}, name={self.name})"
    
    def __repr__(self) -> str:
        return f"Student('{self.student_id}', '{self.name}')"


class Grade:
    """Represents a grade with value, subject, and optional comments."""
    
    def __init__(self, value: float, subject: str, max_value: float = 100.0):
        """
        Initialize a Grade.
        
        Args:
            value: The numeric grade value
            subject: The subject this grade is for
            max_value: Maximum possible grade (default 100)
        """
        self.value = value
        self.subject = subject
        self.max_value = max_value
    
    def get_percentage(self) -> float:
        """Calculate the grade as a percentage."""
        return (self.value / self.max_value) * 100.0
    
    def __str__(self) -> str:
        return f"Grade(subject={self.subject}, value={self.value}/{self.max_value})"
    
    def __repr__(self) -> str:
        return f"Grade({self.value}, '{self.subject}', {self.max_value})"
