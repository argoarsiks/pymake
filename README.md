# pymake

`pymake` is a lightweight Python implementation of `make` for Windows.  
It allows you to define targets in a `Makefile` and run them directly from the terminal.

## Features
- Simple `Makefile` parser in Python.
- Executes shell commands bound to targets.
- Basic CLI:
  - `pymake <target>` — runs the specified target.
  - `pymake -v` or `--version` — prints version.

## Installation

### From Installer (recommended)
1. Download the latest `pymake-setup-<version>.exe` from [GitHub Releases](https://github.com/argoarsiks/pymake/releases).
2. Run the installer (may require admin rights).

## Usage

### From any directory with a Makefile:
```shell
# Run "build" target
pymake build
```

### Example Makefile:
```make
build:
	pyinstaller --onefile src/main.py --name=pymake

test:
	pytest tests
```
