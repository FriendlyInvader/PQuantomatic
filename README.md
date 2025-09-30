# PQuantomatic

Python Quant - A quantitative analysis library for Python.

## Installation

Install the package using pip:

```bash
pip install pquantomatic
```

Or install from source:

```bash
git clone https://github.com/FriendlyInvader/PQuantomatic.git
cd PQuantomatic
pip install -e .
```

## Usage

```python
from pquantomatic.example import hello, add

# Get a greeting
print(hello())  # Output: Hello from PQuantomatic!

# Perform calculations
result = add(2, 3)
print(result)  # Output: 5
```

## Development

### Setup Development Environment

1. Clone the repository
2. Install development dependencies:

```bash
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Running Tests with Coverage

```bash
pytest --cov=pquantomatic --cov-report=html
```

## License

MIT
