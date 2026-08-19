# Offensive-Security-NTLMv2_to_hashcat_format

A simple Python tool to convert NTLMv2 challenge/response data into Hashcat-compatible format for password cracking.

## 🎯 Purpose

This tool is designed for cybersecurity professionals and pentesters who need to quickly convert NTLMv2 authentication data into the format required by Hashcat (mode 5600). It's particularly useful during:
- Active Directory security assessments
- Penetration testing engagements
- CTF (Capture The Flag) competitions
- Cybersecurity research and education

## ✨ Features

- **Interactive Input**: User-friendly prompt-based data collection
- **Input Methods**: Enter fields individually
- **Input Validation**: Basic hex format validation to prevent errors
- **File Export**: Save formatted output directly to a .txt file
- **Clipboard Support**: Copy results to clipboard (requires `pyperclip`)
- **Educational Friendly**: Clear prompts with examples

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (optional: `pyperclip` for clipboard support)

### Clone the Repository
```bash
git clone https://github.com/mbaso61/ntlmv2-hashcat-converter.git
cd ntlmv2-hashcat-converter
