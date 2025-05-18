# Cybersecurity Tool Suite

## Overview

This project is a multi-functional cybersecurity tool designed to help security enthusiasts and professionals perform basic security assessments on networks and websites. The tool includes:

- **Port Scanner:** Scans specified IPs or domains for open ports.
- **HTTP Header Analyzer:** Checks for important security headers on websites.
- **Directory Brute Force:** Attempts to discover hidden directories on websites using a wordlist.

---

## Features

- **Multi-threaded Port Scanning** for fast network reconnaissance.
- **Security Header Analysis** to identify missing HTTP headers that help protect web applications.
- **Directory Bruteforcing** using a customizable wordlist to find hidden paths and directories.
- Interactive user input for customized scanning.

---

## Installation

1. Clone the repository:

```bash

How it works
Port Scanner
Uses multi-threading for speed.

Scans ports 1-1024 by default.

Reports all open ports found.

HTTP Header Analyzer
Sends HTTP GET requests to the target website.

Checks for important security headers like Content-Security-Policy, X-Frame-Options, and others.

Alerts if any important headers are missing.

Directory Brute Force
Reads directories from a wordlist file.

Tries to access each directory on the target website.

Reports which directories exist (HTTP 200 OK response).

Why This Project Matters
This tool helps users identify potential vulnerabilities or misconfigurations in web servers and networks, which is a crucial first step in cybersecurity assessments and penetration testing.

Future Improvements
Add scanning for more ports.

Include banner grabbing for services.

Integrate vulnerability scanning modules.

Add GUI for easier usage.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Your Name (Your GitHub Username)
Cybersecurity enthusiast | Developer
