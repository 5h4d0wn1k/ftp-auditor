"""
FTP audit (lab/owned services only).
- Checks anonymous login.
- Optionally tests small provided credential list (user:pass per line).
"""

from __future__ import annotations

import argparse
import ftplib
from typing import List, Tuple


def load_creds(path: str) -> List[Tuple[str, str]]:
    creds: List[Tuple[str, str]] = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if ":" in line:
                u, p = line.strip().split(":", 1)
                if u and p:
                    creds.append((u, p))
    return creds


def main() -> None:
    parser = argparse.ArgumentParser(description="FTP audit for owned/authorized servers.")
    parser.add_argument("--host", required=True, help="FTP host (owned/authorized).")
    parser.add_argument("--port", type=int, default=21, help="FTP port (default 21).")
    parser.add_argument("--creds", help="Optional cred file user:pass per line (lab-only).")
    parser.add_argument("--timeout", type=float, default=5.0, help="Timeout seconds.")
    args = parser.parse_args()

    print("⚠️  Authorized use only. Test only servers you own/control.")

    def try_login(user: str, pwd: str) -> bool:
        try:
            with ftplib.FTP() as ftp:
                ftp.connect(args.host, args.port, timeout=args.timeout)
                ftp.login(user, pwd)
                return True
        except Exception:
            return False

    if try_login("anonymous", "anonymous@"):
        print("[+] Anonymous login allowed (remediate).")
    else:
        print("[-] Anonymous login not allowed.")

    if args.creds:
        creds = load_creds(args.creds)
        for u, p in creds:
            ok = try_login(u, p)
            print(f"[*] {u}:{p} -> {'SUCCESS' if ok else 'fail/denied'}")


if __name__ == "__main__":
    main()
