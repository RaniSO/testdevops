#!/usr/bin/env python3
"""
Test runner script to execute calculator tests and demonstrate functionality.
"""

import sys
import unittest
import traceback

def run_unit_tests():
    """Run the unit test suite."""
    print("=" * 60)
    print("RUNNING CALCULATOR UNIT TESTS")
    print("=" * 60)
    
    try:
        # Import and run tests
        from test_calculator import TestCalculator, TestCalculatorIntegration
        
        # Create test suite
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        
        # Add test cases
        suite.addTests(loader.loadTestsFromTestCase(TestCalculator))
        suite.addTests(loader.loadTestsFromTestCase(TestCalculatorIntegration))
        
        # Run tests
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        # Print summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Tests run: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        
        if result.failures:
            print("\nFAILURES:")
            for test, traceback in result.failures:
                print(f"- {test}: {traceback}")
        
        if result.errors:
            print("\nERRORS:")
            for test, traceback in result.errors:
                print(f"- {test}: {traceback}")
        
        return result.wasSuccessful()
        
    except Exception as e:
        print(f"Error running tests: {e}")
        traceback.print_exc()
        return False

def test_basic_functionality():
    """Test basic calculator functionality manually."""
    print("\n" + "=" * 60)
    print("TESTING BASIC CALCULATOR FUNCTIONALITY")
    print("=" * 60)
    
    try:
        from calculator import Calculator, CalculatorError
        
        calc = Calculator()
        
        # Test basic operations
        print("Testing basic operations:")
        print(f"5 + 3 = {calc.add(5, 3)}")
        print(f"10 - 4 = {calc.subtract(10, 4)}")
        print(f"6 × 7 = {calc.multiply(6, 7)}")
        print(f"15 ÷ 3 = {calc.divide(15, 3)}")
        print(f"2 ^ 8 = {calc.power(2, 8)}")
        print(f"√16 = {calc.square_root(16)}")
        print(f"5! = {calc.factorial(5)}")
        
        # Test advanced operations
        print("\nTesting advanced operations:")
        print(f"sin(90°) = {calc.sin(90, degrees=True)}")
        print(f"cos(0°) = {calc.cos(0, degrees=True)}")
        print(f"ln(e) = {calc.log(2.718281828459045)}")
        print(f"log₁₀(100) = {calc.log10(100)}")
        
        # Test memory operations
        print("\nTesting memory operations:")
        calc.memory_store(42)
        print(f"Stored 42 in memory")
        print(f"Memory recall: {calc.memory_recall()}")
        calc.memory_add(8)
        print(f"Added 8 to memory: {calc.memory_recall()}")
        
        # Test history
        print("\nCalculation history:")
        history = calc.get_history()
        for i, entry in enumerate(history[-5:], 1):
            print(f"{i}. {entry}")
        
        # Test error handling
        print("\nTesting error handling:")
        try:
            calc.divide(5, 0)
        except CalculatorError as e:
            print(f"Division by zero error: {e}")
        
        try:
            calc.square_root(-4)
        except CalculatorError as e:
            print(f"Negative square root error: {e}")
        
        print("\nBasic functionality test completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error in basic functionality test: {e}")
        traceback.print_exc()
        return False

def test_cli_import():
    """Test that CLI can be imported without errors."""
    print("\n" + "=" * 60)
    print("TESTING CLI IMPORT")
    print("=" * 60)
    
    try:
        from calculator_cli import CalculatorCLI
        cli = CalculatorCLI()
        print("CLI imported successfully!")
        print("CLI instance created successfully!")
        return True
    except Exception as e:
        print(f"Error importing CLI: {e}")
        traceback.print_exc()
        return False

def main():
    """Main test runner."""
    print("Python Calculator Application - Test Suite")
    print("=" * 60)
    
    all_passed = True
    
    # Run unit tests
    if not run_unit_tests():
        all_passed = False
    
    # Test basic functionality
    if not test_basic_functionality():
        all_passed = False
    
    # Test CLI import
    if not test_cli_import():
        all_passed = False
    
    # Final summary
    print("\n" + "=" * 60)
    print("FINAL TEST SUMMARY")
    print("=" * 60)
    
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        print("The calculator application is working correctly.")
        print("\nTo use the calculator:")
        print("1. Run 'python calculator_cli.py' for interactive mode")
        print("2. Import Calculator class for programmatic use")
    else:
        print("❌ SOME TESTS FAILED!")
        print("Please review the errors above and fix the issues.")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())