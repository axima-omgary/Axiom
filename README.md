# Axiom

**Axiom** is a lightweight username reconnaissance tool inspired by projects such as [Sherlock](https://github.com/sherlock-project/sherlock).

The project is currently small by design, providing a clean and modular foundation that can be expanded with more websites, improved checking logic, better performance, and additional features over time.

> **Axiom is currently under active development.**

## Features

* 🔎 Check usernames across supported websites
* 🌐 Website definitions stored in `sites.json`
* ✅ Username validation
* 🧩 Modular Python package structure
* ⚡ Lightweight and easy to install
* 🚀 Designed to grow over time

## Project Structure

```text
Axiom/
├── Axiom_pkg/
│   ├── __init__.py
│   ├── checker.py       # Username checking logic
│   ├── main.py          # Application entry point
│   ├── sites.json       # Supported websites
│   ├── sites.py         # Website data handling
│   └── validator.py     # Username validation
│
├── README.md            # Project documentation
└── pyproject.toml       # Project configuration
```

## Installation

Axiom is designed to be installed using **pipx**, keeping the application isolated from the system Python environment.

### Install pipx

If `pipx` is not already installed:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Restart your terminal after installing `pipx`.

### Install Axiom

Clone the repository and enter the project directory:

```bash
git clone https://github.com/axima-omgary/Axiom/
cd Axiom
```

Then install Axiom with:

```bash
pipx install .
```

If Axiom is already installed and you want to reinstall the current version:

```bash
pipx install . --force
```

## Usage

After installation, run:

```bash
axiom <username>
```

For example:

```bash
axiom axiom
```

The `axiom` command is provided through the entry point configured in `pyproject.toml`.

## Configuration

Supported websites are stored in:

```text
Axiom_pkg/sites.json
```

Website-related logic is handled by:

```text
Axiom_pkg/sites.py
```

This separation makes it easier to expand the list of supported websites without changing the core structure of the application.

## Development

To work on Axiom locally:

```bash
git clone https://github.com/axima-omgary/Axiom/
cd Axiom
```

After making changes, reinstall the local package:

```bash
pipx install . --force
```

This allows you to test the current source code through the installed `axiom` command.

## Roadmap

Axiom is still in its early stages. Possible future improvements include:

* Add more supported websites
* Improve request handling
* Improve error handling
* Improve result formatting
* Add command-line options
* Add concurrent checking
* Improve username validation
* Add configurable timeouts
* Add detailed result statuses
* Improve performance
* Add automated tests
* Improve documentation

## Project Philosophy

Axiom starts small with the goal of becoming a more capable and maintainable tool over time.

The project focuses on keeping the codebase simple, modular, and understandable so that new functionality can be added without making the core unnecessarily complicated.

> **Start small. Keep it clean. Build it better.**

## Responsible Use

Axiom is intended for legitimate research, development, and educational purposes.

Only use Axiom in ways that respect website terms of service, privacy, rate limits, and applicable laws.

## Contributing

Contributions, ideas, bug reports, and improvements are welcome.

If you find a problem or have an idea for improving Axiom, feel free to open an issue or submit a pull request.

## License

Axiom is licensed under the **MIT License**.

See the `LICENSE` file for the full license text.

---

**Axiom** — a small beginning for a bigger project.
