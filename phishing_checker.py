import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for the six warning signs required by the EWB workbook."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    # Add a scheme when the user enters only a hostname or URL text.
    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    # 1. An @ symbol can make the apparent destination confusing.
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    # 2. Flag URLs longer than 100 characters.
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # 3. Check whether the hostname looks like an IPv4 address.
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    # 4. Count hostname labels separated by dots.
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    # 5. Punycode hostnames contain the marker xn--.
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # 6. Plain HTTP is not encrypted.
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def has_warnings(findings):
    """Return True when at least one of the six warning signs was found."""
    information_messages = (
        "No URL entered.",
        "Could not identify a hostname.",
        "This text is not a valid URL format.",
        "No listed warning signs found.",
    )
    return any(not item.startswith(information_messages) for item in findings)


def main():
    print("=" * 52)
    print("       EWB Phishing URL Awareness Checker")
    print("=" * 52)
    print("Text checks only - this program does not open URLs.")
    print("Use sample URL strings only. Type q to quit.")

    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ").strip()

        if raw_url.lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)

        print("\nResult:")
        for item in findings:
            print("- " + item)

        if has_warnings(findings):
            warning_count = sum(
                1 for item in findings
                if not item.startswith((
                    "No URL entered.",
                    "Could not identify a hostname.",
                    "This text is not a valid URL format.",
                    "No listed warning signs found.",
                ))
            )
            print(f"\nREVIEW CAREFULLY: {warning_count} warning sign(s) found.")
        else:
            print("\nNo warning signs were identified by these checks.")

        print("Remember: no warning signs does NOT mean a URL is safe.")


if __name__ == "__main__":
    main()
