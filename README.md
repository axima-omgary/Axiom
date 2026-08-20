# Axiom

**Axiom** is a lightweight username reconnaissance tool written in Python.

It searches for a given username across multiple supported websites and reports whether the username appears to exist on each site.

The project is designed with a modular structure so that new reconnaissance modules can be added without mixing their logic together.

**Current version: Axiom 0.2v**

## Features

* Username validation
* Search for usernames across multiple websites
* Concurrent site checking using `ThreadPoolExecutor`
* Configurable number of workers
* Website definitions stored in JSON
* Modular package structure
* Command-line interface using subcommands

## Installation

### Requirements

* Python 3.10+
* pipx (recommended) or pip

### Install with pipx

Clone the repository:

```bash
git clone <repository-url>
cd Axiom
```

Install Axiom:

```bash
pipx install .
```

If Axiom is already installed and you want to reinstall the current version:

```bash
pipx install . --force
```

## Usage

### Search for a username

```bash
Axiom search-sites <username>
```

Example:

```bash
Axiom search-sites axiom
```

Axiom will validate the username and then check the supported websites concurrently.

### Change the number of workers

By default, Axiom uses 3 workers.

You can change this with:

```bash
Axiom search-sites axiom --workers 5
```

For example:

```text
Valid
Generated URLs:

GitHub --> https://github.com/axiom | Found
Reddit --> https://reddit.com/user/axiom | Not Found
...
```

The exact output depends on the websites configured in `sites.json`.

### Help

Display the available commands:

```bash
Axiom --help
```

Display help for the `search-sites` command:

```bash
Axiom search-sites --help
```

## Project Structure

```text
Axiom/
├── Axiom_pkg/
│   ├── __init__.py
│   ├── main.py
│   │
│   └── username_search/
│       ├── __init__.py
│       ├── checker.py
│       ├── validator.py
│       ├── sites.py
│       └── sites.json
│
├── README.md
└── pyproject.toml
```

### `main.py`

Provides the command-line interface and connects the available Axiom modules.

### `username_search/validator.py`

Validates usernames before performing searches.

### `username_search/checker.py`

Checks whether a generated URL responds as expected.

### `username_search/sites.py`

Loads the supported websites from `sites.json` and generates URLs for the requested username.

### `username_search/sites.json`

Contains the website definitions used by Axiom.

Keeping website definitions in JSON allows new sites to be added without changing the core search logic.

## Architecture

Axiom separates the CLI from the username-search functionality:

```text
Axiom
│
├── CLI
│   └── main.py
│
└── username_search
    ├── validator
    ├── checker
    └── sites
```

This structure makes it easier to add future modules without turning `main.py` into a large collection of unrelated functionality.

## Concurrency

Axiom uses Python's `ThreadPoolExecutor` to check multiple websites concurrently.

The default number of workers is:

```python
MAX_WORKERS = 3
```

Users can override this value from the command line:

```bash
Axiom search-sites axiom --workers 5
```

## Roadmap

* [ ] Shell autocompletion
* [ ] Improved result formatting
* [ ] Better error handling
* [ ] More supported websites
* [ ] Configurable request settings
* [ ] Result export (JSON/CSV)
* [ ] Additional reconnaissance modules
* [ ] YouTube comment-based username search
* [ ] More advanced username discovery features

## Version

Current version:

**Axiom 0.2v**

The project is actively under development, and the architecture may change as new features are introduced.

## Disclaimer

Axiom is intended for educational, research, and legitimate OSINT purposes.

Only use the tool against information and services you are authorized to investigate. Respect the terms of service, privacy expectations, and applicable laws of the websites you interact with.

## License
Axiom is released under the MIT License.
