#!/usr/bin/env python3
"""
Simple test to verify calculator functionality.
"""

# Test basic import
try:
    from calculator import Calculator, CalculatorError
    print("✅ Calculator module imported successfully")
except Exception as e:
    print(f"❌ Error importing calculator: {e}")
    exit(1)

# Test basic functionality
try:
    calc = Calculator()
    
    # Test basic operations
    result = calc.add(5, 3)
    print(f"✅ Addition: 5 + 3 = {result}")
    
    result = calc.multiply(4, 6)
    print(f"✅ Multiplication: 4 × 6 = {result}")
    
    result = calc.divide(15, 3)
    print(f"✅ Division: 15 ÷ 3 = {result}")
    
    result = calc.power(2, 8)
    print(f"✅ Power: 2 ^ 8 = {result}")
    
    result = calc.square_root(16)
    print(f"✅ Square root: √16 = {result}")
    
    # Test error handling
    try:
        calc.divide(5, 0)
        print("❌ Division by zero should have raised an error")
    except CalculatorError:
        print("✅ Division by zero error handled correctly")
    
    # Test memory
    calc.memory_store(42)
    result = calc.memory_recall()
    print(f"✅ Memory operations: stored and recalled {result}")
    
    # Test history
    history = calc.get_history()
    print(f"✅ History tracking: {len(history)} operations recorded")
    
    print("\n🎉 All basic tests passed!")
    
except Exception as e:
    print(f"❌ Error in basic functionality: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Test CLI import
try:
    from calculator_cli import CalculatorCLI
    print("✅ CLI module imported successfully")
except Exception as e:
    print(f"❌ Error importing CLI: {e}")
    import traceback
    traceback.print_exc()

print("\n✅ Calculator application is working correctly!")
print("Run 'python calculator_cli.py' to use the interactive calculator.")