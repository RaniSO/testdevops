"""
Calculator Application
A comprehensive calculator with basic and advanced operations, memory functions, and history tracking.
"""

import math
from typing import List, Union, Optional


class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass


class Calculator:
    """
    A comprehensive calculator class with basic arithmetic, advanced operations,
    memory functions, and calculation history.
    """
    
    def __init__(self):
        """Initialize the calculator with empty memory and history."""
        self.memory: float = 0.0
        self.history: List[str] = []
        self.last_result: Optional[float] = None
    
    def _add_to_history(self, operation: str, result: float) -> None:
        """Add an operation to the calculation history."""
        self.history.append(f"{operation} = {result}")
        self.last_result = result
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers."""
        result = float(a + b)
        self._add_to_history(f"{a} + {b}", result)
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract b from a."""
        result = float(a - b)
        self._add_to_history(f"{a} - {b}", result)
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers."""
        result = float(a * b)
        self._add_to_history(f"{a} × {b}", result)
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b."""
        if b == 0:
            raise CalculatorError("Division by zero is not allowed")
        result = float(a / b)
        self._add_to_history(f"{a} ÷ {b}", result)
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Raise base to the power of exponent."""
        try:
            result = float(base ** exponent)
            self._add_to_history(f"{base} ^ {exponent}", result)
            return result
        except (OverflowError, ValueError) as e:
            raise CalculatorError(f"Power operation failed: {str(e)}")
    
    def square_root(self, number: Union[int, float]) -> float:
        """Calculate the square root of a number."""
        if number < 0:
            raise CalculatorError("Cannot calculate square root of negative number")
        result = float(math.sqrt(number))
        self._add_to_history(f"√{number}", result)
        return result
    
    def modulo(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Calculate a modulo b."""
        if b == 0:
            raise CalculatorError("Modulo by zero is not allowed")
        result = float(a % b)
        self._add_to_history(f"{a} mod {b}", result)
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate the factorial of n."""
        if not isinstance(n, int) or n < 0:
            raise CalculatorError("Factorial is only defined for non-negative integers")
        if n > 170:  # Prevent overflow
            raise CalculatorError("Number too large for factorial calculation")
        result = math.factorial(n)
        self._add_to_history(f"{n}!", result)
        return result
    
    def sin(self, angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate sine of an angle."""
        if degrees:
            angle = math.radians(angle)
        result = float(math.sin(angle))
        unit = "°" if degrees else "rad"
        self._add_to_history(f"sin({angle}{unit})", result)
        return result
    
    def cos(self, angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate cosine of an angle."""
        if degrees:
            angle = math.radians(angle)
        result = float(math.cos(angle))
        unit = "°" if degrees else "rad"
        self._add_to_history(f"cos({angle}{unit})", result)
        return result
    
    def tan(self, angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate tangent of an angle."""
        if degrees:
            angle = math.radians(angle)
        result = float(math.tan(angle))
        unit = "°" if degrees else "rad"
        self._add_to_history(f"tan({angle}{unit})", result)
        return result
    
    def log(self, number: Union[int, float], base: Union[int, float] = math.e) -> float:
        """Calculate logarithm of number with given base (default: natural log)."""
        if number <= 0:
            raise CalculatorError("Logarithm is only defined for positive numbers")
        if base <= 0 or base == 1:
            raise CalculatorError("Logarithm base must be positive and not equal to 1")
        
        if base == math.e:
            result = float(math.log(number))
            self._add_to_history(f"ln({number})", result)
        else:
            result = float(math.log(number, base))
            self._add_to_history(f"log_{base}({number})", result)
        return result
    
    def log10(self, number: Union[int, float]) -> float:
        """Calculate base-10 logarithm of number."""
        if number <= 0:
            raise CalculatorError("Logarithm is only defined for positive numbers")
        result = float(math.log10(number))
        self._add_to_history(f"log₁₀({number})", result)
        return result
    
    # Memory operations
    def memory_store(self, value: Union[int, float]) -> None:
        """Store a value in memory."""
        self.memory = float(value)
        self.history.append(f"M = {value}")
    
    def memory_recall(self) -> float:
        """Recall the value stored in memory."""
        self.history.append(f"MR = {self.memory}")
        return self.memory
    
    def memory_clear(self) -> None:
        """Clear the memory."""
        self.memory = 0.0
        self.history.append("MC")
    
    def memory_add(self, value: Union[int, float]) -> None:
        """Add a value to memory."""
        self.memory += float(value)
        self.history.append(f"M+ {value} = {self.memory}")
    
    def memory_subtract(self, value: Union[int, float]) -> None:
        """Subtract a value from memory."""
        self.memory -= float(value)
        self.history.append(f"M- {value} = {self.memory}")
    
    # Utility methods
    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()
        self.last_result = None
    
    def get_history(self) -> List[str]:
        """Get the calculation history."""
        return self.history.copy()
    
    def get_last_result(self) -> Optional[float]:
        """Get the last calculation result."""
        return self.last_result
    
    def reset(self) -> None:
        """Reset the calculator (clear memory and history)."""
        self.memory = 0.0
        self.history.clear()
        self.last_result = None


if __name__ == "__main__":
    # Simple demonstration
    calc = Calculator()
    
    print("Calculator Demo:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 × 7 = {calc.multiply(6, 7)}")
    print(f"15 ÷ 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print(f"√16 = {calc.square_root(16)}")
    
    print("\nHistory:")
    for entry in calc.get_history():
        print(f"  {entry}")