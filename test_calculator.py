"""
Unit tests for the Calculator application.
Tests all calculator operations, memory functions, and error handling.
"""

import unittest
import math
from calculator import Calculator, CalculatorError


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up a fresh calculator instance for each test."""
        self.calc = Calculator()
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        # Addition
        self.assertEqual(self.calc.add(5, 3), 8.0)
        self.assertEqual(self.calc.add(-2, 7), 5.0)
        self.assertEqual(self.calc.add(0, 0), 0.0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        
        # Subtraction
        self.assertEqual(self.calc.subtract(10, 4), 6.0)
        self.assertEqual(self.calc.subtract(-5, -3), -2.0)
        self.assertEqual(self.calc.subtract(0, 5), -5.0)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)
        
        # Multiplication
        self.assertEqual(self.calc.multiply(6, 7), 42.0)
        self.assertEqual(self.calc.multiply(-3, 4), -12.0)
        self.assertEqual(self.calc.multiply(0, 100), 0.0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        
        # Division
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(-12, 4), -3.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
    
    def test_division_by_zero(self):
        """Test division by zero error handling."""
        with self.assertRaises(CalculatorError):
            self.calc.divide(5, 0)
        with self.assertRaises(CalculatorError):
            self.calc.divide(-3, 0)
    
    def test_power_operations(self):
        """Test power operations."""
        self.assertEqual(self.calc.power(2, 3), 8.0)
        self.assertEqual(self.calc.power(5, 0), 1.0)
        self.assertEqual(self.calc.power(4, 0.5), 2.0)
        self.assertEqual(self.calc.power(-2, 3), -8.0)
        self.assertEqual(self.calc.power(10, -1), 0.1)
    
    def test_square_root(self):
        """Test square root operations."""
        self.assertEqual(self.calc.square_root(16), 4.0)
        self.assertEqual(self.calc.square_root(0), 0.0)
        self.assertEqual(self.calc.square_root(2.25), 1.5)
        self.assertAlmostEqual(self.calc.square_root(2), math.sqrt(2), places=10)
        
        # Test negative number error
        with self.assertRaises(CalculatorError):
            self.calc.square_root(-4)
    
    def test_modulo_operations(self):
        """Test modulo operations."""
        self.assertEqual(self.calc.modulo(10, 3), 1.0)
        self.assertEqual(self.calc.modulo(15, 5), 0.0)
        self.assertEqual(self.calc.modulo(7.5, 2.5), 0.0)
        
        # Test modulo by zero error
        with self.assertRaises(CalculatorError):
            self.calc.modulo(5, 0)
    
    def test_factorial(self):
        """Test factorial operations."""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)
        
        # Test negative number error
        with self.assertRaises(CalculatorError):
            self.calc.factorial(-1)
        
        # Test non-integer error
        with self.assertRaises(CalculatorError):
            self.calc.factorial(3.5)
        
        # Test large number error
        with self.assertRaises(CalculatorError):
            self.calc.factorial(200)
    
    def test_trigonometric_functions(self):
        """Test trigonometric functions."""
        # Test in radians
        self.assertAlmostEqual(self.calc.sin(0), 0.0, places=10)
        self.assertAlmostEqual(self.calc.sin(math.pi/2), 1.0, places=10)
        self.assertAlmostEqual(self.calc.cos(0), 1.0, places=10)
        self.assertAlmostEqual(self.calc.cos(math.pi), -1.0, places=10)
        self.assertAlmostEqual(self.calc.tan(0), 0.0, places=10)
        self.assertAlmostEqual(self.calc.tan(math.pi/4), 1.0, places=10)
        
        # Test in degrees
        self.assertAlmostEqual(self.calc.sin(0, degrees=True), 0.0, places=10)
        self.assertAlmostEqual(self.calc.sin(90, degrees=True), 1.0, places=10)
        self.assertAlmostEqual(self.calc.cos(0, degrees=True), 1.0, places=10)
        self.assertAlmostEqual(self.calc.cos(180, degrees=True), -1.0, places=10)
        self.assertAlmostEqual(self.calc.tan(0, degrees=True), 0.0, places=10)
        self.assertAlmostEqual(self.calc.tan(45, degrees=True), 1.0, places=10)
    
    def test_logarithmic_functions(self):
        """Test logarithmic functions."""
        # Natural logarithm
        self.assertAlmostEqual(self.calc.log(math.e), 1.0, places=10)
        self.assertAlmostEqual(self.calc.log(1), 0.0, places=10)
        self.assertAlmostEqual(self.calc.log(math.e**2), 2.0, places=10)
        
        # Base-10 logarithm
        self.assertAlmostEqual(self.calc.log10(10), 1.0, places=10)
        self.assertAlmostEqual(self.calc.log10(100), 2.0, places=10)
        self.assertAlmostEqual(self.calc.log10(1), 0.0, places=10)
        
        # Custom base logarithm
        self.assertAlmostEqual(self.calc.log(8, 2), 3.0, places=10)
        self.assertAlmostEqual(self.calc.log(27, 3), 3.0, places=10)
        
        # Test error cases
        with self.assertRaises(CalculatorError):
            self.calc.log(0)  # log of zero
        with self.assertRaises(CalculatorError):
            self.calc.log(-5)  # log of negative
        with self.assertRaises(CalculatorError):
            self.calc.log(10, 0)  # invalid base
        with self.assertRaises(CalculatorError):
            self.calc.log(10, 1)  # invalid base
        with self.assertRaises(CalculatorError):
            self.calc.log10(-1)  # log10 of negative
    
    def test_memory_operations(self):
        """Test memory operations."""
        # Test initial memory state
        self.assertEqual(self.calc.memory, 0.0)
        self.assertEqual(self.calc.memory_recall(), 0.0)
        
        # Test memory store
        self.calc.memory_store(42.5)
        self.assertEqual(self.calc.memory, 42.5)
        self.assertEqual(self.calc.memory_recall(), 42.5)
        
        # Test memory add
        self.calc.memory_add(7.5)
        self.assertEqual(self.calc.memory, 50.0)
        
        # Test memory subtract
        self.calc.memory_subtract(10.0)
        self.assertEqual(self.calc.memory, 40.0)
        
        # Test memory clear
        self.calc.memory_clear()
        self.assertEqual(self.calc.memory, 0.0)
    
    def test_history_tracking(self):
        """Test calculation history tracking."""
        # Test initial state
        self.assertEqual(len(self.calc.get_history()), 0)
        self.assertIsNone(self.calc.get_last_result())
        
        # Perform some calculations
        result1 = self.calc.add(5, 3)
        result2 = self.calc.multiply(4, 6)
        result3 = self.calc.square_root(16)
        
        # Check history
        history = self.calc.get_history()
        self.assertEqual(len(history), 3)
        self.assertIn("5 + 3 = 8.0", history[0])
        self.assertIn("4 × 6 = 24.0", history[1])
        self.assertIn("√16 = 4.0", history[2])
        
        # Check last result
        self.assertEqual(self.calc.get_last_result(), result3)
        
        # Test history clear
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)
        self.assertIsNone(self.calc.get_last_result())
    
    def test_reset_functionality(self):
        """Test calculator reset functionality."""
        # Set up some state
        self.calc.add(5, 3)
        self.calc.memory_store(42)
        
        # Verify state exists
        self.assertGreater(len(self.calc.get_history()), 0)
        self.assertEqual(self.calc.memory, 42.0)
        self.assertIsNotNone(self.calc.get_last_result())
        
        # Reset calculator
        self.calc.reset()
        
        # Verify reset state
        self.assertEqual(len(self.calc.get_history()), 0)
        self.assertEqual(self.calc.memory, 0.0)
        self.assertIsNone(self.calc.get_last_result())
    
    def test_type_handling(self):
        """Test that calculator handles different numeric types correctly."""
        # Test with integers
        self.assertEqual(self.calc.add(5, 3), 8.0)
        
        # Test with floats
        self.assertEqual(self.calc.add(5.5, 3.2), 8.7)
        
        # Test mixed types
        self.assertEqual(self.calc.add(5, 3.5), 8.5)
        self.assertEqual(self.calc.multiply(2, 3.14), 6.28)
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Very large numbers
        large_num = 1e10
        self.assertEqual(self.calc.add(large_num, large_num), 2e10)
        
        # Very small numbers
        small_num = 1e-10
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2e-10, places=15)
        
        # Zero operations
        self.assertEqual(self.calc.multiply(0, 1000000), 0.0)
        self.assertEqual(self.calc.power(0, 5), 0.0)
        self.assertEqual(self.calc.power(5, 0), 1.0)
        
        # Negative numbers
        self.assertEqual(self.calc.add(-5, -3), -8.0)
        self.assertEqual(self.calc.multiply(-4, -6), 24.0)
        self.assertEqual(self.calc.divide(-12, -3), 4.0)


class TestCalculatorIntegration(unittest.TestCase):
    """Integration tests for calculator operations."""
    
    def setUp(self):
        """Set up a fresh calculator instance for each test."""
        self.calc = Calculator()
    
    def test_complex_calculation_sequence(self):
        """Test a sequence of complex calculations."""
        # Perform a series of calculations
        result1 = self.calc.add(10, 5)  # 15
        result2 = self.calc.multiply(result1, 2)  # 30
        result3 = self.calc.square_root(result2 + 6)  # sqrt(36) = 6
        result4 = self.calc.power(result3, 2)  # 36
        result5 = self.calc.divide(result4, 6)  # 6
        
        self.assertEqual(result5, 6.0)
        
        # Check that history contains all operations
        history = self.calc.get_history()
        self.assertEqual(len(history), 5)
    
    def test_memory_with_calculations(self):
        """Test memory operations combined with calculations."""
        # Store a value in memory
        self.calc.memory_store(10)
        
        # Perform calculations
        result1 = self.calc.add(5, 3)  # 8
        
        # Add result to memory
        self.calc.memory_add(result1)  # memory = 18
        
        # Use memory in calculation
        memory_value = self.calc.memory_recall()  # 18
        result2 = self.calc.multiply(memory_value, 2)  # 36
        
        self.assertEqual(result2, 36.0)
        self.assertEqual(self.calc.memory, 18.0)
    
    def test_trigonometric_calculations(self):
        """Test trigonometric function calculations."""
        # Calculate sin²(x) + cos²(x) = 1 for various angles
        angles = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2]
        
        for angle in angles:
            sin_val = self.calc.sin(angle)
            cos_val = self.calc.cos(angle)
            result = sin_val**2 + cos_val**2
            self.assertAlmostEqual(result, 1.0, places=10, 
                                 msg=f"sin²({angle}) + cos²({angle}) should equal 1")


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)