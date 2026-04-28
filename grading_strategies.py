"""
Grading strategies module - Contains concrete implementations of grading strategies.
Follows Open/Closed Principle (OCP) and Liskov Substitution Principle (LSP).
"""

from typing import List
from models import Grade
from interfaces import IGradingStrategy


class StandardGradingStrategy(IGradingStrategy):
    """
    Standard 4.0 scale grading strategy.
    Follows Liskov Substitution Principle - can be used anywhere IGradingStrategy is expected.
    """
    
    def calculate_gpa(self, grades: List[Grade]) -> float:
        """
        Calculate GPA on 4.0 scale from grades.
        
        Args:
            grades: List of Grade objects
            
        Returns:
            GPA on 4.0 scale
        """
        if not grades:
            return 0.0
        
        total_percentage = sum(grade.get_percentage() for grade in grades)
        average_percentage = total_percentage / len(grades)
        
        # Convert percentage to 4.0 scale
        if average_percentage >= 90:
            return 4.0
        elif average_percentage >= 80:
            return 3.0
        elif average_percentage >= 70:
            return 2.0
        elif average_percentage >= 60:
            return 1.0
        else:
            return 0.0
    
    def get_letter_grade(self, grade: Grade) -> str:
        """
        Convert numeric grade to letter grade (A, B, C, D, F).
        
        Args:
            grade: Grade object
            
        Returns:
            Letter grade
        """
        percentage = grade.get_percentage()
        
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        else:
            return 'F'


class PercentageGradingStrategy(IGradingStrategy):
    """
    Percentage-based grading strategy.
    Demonstrates Open/Closed Principle - new strategy without modifying existing code.
    """
    
    def calculate_gpa(self, grades: List[Grade]) -> float:
        """
        Calculate average percentage from grades.
        
        Args:
            grades: List of Grade objects
            
        Returns:
            Average percentage
        """
        if not grades:
            return 0.0
        
        total_percentage = sum(grade.get_percentage() for grade in grades)
        return total_percentage / len(grades)
    
    def get_letter_grade(self, grade: Grade) -> str:
        """
        Return percentage as string with % sign.
        
        Args:
            grade: Grade object
            
        Returns:
            Percentage as formatted string
        """
        return f"{grade.get_percentage():.1f}%"


class EuropeanGradingStrategy(IGradingStrategy):
    """
    European 1-10 scale grading strategy.
    Another example of Open/Closed Principle.
    """
    
    def calculate_gpa(self, grades: List[Grade]) -> float:
        """
        Calculate average grade on 1-10 scale.
        
        Args:
            grades: List of Grade objects
            
        Returns:
            Average grade on 1-10 scale
        """
        if not grades:
            return 0.0
        
        # Convert percentage to 1-10 scale
        total_percentage = sum(grade.get_percentage() for grade in grades)
        average_percentage = total_percentage / len(grades)
        
        # Map percentage to 1-10 scale
        return (average_percentage / 100.0) * 9.0 + 1.0
    
    def get_letter_grade(self, grade: Grade) -> str:
        """
        Return grade on 1-10 scale.
        
        Args:
            grade: Grade object
            
        Returns:
            Grade as string on 1-10 scale
        """
        percentage = grade.get_percentage()
        european_grade = (percentage / 100.0) * 9.0 + 1.0
        return f"{european_grade:.1f}"
