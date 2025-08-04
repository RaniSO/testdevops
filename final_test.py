#!/usr/bin/env python3
"""
Final comprehensive test of the calculator application.
"""

def test_calculator():
    """Test the calculator functionality."""
    print("Testing Calculator Application")
    print("=" * 40)
    
    # Import test
    try:
        from calculator import Calculator, CalculatorError
        print("✅ Calculator imported successfully")
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False
    
    # Basic functionality test
    try:
        calc = Calculator()
        
        # Test basic operations
        assert calc.add(5, 3) == 8.0
        assert calc.subtract(10, 4) == 6.0
        assert calc.multiply(6, 7) == 42.0
        assert calc.divide(15, 3) == 5.0
        print("✅ Basic arithmetic operations work")
        
        # Test advanced operations
        assert calc.power(2, 3) == 8.0
        assert calc.square_root(16) == 4.0
        assert calc.factorial(5) == 120
        print("✅ Advanced operations work")
        
        # Test error handling
        try:
            calc.divide(5, 0)
            assert False, "Should have raised error"
        except CalculatorError:
            pass
        print("✅ Error handling works")
        
        # Test memory
        calc.memory_store(42)
        assert calc.memory_recall() == 42.0
        print("✅ Memory operations work")
        
        # Test history
        history = calc.get_history()
        assert len(history) > 0
        print("✅ History tracking works")
        
        return True
        
    except Exception as e:
        print(f"❌ Calculator test failed: {e}")
        return False

def test_cli():
    """Test CLI import."""
    try:
        from calculator_cli import CalculatorCLI
        cli = CalculatorCLI()
        print("✅ CLI imported successfully")
        return True
    except Exception as e:
        print(f"❌ CLI test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Python Calculator - Final Test")
    print("=" * 50)
    
    success = True
    
    if not test_calculator():
        success = False
    
    if not test_cli():
        success = False
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 ALL TESTS PASSED!")
        print("Calculator application is ready to use!")
        print("\nUsage:")
        print("• python calculator_cli.py - Interactive calculator")
        print("• python demo.py - Feature demonstration")
        print("• from calculator import Calculator - Programmatic use")
    else:
        print("❌ Some tests failed!")
    
    return success

if __name__ == "__main__":
    main()