# Python Calculator Application

A comprehensive calculator application written in Python with both programmatic API and command-line interface.

## Features

### Basic Operations
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`, `×`)
- Division (`/`, `÷`)
- Power/Exponentiation (`^`, `**`)
- Modulo (`mod`)
- Square root (`sqrt`)
- Factorial (`!`)

### Advanced Operations
- Trigonometric functions: `sin`, `cos`, `tan` (supports both radians and degrees)
- Logarithmic functions: `ln`, `log`, `log10` (supports custom bases)

### Memory Functions
- Store value in memory (`ms`)
- Recall memory (`mr`)
- Clear memory (`mc`)
- Add to memory (`m+`)
- Subtract from memory (`m-`)

### Utility Features
- Calculation history tracking
- Error handling with descriptive messages
- Support for both integers and floating-point numbers
- Reset functionality

## Files

- `calculator.py` - Main calculator class with all operations
- `calculator_cli.py` - Interactive command-line interface
- `test_calculator.py` - Comprehensive unit tests
- `README.md` - This documentation file

## Usage

### Command Line Interface

Run the interactive calculator:

```bash
python calculator_cli.py
```

#### Example Commands:
```
Calculator> 5 + 3
Result: 8.0

Calculator> sqrt 16
Result: 4.0

Calculator> sin 90 deg
Result: 1.0

Calculator> 2 ^ 8
Result: 256.0

Calculator> ms 42
Stored 42.0 in memory.

Calculator> mr
Memory: 42.0

Calculator> history
Calculation History:
1. 5 + 3 = 8.0
2. √16 = 4.0
3. sin(90°) = 1.0
4. 2 ^ 8 = 256.0
5. M = 42.0
6. MR = 42.0

Calculator> help
[Shows detailed help information]

Calculator> quit
Calculator closed.
```

### Programmatic API

```python
from calculator import Calculator

# Create calculator instance
calc = Calculator()

# Basic operations
result = calc.add(5, 3)        # 8.0
result = calc.multiply(4, 6)   # 24.0
result = calc.divide(15, 3)    # 5.0

# Advanced operations
result = calc.power(2, 8)      # 256.0
result = calc.square_root(16)  # 4.0
result = calc.sin(90, degrees=True)  # 1.0

# Memory operations
calc.memory_store(42)
value = calc.memory_recall()   # 42.0
calc.memory_add(8)            # Memory now contains 50.0

# History and utilities
history = calc.get_history()
last_result = calc.get_last_result()
calc.clear_history()
calc.reset()  # Clear memory and history
```

## Error Handling

The calculator includes comprehensive error handling for:
- Division by zero
- Square root of negative numbers
- Logarithm of non-positive numbers
- Invalid factorial inputs
- Overflow conditions
- Invalid input formats

## Testing

Run the unit tests:

```bash
python test_calculator.py
```

Or using unittest module:

```bash
python -m unittest test_calculator.py -v
```

The test suite includes:
- Unit tests for all calculator operations
- Error condition testing
- Memory operation testing
- History tracking verification
- Integration tests for complex calculation sequences
- Edge case and boundary condition testing

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download the repository
2. Ensure Python 3.6+ is installed
3. Run the calculator:
   ```bash
   python calculator_cli.py
   ```

## Examples

### Basic Calculations
```python
calc = Calculator()
print(calc.add(10, 5))        # 15.0
print(calc.subtract(10, 3))   # 7.0
print(calc.multiply(4, 7))    # 28.0
print(calc.divide(20, 4))     # 5.0
```

### Scientific Calculations
```python
import math

calc = Calculator()
print(calc.power(2, 10))      # 1024.0
print(calc.square_root(144))  # 12.0
print(calc.factorial(5))      # 120
print(calc.sin(math.pi/2))    # 1.0
print(calc.log(math.e))       # 1.0
print(calc.log10(1000))       # 3.0
```

### Memory Operations
```python
calc = Calculator()
calc.memory_store(100)        # Store 100 in memory
calc.memory_add(50)           # Memory now contains 150
result = calc.memory_recall() # Returns 150.0
calc.memory_clear()           # Memory cleared to 0
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.