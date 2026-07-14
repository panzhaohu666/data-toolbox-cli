# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please **do not** open a public issue.

Report it via email to the project maintainer. You can expect:

- Acknowledgment within 48 hours
- Status update within 5 business days
- Disclosure policy: coordinated disclosure after fix is released

## Scope

This tool reads local CSV/JSON files. Key security considerations:

- **Path traversal**: Ensure input file paths are validated
- **Large file DoS**: Be cautious with untrusted input files
- **Python `eval` / `exec`**: This project uses neither

## Supply Chain

- Zero third-party runtime dependencies (Python standard library only)
- Development dependencies pinned in `pyproject.toml`
