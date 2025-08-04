#!/usr/bin/env python3

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("Testing Calculator Application...")
print("=" * 50)

# Test 1: Import calculator module
try:
    from calculator import Calculator, CalculatorError
    print("✅ Calculator module imported successfully")
except ImportError as e:
    print(f"❌ Failed to import calculator module: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected error importing calculator: {e}")
    sys.exit(1)

# Test 2: Create calculator instance
try:
    calc = Calculator()
    print("✅ Calculator instance created successfully")
except Exception as e:
    print(f"❌ Failed to create calculator instance: {e}")
    sys.exit(1)

# Test 3: Basic operations
print("\nTesting basic operations:")
try:
    result = calc.add(5, 3)
    assert result == 8.0, f"Expected 8.0, got {result}"
    print(f"✅ Addition: 5 + 3 = {result}")
    
    result = calc.subtract(10, 4)
    assert result == 6.0, f"Expected 6.0, got {result}"
    print(f"✅ Subtraction: 10 - 4 = {result}")
    
    result = calc.multiply(6, 7)
    assert result == 42.0, f"Expected 42.0, got {result}"
    print(f"✅ Multiplication: 6 × 7 = {result}")
    
    result = calc.divide(15, 3)
    assert result == 5.0, f"Expected 5.0, got {result}"
    print(f"✅ Division: 15 ÷ 3 = {result}")
    
except Exception as e:
    print(f"❌ Error in basic operations: {e}")
    sys.exit(1)

# Test 4: Advanced operations
print("\nTesting advanced operations:")
try:
    result = calc.power(2, 8)
    assert result == 256.0, f"Expected 256.0, got {result}"
    print(f"✅ Power: 2 ^ 8 = {result}")
    
    result = calc.square_root(16)
    assert result == 4.0, f"Expected 4.0, got {result}"
    print(f"✅ Square root: √16 = {result}")
    
    result = calc.factorial(5)
    assert result == 120, f"Expected 120, got {result}"
    print(f"✅ Factorial: 5! = {result}")
    
except Exception as e:
    print(f"❌ Error in advanced operations: {e}")
    sys.exit(1)

# Test 5: Error handling
print("\nTesting error handling:")
try:
    calc.divide(5, 0)
    print("❌ Division by zero should have raised an error")
    sys.exit(1)
except CalculatorError:
    print("✅ Division by zero error handled correctly")
except Exception as e:
    print(f"❌ Unexpected error type for division by zero: {e}")
    sys.exit(1)

try:
    calc.square_root(-4)
    print("❌ Negative square root should have raised an error")
    sys.exit(1)
except CalculatorError:
    print("✅ Negative square root error handled correctly")
except Exception as e:
    print(f"❌ Unexpected error type for negative square root: {e}")
    sys.exit(1)

# Test 6: Memory operations
print("\nTesting memory operations:")
try:
    calc.memory_store(42)
    result = calc.memory_recall()
    assert result == 42.0, f"Expected 42.0, got {result}"
    print(f"✅ Memory store/recall: {result}")
    
    calc.memory_add(8)
    result = calc.memory_recall()
    assert result == 50.0, f"Expected 50.0, got {result}"
    print(f"✅ Memory add: {result}")
    
    calc.memory_clear()
    result = calc.memory_recall()
    assert result == 0.0, f"Expected 0.0, got {result}"
    print(f"✅ Memory clear: {result}")
    
except Exception as e:
    print(f"❌ Error in memory operations: {e}")
    sys.exit(1)

# Test 7: History tracking
print("\nTesting history tracking:")
try:
    calc.clear_history()  # Start fresh
    calc.add(1, 2)
    calc.multiply(3, 4)
    
    history = calc.get_history()
    assert len(history) == 2, f"Expected 2 history entries, got {len(history)}"
    print(f"✅ History tracking: {len(history)} entries recorded")
    
    last_result = calc.get_last_result()
    assert last_result == 12.0, f"Expected 12.0, got {last_result}"
    print(f"✅ Last result tracking: {last_result}")
    
except Exception as e:
    print(f"❌ Error in history tracking: {e}")
    sys.exit(1)

# Test 8: CLI import
print("\nTesting CLI import:")
try:
    from calculator_cli import CalculatorCLI
    cli = CalculatorCLI()
    print("✅ CLI module imported and instantiated successfully")
except Exception as e:
    print(f"❌ Error importing CLI: {e}")
    sys.exit(1)

print("\n" + "=" * 50)
print("🎉 ALL TESTS PASSED!")
print("The calculator application is working correctly.")
print("\nTo use the calculator:")
print("• Run 'python calculator_cli.py' for interactive mode")
print("• Run 'python demo.py' for a feature demonstration")
print("• Import Calculator class for programmatic use")
print("=" * 50)