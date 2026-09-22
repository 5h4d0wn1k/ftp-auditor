> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.
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

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always get explicit authorization before testing any FTP server!
