# statistics101-python-samples

Python Scripts for Learning Statistics 101

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This repository contains simple, Python scripts intended to help students and self-learners (like me!) practice and understand foundational concepts from a Statistics 101 course. Scripts cover topics such as descriptive statistics, probability distributions, simple hypothesis tests, sampling, visualization, and simulation. Corrections and additions are happily welcome! 

The goal is to provide clear, executable examples that demonstrate statistical concepts using Python's standard scientific libraries.

## Features

- Clear, commented example scripts for common introductory statistics topics
- Small, focused scripts suitable for running from the command line or importing into notebooks
- Examples that illustrate both theory (formulas) and practice (simulated or real data)
- Instructions for running and extending the examples

## Requirements

- Python 3.8 or newer
- Recommended libraries
  - numpy
  - scipy
  - pandas
  - matplotlib
  - seaborn
  - jupyter (optional, for notebooks)

Install the recommended packages with pip:

```bash
python -m pip install numpy scipy pandas matplotlib seaborn
```

Using a virtual environment is recommended:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

## Installation

This repository does not require a formal installation. Clone or download it and run the example scripts directly.

Clone:

```bash
git clone https://github.com/devotedbee/statistics101-python-samples.git
cd statistics101-python-samples
```

## Usage

Run a script directly:

```bash
python path/to/script.py
```

Import a script from another script or notebook:

```python
from scripts import descriptive_stats  # example
descriptive_stats.run_example()
```

Open and run notebooks:

```bash
jupyter notebook
```
or
```bash
jupyter lab
```

## Contributing

Contributions are welcome! A simple guide:

1. Fork the repository.
2. Create a branch for your feature or fix:
   ```bash
   git checkout -b feature/my-new-script
   ```
3. Add or update scripts, tests, and documentation.
4. Commit and push your branch:
   ```bash
   git commit -am "Add [short description]"
   git push origin feature/my-new-script
   ```
5. Open a pull request with a clear description of changes.

Guidelines:
- Keep scripts small and focused on a single concept.
- Add comments and a short header describing the purpose, inputs, and outputs.
- Include sample input data (or a generator) when appropriate.


## License

This repository is available under the MIT License.

Copyright (c) 2025 cw

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
- The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.
- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.

## Contact

If you have questions or suggestions, open an issue or pull request on the repository:
https://github.com/devotedbee/statistics101-python-samples
