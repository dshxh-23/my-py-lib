# MY-LIB

A collection of simple, reusable Python utility functions for input handling and console output. Designed for beginner developers and anyone who wants to avoid rewriting common input and display logic. This library is open source and intended for public use.

## Features

- **User Input Helpers**: Safely prompt for integers, positive integers, floats, positive floats, and choices from a list.
- **Console Output Utility**: Print animated ellipsis after a message, useful for CLI feedback.
- **Easy to Use**: Minimal dependencies, type-annotated, and beginner-friendly.
- **More features coming soon...**

## Installation

You can copy the `src/my_lib` folder into your own project, or copy and paste individual functions as needed.


## Usage

### Importing
```python
from my_lib import hello
from my_lib.getters import get_int, get_positive_int, get_float, get_positive_float, get_choice
from my_lib.utilities import print_ellipsis
```

### Example: Input Functions
```python
age = get_positive_int("Enter your age: ")
score = get_float("Enter your score: ", min_value=0.0, max_value=100.0)
color = get_choice("red", "green", "blue", prompt="Pick a color")
```

### Example: Animated Ellipsis
```python
print_ellipsis("Loading", n=5, delay=0.5)
```

### Example: Hello
```python
print(hello())  # Output: Hello from my-lib!
```

## API Reference

### `hello()`
Returns a friendly hello string.

### `get_int(prompt, min_value, max_value)`
Prompt for an integer between `min_value` and `max_value`.

### `get_positive_int(prompt, max_value)`
Prompt for a positive integer up to `max_value`.

### `get_float(prompt, min_value, max_value)`
Prompt for a float between `min_value` and `max_value`.

### `get_positive_float(prompt, max_value)`
Prompt for a positive float up to `max_value`.

### `get_choice(*choices, prompt, exact_match)`
Prompt for a string from a list of choices. Case-insensitive by default.

### `print_ellipsis(s, n, delay)`
Print a string followed by `n` animated periods, with `delay` seconds between each.

## Contributing

Contributions, suggestions, and issues are welcome! Please open an issue or pull request on GitHub.

## License

MIT License. See [LICENSE](LICENSE) for details.
