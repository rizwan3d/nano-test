The implementation is complete and working. Here's a summary of the changes made:

## Summary

**Issue Fixed:** Breaking Encapsulation - Direct Access to Private Attributes

**Changes Made:**

1. **services.py** - Added a new public method `set_grading_strategy()` to the `GradeService` class:
   - This method provides a proper interface to change the grading strategy at runtime
   - Preserves encapsulation by removing the need to directly access the private `_grading_strategy` attribute

2. **app.py** - Updated to use the new public method:
   - Changed `grade_service._grading_strategy = PercentageGradingStrategy()` to `grade_service.set_grading_strategy(PercentageGradingStrategy())`
   - Changed `grade_service._grading_strategy = EuropeanGradingStrategy()` to `grade_service.set_grading_strategy(EuropeanGradingStrategy())`

3. **test_grading.py** - Updated the test case to use the new public method:
   - Changed `self.service._grading_strategy = PercentageGradingStrategy()` to `self.service.set_grading_strategy(PercentageGradingStrategy())`

**Validation:**
- All 27 unit tests pass
- The application runs correctly and demonstrates the strategy pattern using the public method
- The code now properly encapsulates the `_grading_strategy` attribute while still allowing runtime strategy changes

The changes follow the Open/Closed Principle - the behavior can be extended (swapping strategies) without modifying the internal implementation details directly.
