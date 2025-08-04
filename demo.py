#!/usr/bin/env python3
"""
Demonstration script for the Calculator application.
Shows various calculator features and capabilities.
"""

from calculator import Calculator, CalculatorError

def main():
    print("=" * 60)
    print("PYTHON CALCULATOR - DEMONSTRATION")
    print("=" * 60)
    
    # Create calculator instance
    calc = Calculator()
    
    print("\n1. BASIC ARITHMETIC OPERATIONS")
    print("-" * 40)
    operations = [
        ("5 + 3", lambda: calc.add(5, 3)),
        ("10 - 4", lambda: calc.subtract(10, 4)),
        ("6 × 7", lambda: calc.multiply(6, 7)),
        ("15 ÷ 3", lambda: calc.divide(15, 3)),
        ("2 ^ 8", lambda: calc.power(2, 8)),
        ("√16", lambda: calc.square_root(16)),
        ("5!", lambda: calc.factorial(5)),
        ("17 mod 5", lambda: calc.modulo(17, 5))
    ]
    
    for description, operation in operations:
        result = operation()
        print(f"{description:12} = {result}")
    
    print("\n2. ADVANCED MATHEMATICAL FUNCTIONS")
    print("-" * 40)
    import math
    
    advanced_ops = [
        ("sin(90°)", lambda: calc.sin(90, degrees=True)),
        ("cos(0°)", lambda: calc.cos(0, degrees=True)),
        ("tan(45°)", lambda: calc.tan(45, degrees=True)),
        ("sin(π/2)", lambda: calc.sin(math.pi/2)),
        ("ln(e)", lambda: calc.log(math.e)),
        ("log₁₀(100)", lambda: calc.log10(100)),
        ("log₂(8)", lambda: calc.log(8, 2))
    ]
    
    for description, operation in advanced_ops:
        result = operation()
        print(f"{description:12} = {result:.6f}")
    
    print("\n3. MEMORY OPERATIONS")
    print("-" * 40)
    calc.memory_store(25)
    print(f"Store 25 in memory")
    print(f"Memory recall: {calc.memory_recall()}")
    
    calc.memory_add(15)
    print(f"Add 15 to memory")
    print(f"Memory now: {calc.memory_recall()}")
    
    calc.memory_subtract(10)
    print(f"Subtract 10 from memory")
    print(f"Memory now: {calc.memory_recall()}")
    
    print("\n4. ERROR HANDLING DEMONSTRATION")
    print("-" * 40)
    
    error_tests = [
        ("Division by zero", lambda: calc.divide(5, 0)),
        ("Square root of negative", lambda: calc.square_root(-4)),
        ("Logarithm of zero", lambda: calc.log(0)),
        ("Factorial of negative", lambda: calc.factorial(-1))
    ]
    
    for description, operation in error_tests:
        try:
            result = operation()
            print(f"❌ {description}: Should have raised an error but got {result}")
        except CalculatorError as e:
            print(f"✅ {description}: {e}")
    
    print("\n5. CALCULATION HISTORY")
    print("-" * 40)
    history = calc.get_history()
    print(f"Total operations performed: {len(history)}")
    print("Last 10 operations:")
    for i, entry in enumerate(history[-10:], 1):
        print(f"{i:2d}. {entry}")
    
    print(f"\nLast result: {calc.get_last_result()}")
    
    print("\n6. COMPLEX CALCULATION EXAMPLE")
    print("-" * 40)
    # Calculate: ((5 + 3) × 2)² ÷ 4 - √16
    step1 = calc.add(5, 3)          # 8
    step2 = calc.multiply(step1, 2)  # 16
    step3 = calc.power(step2, 2)     # 256
    step4 = calc.divide(step3, 4)    # 64
    step5 = calc.square_root(16)     # 4
    final = calc.subtract(step4, step5)  # 60
    
    print("Complex calculation: ((5 + 3) × 2)² ÷ 4 - √16")
    print(f"Step by step:")
    print(f"  5 + 3 = {step1}")
    print(f"  {step1} × 2 = {step2}")
    print(f"  {step2}² = {step3}")
    print(f"  {step3} ÷ 4 = {step4}")
    print(f"  √16 = {step5}")
    print(f"  {step4} - {step5} = {final}")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("The calculator supports:")
    print("• Basic arithmetic operations")
    print("• Advanced mathematical functions")
    print("• Memory operations")
    print("• Comprehensive error handling")
    print("• Calculation history tracking")
    print("• Both programmatic API and CLI interface")
    print("\nRun 'python calculator_cli.py' for interactive mode!")

if __name__ == "__main__":
    main()