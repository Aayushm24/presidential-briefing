#!/usr/bin/env python3
"""Send an email via Gmail SMTP with an App Password.

Much simpler than OAuth for a cron job that sends one email a day.

Usage:
    python3 scripts/send_gmail.py <to> <subject> <body>
    python3 scripts/send_gmail.py <to> <subject> - < body.txt   # body from stdin

Required env:
    GMAIL_APP_PASSWORD   — 16-char App Password from https://myaccount.google.com/apppasswords
    GMAIL_FROM_ADDRESS   — The Gmail address that sends the email
"""

import os
import smtplib
import sys
from email.message import EmailMessage


def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: send_gmail.py <to> <subject> <body|->", file=sys.stderr)
        sys.exit(2)

    to = sys.argv[1]
    subject = sys.argv[2]
    body_arg = sys.argv[3]

    body = sys.stdin.read() if body_arg == "-" else body_arg

    password = os.environ.get("GMAIL_APP_PASSWORD")
    sender = os.environ.get("GMAIL_FROM_ADDRESS")

    if not password:
        print("[send_gmail] GMAIL_APP_PASSWORD not set", file=sys.stderr)
        sys.exit(1)
    if not sender:
        print("[send_gmail] GMAIL_FROM_ADDRESS not set", file=sys.stderr)
        sys.exit(1)

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
    except smtplib.SMTPAuthenticationError as e:
        print(f"[send_gmail] authentication failed: {e}", file=sys.stderr)
        print(
            "[send_gmail] Verify GMAIL_APP_PASSWORD is a 16-character App Password, not your account password.",
            file=sys.stderr,
        )
        print(
            "[send_gmail] Generate one at https://myaccount.google.com/apppasswords",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(f"[send_gmail] send failed: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"[send_gmail] sent to {to}")


if __name__ == "__main__":
    main()
