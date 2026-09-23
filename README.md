> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# FTP Security Auditor

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/5h4d0wn1k/ftp-auditor)
![Last commit](https://img.shields.io/github/last-commit/5h4d0wn1k/ftp-auditor)
![GitHub issues](https://img.shields.io/github/issues/5h4d0wn1k/ftp-auditor)

Lightweight **FTP security auditing** tool — detects anonymous-login exposure and optionally tests credentials (user:pass wordlists) against servers you own or hold explicit authorization to assess.

## Why

Legacy FTP servers still expose anonymous login and weak credentials across internal networks and edge devices. This tool performs a focused **FTP misconfiguration audit**: it validates the target before scanning, checks whether anonymous access is enabled, and optionally tests a wordlist of credentials for lab assessment — with built-in delays to prevent account lockouts. Designed strictly for **authorized security testing and education**, it keeps the dependency surface small (Python standard library only) so it ships anywhere and never surprises you with extra tooling.

## Features

- **Anonymous Login Check** — detects open anonymous FTP access.
- **Credential Testing** — optional `user:pass` wordlist testing with lockout-safe rate limiting.
- **Target Validation** — validates host before scanning.
- **Custom Port & Timeout** — `--port`, `--timeout` for non-standard services.
- **Minimal dependencies** — Python 3.8+, standard library only.

## Quickstart

```bash
# Basic anonymous-login check
python ftp_audit.py --host 192.168.1.100

# Credential testing (lab-only)
python ftp_audit.py --host 192.168.1.100 --port 21 --creds credentials.txt

# Custom port and timeout
python ftp_audit.py --host 192.168.1.100 --port 2121 --timeout 10.0
```

Credentials file — one `username:password` pair per line:

```
admin:password123
ftp:ftp
anonymous:anonymous@
```

## Project structure

```
ftp-auditor/
├── ftp_audit.py        # main CLI (stdlib only)
├── VERSION, CHANGELOG.md
└── ETHICS.md, SCOPE.md # authorized-use rules
```

## Documentation

- [ETHICS.md](ETHICS.md) — authorized-use policy
- [SCOPE.md](SCOPE.md) — assessment scope
- [SECURITY.md](SECURITY.md) — security policy
- [CONTRIBUTING.md](CONTRIBUTING.md) — contribution guide

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Test only FTP servers you own or have written authorization for.

## License

MIT. See [LICENSE](LICENSE).