<div align="center">

# 🔐 Password Strength Checker

**A lightweight command-line utility for evaluating password composition and highlighting practical improvements.**

<p>
  <img src="https://img.shields.io/badge/Language-Python%203.x-3776AB?logo=python&logoColor=white" alt="Python 3.x" />
  <img src="https://img.shields.io/badge/Interface-CLI-24292F?logo=windows-terminal&logoColor=white" alt="Command-line interface" />
  <img src="https://img.shields.io/badge/Dependencies-None-2EA44F" alt="No third-party dependencies" />
  <img src="https://img.shields.io/badge/License-Not%20specified-lightgrey" alt="License not specified" />
</p>

</div>

---

## Overview

**Password Strength Checker** is an interactive Python CLI that scores a password against five basic composition criteria and explains which requirements are missing. It offers immediate, readable feedback in the terminal, helping users identify simple improvements without installing third-party packages.

---

## ✨ Key Features

- 🧮 **Five-point scoring** — evaluates length, uppercase letters, lowercase letters, digits, and symbols.
- 🧭 **Actionable feedback** — identifies the specific criteria a password does not meet.
- 🔁 **Interactive retry loop** — lets users try again after a weak or medium result.
- ✅ **Clear completion condition** — exits when all five checks pass.
- ⚡ **Zero dependency setup** — runs with Python and its standard library.
- 🖥️ **Simple terminal interface** — no browser, account, or configuration required.

---

## 🧰 Tech Stack & Architecture

| Component | Implementation | Purpose |
|---|---|---|
| Language | Python 3.x | Application logic and terminal interaction |
| Input / output | `input()` and `print()` | Collect a password and display the result |
| Character checks | Built-in string methods | Detect uppercase, lowercase, and numeric characters |
| Dependencies | Python standard library | No third-party packages required |

### How It Works

1. **Accept input** — prompt the user to enter a password.
2. **Inspect the characters** — determine whether the password contains uppercase letters, lowercase letters, digits, and symbols.
3. **Apply the length rule** — award a point if the password is at least eight characters long.
4. **Calculate the score** — award one point for each of the five criteria.
5. **Report and repeat** — classify the result as *Weak* (0–2), *Medium* (3–4), or *Strong* (5). The program exits on a strong result and prompts again otherwise.

### Scoring Rules

| Criterion | Points | Requirement |
|---|:---:|---|
| Length | 1 | At least 8 characters |
| Uppercase | 1 | Contains an uppercase letter |
| Lowercase | 1 | Contains a lowercase letter |
| Number | 1 | Contains a digit |
| Symbol | 1 | Contains a character that is not an uppercase letter, lowercase letter, or digit |
| **Maximum** | **5** | **All criteria satisfied** |

> **Scoring note:** This is a rule-based composition check, not a measurement of real-world password security. It does not check password reuse, known breaches, common-password lists, or estimated cracking time.

---

## 🚀 Quick Start

### Prerequisites

- Python 3 installed on your system.
- The project script saved as `password_strength_checker.py`.

No package installation or virtual environment is required for the current implementation.

### 1. Get the project files

Clone the repository and move into its directory. Replace the placeholders with your GitHub username and repository name:

```bash
git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>.git
cd <YOUR-REPOSITORY>
```

Alternatively, save the Python script as `password_strength_checker.py` in a local folder and open a terminal in that folder.

### 2. Verify Python

```bash
python --version
```

On Windows, `py --version` may be available if the `python` command is not configured.

### 3. Run the checker

```bash
python password_strength_checker.py
```

On Windows, you can also run:

```powershell
py password_strength_checker.py
```

### Example Session

```text
Welcome to the Password Strength Checker!
Enter a password to check: example123

--- Results ---
Medium password. It's okay, but could be better.
- Missing an uppercase letter.
- Missing a symbol (like !, @, #, $).
Welcome to the Password Strength Checker!
Enter a password to check: Str0ng!Pass

--- Results ---
Strong password! Excellent.
```

The example uses fictional values for illustration. The program returns to the prompt after a weak or medium result and exits after a strong result.

---

## 🖼️ Visual Proof

The terminal session above demonstrates the expected interaction. To add a screenshot or GIF of an actual run, save it to `docs/images/password-checker-demo.png` and replace this placeholder with:

```markdown
![Password Strength Checker terminal demo](docs/images/password-checker-demo.png)
```

> Capture only fictional test passwords in screenshots. Do not publish personal or production credentials.

---

## ⚠️ Current Scope & Limitations

- The result is based on five composition rules; it is not a definitive measure of password strength.
- A character that is neither uppercase, lowercase, nor numeric is treated as a symbol by the current logic. This can include whitespace.
- Password input uses Python's `input()`, so typed characters are visible in the terminal. Avoid entering real credentials into this version until hidden input is implemented.
- The script does not store passwords to a file or transmit them over a network, but terminal visibility and the surrounding environment still matter.
- The current source imports `re` and `string`, but does not use them; these imports can be removed without changing the present behavior.

---

## 🛡️ Ethical Use

> [!WARNING]
> Use this utility only to assess passwords you own or are explicitly authorized to test. Do not use it as a substitute for a reputable password manager, multi-factor authentication, or an organization's approved password-auditing process. Never share or commit real passwords, screenshots of real credentials, or other sensitive authentication data.

---

## 📄 License

No license has been specified yet. Until a license is added to the repository, others should not assume they have permission to redistribute or modify the project. Consider adding a `LICENSE` file before publishing it as open source.
