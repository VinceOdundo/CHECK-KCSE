# KNEC Results Checker

Yo, check out this Python app to peep your KCSE results from the KNEC portal.

## What You Need

- Python 3.6+ (keep it updated, fam)
- Internet (duh)
- Your KNEC index number and name

## How to Install

1. Clone or download this repo:

```bash
git clone https://github.com/vinceodundo/knec-results-checker.git
cd knec-results-checker
```

2. No extra stuff needed - just pure Python.

## How to Use

1. Run the script:

```bash
python check_kcse.py
```

2. Follow the prompts:
   - Type in your 11-digit index number
   - Type in your one/ full name as registered with KNEC

Example:

```
KNEC Results Checker
==================================================
Please enter the student details below:

Index Number: 12345678901
Student's Full Name: Kasongo Muss Tgoh
```

## Input Rules

- Index Number: 11 digits, no more, no less
- Student Name: Only letters and spaces
- Both fields are a must

## Error Handling

The script got you covered for:

- Invalid inputs
- Network issues
- Server errors
- Timeouts

## Privacy Note

This tool only fetches public info from KNEC. Make sure you have the right to check the results for the given index number.

## License

This project is under the MIT License - check the LICENSE file for the deets.

## Disclaimer

This tool ain't officially linked with KNEC. Use it wisely and follow KNEC's terms of service.
