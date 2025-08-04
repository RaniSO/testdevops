"""
Calculator Command Line Interface
Interactive command-line interface for the calculator application.
"""

import sys
from typing import List, Optional
from calculator import Calculator, CalculatorError


class CalculatorCLI:
    """Command-line interface for the calculator."""
    
    def __init__(self):
        """Initialize the CLI with a calculator instance."""
        self.calculator = Calculator()
        self.running = True
    
    def display_welcome(self) -> None:
        """Display welcome message and instructions."""
        print("=" * 50)
        print("         PYTHON CALCULATOR")
        print("=" * 50)
        print("\nAvailable operations:")
        print("  Basic: +, -, *, /, ^, sqrt, mod, !")
        print("  Trigonometric: sin, cos, tan")
        print("  Logarithmic: ln, log, log10")
        print("  Memory: ms, mr, mc, m+, m-")
        print("  Utility: history, clear, reset, help, quit")
        print("\nType 'help' for detailed instructions.")
        print("Type 'quit' or 'exit' to exit the calculator.")
        print("-" * 50)
    
    def display_help(self) -> None:
        """Display detailed help information."""
        help_text = """
CALCULATOR HELP
===============

Basic Operations:
  <num1> + <num2>     Addition
  <num1> - <num2>     Subtraction
  <num1> * <num2>     Multiplication
  <num1> / <num2>     Division
  <num1> ^ <num2>     Power (exponentiation)
  <num1> mod <num2>   Modulo
  sqrt <num>          Square root
  <num>!              Factorial

Trigonometric Functions:
  sin <angle>         Sine (in radians)
  cos <angle>         Cosine (in radians)
  tan <angle>         Tangent (in radians)
  sin <angle> deg     Sine (in degrees)
  cos <angle> deg     Cosine (in degrees)
  tan <angle> deg     Tangent (in degrees)

Logarithmic Functions:
  ln <num>            Natural logarithm
  log <num>           Natural logarithm (same as ln)
  log10 <num>         Base-10 logarithm
  log <num> <base>    Logarithm with custom base

Memory Operations:
  ms <num>            Store number in memory
  mr                  Recall memory
  mc                  Clear memory
  m+ <num>            Add to memory
  m- <num>            Subtract from memory

Utility Commands:
  history             Show calculation history
  clear               Clear history
  reset               Reset calculator (clear memory and history)
  help                Show this help
  quit/exit           Exit calculator

Examples:
  5 + 3
  sqrt 16
  sin 90 deg
  2 ^ 8
  ms 42
  mr
"""
        print(help_text)
    
    def parse_input(self, user_input: str) -> Optional[float]:
        """Parse user input and execute the corresponding operation."""
        user_input = user_input.strip().lower()
        
        if not user_input:
            return None
        
        # Handle quit commands
        if user_input in ['quit', 'exit', 'q']:
            self.running = False
            return None
        
        # Handle utility commands
        if user_input == 'help':
            self.display_help()
            return None
        
        if user_input == 'history':
            self.show_history()
            return None
        
        if user_input == 'clear':
            self.calculator.clear_history()
            print("History cleared.")
            return None
        
        if user_input == 'reset':
            self.calculator.reset()
            print("Calculator reset.")
            return None
        
        # Handle memory operations
        if user_input == 'mr':
            result = self.calculator.memory_recall()
            print(f"Memory: {result}")
            return result
        
        if user_input == 'mc':
            self.calculator.memory_clear()
            print("Memory cleared.")
            return None
        
        # Parse mathematical expressions
        try:
            return self.parse_expression(user_input)
        except CalculatorError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Invalid input: {e}")
            return None
    
    def parse_expression(self, expression: str) -> float:
        """Parse and evaluate mathematical expressions."""
        tokens = expression.split()
        
        if len(tokens) == 0:
            raise ValueError("Empty expression")
        
        # Handle single number factorial
        if len(tokens) == 1 and tokens[0].endswith('!'):
            num_str = tokens[0][:-1]
            try:
                num = int(float(num_str))
                return float(self.calculator.factorial(num))
            except ValueError:
                raise ValueError("Invalid factorial expression")
        
        # Handle memory store
        if len(tokens) == 2 and tokens[0] == 'ms':
            value = float(tokens[1])
            self.calculator.memory_store(value)
            print(f"Stored {value} in memory.")
            return value
        
        # Handle memory add/subtract
        if len(tokens) == 2 and tokens[0] in ['m+', 'm-']:
            value = float(tokens[1])
            if tokens[0] == 'm+':
                self.calculator.memory_add(value)
                print(f"Added {value} to memory. Memory: {self.calculator.memory}")
            else:
                self.calculator.memory_subtract(value)
                print(f"Subtracted {value} from memory. Memory: {self.calculator.memory}")
            return self.calculator.memory
        
        # Handle square root
        if len(tokens) == 2 and tokens[0] == 'sqrt':
            num = float(tokens[1])
            return self.calculator.square_root(num)
        
        # Handle trigonometric functions
        if len(tokens) >= 2 and tokens[0] in ['sin', 'cos', 'tan']:
            angle = float(tokens[1])
            degrees = len(tokens) == 3 and tokens[2] == 'deg'
            
            if tokens[0] == 'sin':
                return self.calculator.sin(angle, degrees)
            elif tokens[0] == 'cos':
                return self.calculator.cos(angle, degrees)
            elif tokens[0] == 'tan':
                return self.calculator.tan(angle, degrees)
        
        # Handle logarithmic functions
        if len(tokens) >= 2 and tokens[0] in ['ln', 'log', 'log10']:
            num = float(tokens[1])
            
            if tokens[0] == 'ln' or (tokens[0] == 'log' and len(tokens) == 2):
                return self.calculator.log(num)
            elif tokens[0] == 'log10':
                return self.calculator.log10(num)
            elif tokens[0] == 'log' and len(tokens) == 3:
                base = float(tokens[2])
                return self.calculator.log(num, base)
        
        # Handle binary operations
        if len(tokens) == 3:
            try:
                num1 = float(tokens[0])
                operator = tokens[1]
                num2 = float(tokens[2])
                
                if operator == '+':
                    return self.calculator.add(num1, num2)
                elif operator == '-':
                    return self.calculator.subtract(num1, num2)
                elif operator in ['*', '×']:
                    return self.calculator.multiply(num1, num2)
                elif operator in ['/', '÷']:
                    return self.calculator.divide(num1, num2)
                elif operator in ['^', '**']:
                    return self.calculator.power(num1, num2)
                elif operator == 'mod':
                    return self.calculator.modulo(num1, num2)
                else:
                    raise ValueError(f"Unknown operator: {operator}")
            except ValueError as e:
                if "could not convert" in str(e):
                    raise ValueError("Invalid number format")
                raise e
        
        raise ValueError("Invalid expression format")
    
    def show_history(self) -> None:
        """Display the calculation history."""
        history = self.calculator.get_history()
        if not history:
            print("No calculations in history.")
        else:
            print("\nCalculation History:")
            print("-" * 30)
            for i, entry in enumerate(history[-10:], 1):  # Show last 10 entries
                print(f"{i:2d}. {entry}")
            if len(history) > 10:
                print(f"... and {len(history) - 10} more entries")
    
    def run(self) -> None:
        """Run the calculator CLI."""
        self.display_welcome()
        
        while self.running:
            try:
                user_input = input("\nCalculator> ").strip()
                
                if not user_input:
                    continue
                
                result = self.parse_input(user_input)
                
                if result is not None:
                    print(f"Result: {result}")
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except EOFError:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
        
        print("Calculator closed.")


def main():
    """Main function to run the calculator CLI."""
    cli = CalculatorCLI()
    cli.run()


if __name__ == "__main__":
    main()