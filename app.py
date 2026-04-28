"""
Main application module - Demonstrates the student grading system.
Shows SOLID principles in action.
"""

from models import Student, Grade
from interfaces import IGradingStrategy
from grading_strategies import StandardGradingStrategy, PercentageGradingStrategy, EuropeanGradingStrategy
from storage import InMemoryStudentRepository, InMemoryGradeRepository
from services import GradeService


def main():
    """
    Main function demonstrating the student grading application.
    Shows how SOLID principles are applied.
    """
    print("=" * 60)
    print("Student Grading Application - SOLID Principles Demo")
    print("=" * 60)
    print()
    
    # Create repositories (Dependency Injection)
    student_repo = InMemoryStudentRepository()
    grade_repo = InMemoryGradeRepository()
    
    # Create grading strategy (Open/Closed Principle - can swap strategies)
    # Try changing to PercentageGradingStrategy() or EuropeanGradingStrategy()
    grading_strategy: IGradingStrategy = StandardGradingStrategy()
    
    # Create service with injected dependencies (Dependency Inversion Principle)
    grade_service = GradeService(student_repo, grade_repo, grading_strategy)
    
    # Add students
    print(">>> Enrolling students...")
    grade_service.enroll_student("S001", "Alice Johnson")
    grade_service.enroll_student("S002", "Bob Smith")
    grade_service.enroll_student("S003", "Charlie Brown")
    print("   Students enrolled successfully!")
    print()
    
    # Add grades for Alice
    print(">>> Adding grades for Alice...")
    grade_service.add_grade("S001", Grade(95, "Math"))
    grade_service.add_grade("S001", Grade(88, "Science"))
    grade_service.add_grade("S001", Grade(92, "English"))
    print("   Grades added for Alice!")
    print()
    
    # Add grades for Bob
    print(">>> Adding grades for Bob...")
    grade_service.add_grade("S002", Grade(78, "Math"))
    grade_service.add_grade("S002", Grade(85, "Science"))
    grade_service.add_grade("S002", Grade(82, "English"))
    print("   Grades added for Bob!")
    print()
    
    # Add grades for Charlie
    print(">>> Adding grades for Charlie...")
    grade_service.add_grade("S003", Grade(65, "Math"))
    grade_service.add_grade("S003", Grade(70, "Science"))
    grade_service.add_grade("S003", Grade(68, "English"))
    print("   Grades added for Charlie!")
    print()
    
    # Generate individual reports
    print("=" * 60)
    print("Individual Student Reports")
    print("=" * 60)
    for student_id in ["S001", "S002", "S003"]:
        print()
        print(grade_service.get_student_report(student_id))
        print()
    
    # Generate all students report
    print("=" * 60)
    print("All Students Summary")
    print("=" * 60)
    print()
    print(grade_service.get_all_students_report())
    print()
    
    # Demonstrate strategy swapping (Open/Closed Principle)
    print("=" * 60)
    print("Demonstrating Strategy Pattern (OCP)")
    print("=" * 60)
    print()
    print(">>> Switching to PercentageGradingStrategy...")
    grade_service.set_grading_strategy(PercentageGradingStrategy())
    print(f"   Alice's GPA (percentage): {grade_service.get_student_gpa('S001'):.1f}%")
    print()
    
    print(">>> Switching to EuropeanGradingStrategy...")
    grade_service.set_grading_strategy(EuropeanGradingStrategy())
    print(f"   Alice's GPA (European 1-10 scale): {grade_service.get_student_gpa('S001'):.1f}")
    print()
    
    print("=" * 60)
    print("Application Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
