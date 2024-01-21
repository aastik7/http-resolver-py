# HTTP Resolver

## Overview

This Python script provides a basic implementation of an HTTP resolver using raw sockets and the SSL library. The resolver is designed to retrieve content from a specified URL using low-level socket communication without relying on higher-level abstractions like the `requests` library.

## Usage

1. **Clone the Repository:**
   - Clone this repository to your local machine using the following command:
     ```
     git clone [https://github.com/aastik7/http-resolver.git](https://github.com/aastik7/http-resolver-py)
     ```

2. **Run the Script:**
   - Execute the script by providing the desired URL and, optionally, an output file name:
     ```
     python http_resolver.py https://www.example.com outputfile.txt
     ```

## Dependencies

- Python 3.x
- No external libraries beyond the standard library (uses `socket` and `ssl`).

## Important Note

This HTTP resolver is implemented at a low level, using raw sockets and SSL. It lacks the higher-level abstractions provided by libraries like `requests`. As a result, it may exhibit slower performance compared to more optimized and feature-rich solutions.

For improved ease of use, readability, and performance, consider using higher-level libraries like `requests`. This script is provided primarily for educational purposes and as a demonstration of low-level HTTP communication.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
