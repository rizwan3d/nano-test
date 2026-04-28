The changes have been successfully implemented. The direct access to the private `_grading_strategy` attribute from outside the `GradeService` class has been replaced with a proper public method `set_grading_strategy()`.

## Summary of Changes

**Issue:** Breaking Encapsulation - Direct Access to Private Attributes

**Changes Made:**

1. **services.py** - Added a new public method `set_grading_strategy()` to the `GradeService` class:
   ```python
   def set_grading_strategy(self, strategy: IGradingStrategy) -> None:
       """Change the grading strategy at runtime."""
       self._grading_strategy = strategy
   ```

2. **app.py** - Updated to use the new public method:
   - Line 89: `grade_service.set_grading_strategy(PercentageGradingStrategy())` (was `grade_service._grading_strategy = PercentageGradingStrategy()`)
   - Line 94: `grade_service.set_grading_strategy(EuropeanGradingStrategy())` (was `grade_service._grading_strategy = EuropeanGradingStrategy()`)

3. **test_grading.py** - Updated the test to use the new public method:
   - Line 254: `self.service.set_grading_strategy(PercentageGradingStrategy())` (was `self.service._grading_strategy = PercentageGradingStrategy()`)

**Validation:**
- The code search confirms that `set_grading_strategy` is now being used in all three files
- The private attribute `_grading_strategy` is now only accessed within the `services.py` file (internally within the class), preserving encapsulation
- The public method follows the proper interface for changing the grading strategy at runtime

**Note:** The test execution could not be completed due to a sandbox environment issue with `bwrap`, but the code changes are syntactically correct and follow the requested pattern exactly as specified in the issue.
