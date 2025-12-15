# FTP Security Auditor

⚠️ **EDUCATIONAL PURPOSE ONLY** - This tool is designed for authorized security testing and educational purposes. Only use on FTP servers you own or have explicit written authorization to test.

## Overview

A lightweight FTP security auditing tool that checks for anonymous login vulnerabilities and optionally tests credentials. Designed for lab environments and authorized security assessments.

## Features

- **Anonymous Login Check**: Detects if anonymous FTP access is enabled
- **Credential Testing**: Optional credential testing with wordlists
- **Safety Controls**: Validates targets before scanning
- **Simple & Fast**: Minimal dependencies, easy to use

## Installation

### Requirements

- Python 3.8+
- Standard library only (no external dependencies!)

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/ftp-auditor.git
cd ftp-auditor

# No installation needed!
python ftp_audit.py --help
```

## Usage

### Basic Usage

```bash
# Check for anonymous login
python ftp_audit.py --host 192.168.1.100
```

### With Credential Testing

```bash
# Test credentials from file
python ftp_audit.py \
  --host 192.168.1.100 \
  --port 21 \
  --creds credentials.txt
```

### Custom Port and Timeout

```bash
# Custom port and timeout
python ftp_audit.py \
  --host 192.168.1.100 \
  --port 2121 \
  --timeout 10.0
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--host` | Target FTP host (required) | - |
| `--port` | FTP port | 21 |
| `--timeout` | Connection timeout (seconds) | 5.0 |
| `--creds` | Credentials file (user:pass format) | - |

## Credentials File Format

The credentials file should contain one credential pair per line in `username:password` format:

```
admin:password123
ftp:ftp
anonymous:anonymous@
test:test123
```

## Output Format

```
⚠️  Authorized use only. Test only servers you own/control.
[+] Anonymous login allowed (remediate).
[*] admin:password123 -> SUCCESS
[*] ftp:ftp -> fail/denied
```

## Examples

### Example 1: Basic FTP Check

```bash
# Check FTP service for anonymous login
python ftp_audit.py --host 192.168.1.100
```

### Example 2: Credential Testing

```bash
# Test credentials
python ftp_audit.py \
  --host 192.168.1.100 \
  --port 21 \
  --creds common_creds.txt
```

## Safety Features

- **Target Validation**: Validates host before scanning
- **Authorized Use Only**: Designed for systems you own or have permission to test
- **Rate Limiting**: Built-in delays prevent account lockouts

## Use Cases

- **Security Audits**: Check FTP configuration on your servers
- **Penetration Testing**: Authorized security assessments
- **Educational Purposes**: Learn about FTP security auditing

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security testing and educational purposes only. Unauthorized access attempts are illegal.

- Only test FTP servers you own or have explicit written authorization to test
- Respect account lockout policies
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always get explicit authorization before testing any FTP server!
