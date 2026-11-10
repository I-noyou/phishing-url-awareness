# EWB Phishing URL Awareness Checker

## Overview

Phishing is a trick in which fake links or messages try to make people
share passwords, OTPs, or payment details. This beginner-friendly Python
program checks the text of a URL for six selected warning signs. It does
not visit the URL or send information anywhere.

## Features

-   Detects an `@` symbol in the URL.
-   Flags unusually long URLs (over 100 characters).
-   Flags IP-address hostnames.
-   Flags hostnames with five or more segments.
-   Flags punycode-style hostnames containing `xn--`.
-   Flags the HTTP scheme.
-   Repeats checks until the user enters `q`, `quit`, or `exit`.
-   Handles malformed URL input without stopping unexpectedly.
-   Displays a cautious review message when warning signs are found.

## Requirements

-   Python 3.10 or later.
-   No extra Python packages are required.

## Project Structure

``` text
phishing-url-awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── tests/
│   └── test_samples.md
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

Capture both screenshot files on your own computer after running the
program and completing the tests.

## How to Run

### Windows

Check your Python version:

``` bash
python --version
```

Run the program:

``` bash
python phishing_checker.py
```

If `python` is not recognised, try:

``` bash
py phishing_checker.py
```

### macOS / Linux

Check your Python version:

``` bash
python3 --version
```

Run the program:

``` bash
python3 phishing_checker.py
```

Enter a sample URL when prompted. Enter `q` to quit.

## Example Output

``` text
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.
Use sample URL strings only. Type q to quit.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Remember: no warning signs does NOT mean a URL is safe.
```

## Testing

The five required sample test cases from the EWB workbook were run.
Based on the terminal results shared during project development, all
five produced the expected observations.

  -----------------------------------------------------------------------------------------------------
  \#                Sample test                                 Expected observation  Result
  ----------------- ------------------------------------------- --------------------- -----------------
  1                 `https://www.example.com/login`             No listed warning     PASS
                                                                signs; this is not a  
                                                                safety guarantee      

  2                 `http://192.0.2.10/account`                 IP-address hostname   PASS
                                                                and HTTP warnings     

  3                 `http://example.com@sample.invalid/login`   `@` symbol and HTTP   PASS
                                                                warnings              

  4                 `https://a.b.c.d.e.example.invalid/path`    Many hostname         PASS
                                                                segments/subdomains   
                                                                warning               

  5                 `https://xn--example.invalid/`              Punycode-style        PASS
                                                                hostname warning      
  -----------------------------------------------------------------------------------------------------

Detailed evidence is recorded in
[`tests/test_samples.md`](tests/test_samples.md). Before final
submission, record the actual Python version, operating system, and test
date in that file.

## Screenshots

### Sample Program Run

![Sample program run](screenshots/sample_run.png)

### Test Results

![Test results](screenshots/test_results.png)

These images will display on GitHub after `sample_run.png` and
`test_results.png` have been saved in the `screenshots` folder.

## Improvements

1.  **Repeat checks with a quit command:** users can inspect several
    sample URL strings without restarting the program.
2.  **Malformed URL handling:** invalid URL formats are reported clearly
    rather than causing the program to stop unexpectedly.
3.  **Review summary:** the program displays a `REVIEW CAREFULLY`
    message and the number of warning signs found when warning signs are
    detected.

## Limitations

This is an educational awareness tool. It only reads URL text. It does
not visit URLs, scan for malware, query reputation services, or prove
that a URL is safe. "No listed warning signs found" does **NOT** mean a
URL is safe. Some legitimate URLs may also contain one or more warning
signs.

## Ethical Use

-   Use the sample strings supplied in the EWB workbook.
-   Do not collect passwords, OTPs, or other credentials.
-   Do not send phishing messages.
-   Do not scan or probe websites or networks without written
    authorisation.
-   Do not upload passwords, API keys, or confidential data to GitHub.

## Author

**Lokesh Kumar Sahu**\
EWB Cybersecurity Internship Mini Project
