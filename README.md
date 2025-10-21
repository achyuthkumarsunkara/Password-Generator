# Password Candidate Generator

A Python tool that generates password candidates from personal information, organized by password strength categories. **This tool is for educational and security awareness purposes only.**

## ⚠️ Important Security Warning

**DO NOT use these generated passwords for real accounts!**
- Personal-information-based passwords are inherently weak and easily guessable
- Always prefer long, random passwords or passphrases
- Use a reputable password manager for secure password storage
- This tool demonstrates how attackers might generate password guesses

## Features

- 🔐 **Strength-Based Generation**: Creates passwords categorized by strength (Weak, Medium, Strong, Very Strong)
- 🎯 **Balanced Output**: Generates a specified number of passwords for each strength category
- 📊 **Entropy Estimation**: Calculates and displays password entropy bits
- 🎨 **Color-Coded Output**: Terminal display with color-coded strength categories
- 💾 **Export Capability**: Save results to organized text files
- 🔄 **Multiple Input Sources**: Uses name, birth date, favorite places, important dates, and more

## Installation

1. **Clone or download** the Python script to your local machine

2. **Requirements**: 
   - Python 3.6 or higher
   - No external dependencies required (uses only standard library)

## Usage

### Basic Run

```bash
python password_generator.py
```

### Step-by-Step Process

1. **Run the script**:
   ```bash
   python password_generator.py
   ```

2. **Provide input when prompted**:
   - **Full Name**: Your full name (e.g., "John Smith")
   - **Date of Birth**: Any format (e.g., "1990-05-15", "05151990")
   - **Favorite Place**: City, country, or special location
   - **Favorite Person**: Partner, family member, hero, or pet name
   - **Important Dates**: Wedding anniversary, graduation, etc. (press Enter to skip)

3. **Configure generation settings**:
   - **Max parts to combine**: How many information pieces to combine (1-4)
   - **Passwords per category**: Number of passwords to generate for each strength level
   - **Leet substitutions**: Whether to use character substitutions (e.g., a→4, e→3)
   - **Include symbols**: Whether to add special characters (!, @, #, etc.)

4. **View results**: The tool displays generated passwords organized by strength category

5. **Save results** (optional): Choose to export all passwords to a text file

### Example Session

```
Password Candidate Generator - Strength-Based
=======================================================
WARNING: Using personal-info-based passwords is weak for real accounts.
Prefer long random passwords or passphrases and a password manager.

Enter full name: Priya Sharma
Enter date of birth (YYYY-MM-DD or any format): 1995-06-12
Enter favorite place: Goa
Enter favorite person/pet/hero: Rohit

Enter important dates (wedding, graduation, etc.)
Press Enter with empty input to finish
Date 1: 2015-11-05
Date 2: 

Max parts to combine (1-4, default 3): 3
Passwords per strength category (default 100): 50
Use leet substitutions? (y/n, default y): y
Include symbols? (y/n, default y): y
```

## Output Example

```
Generated 200 total passwords across 4 strength categories
======================================================================

Very Strong Passwords (50 total):
------------------------------------------------------------
 1. PriyaGoaRohit@2024!    (entropy:  68.2 bits, length: 18)
 2. Sharma12Goa#Rohit      (entropy:  65.1 bits, length: 16)
 3. PGR9512!@#2024         (entropy:  62.3 bits, length: 14)
...

Strong Passwords (50 total):
------------------------------------------------------------
 1. PriyaRohit95           (entropy:  48.5 bits, length: 12)
 2. Goa2015!Priya          (entropy:  46.2 bits, length: 11)
 3. SharmaRohit11          (entropy:  45.8 bits, length: 12)
...

Medium Passwords (50 total):
------------------------------------------------------------
 1. Priya950612            (entropy:  38.1 bits, length: 10)
 2. GoaRohit               (entropy:  36.5 bits, length: 8)
 3. Sharma2015             (entropy:  35.9 bits, length: 9)
...

Weak Passwords (50 total):
------------------------------------------------------------
 1. Priya123               (entropy:  28.3 bits, length: 8)
 2. Rohit1                 (entropy:  25.1 bits, length: 6)
 3. 950612                 (entropy:  19.9 bits, length: 6)
...
```

## Password Strength Classification

The tool classifies passwords based on:

- **Entropy bits** (primary metric)
- **Length requirements**
- **Character diversity** (uppercase, lowercase, digits, symbols)
- **Common weak patterns**

### Strength Categories

| Category | Typical Characteristics | Use Case |
|----------|------------------------|----------|
| **Very Strong** | 12+ chars, 60+ bits entropy, 3+ char types | Important accounts |
| **Strong** | 10+ chars, 45+ bits entropy, 2+ char types | General accounts |
| **Medium** | 8+ chars, 35+ bits entropy | Low-risk accounts |
| **Weak** | <8 chars, low entropy, simple patterns | **Not recommended** |

## How It Works

### 1. Input Processing
- Tokenizes text inputs (names, places) into meaningful words
- Extracts date components in multiple formats
- Generates initials and common abbreviations

### 2. Variant Generation
- Case variations (upper, lower, capitalize)
- Leet speak substitutions (a→4, e→3, etc.)
- Symbol additions (beginning, end, both)
- Date format variations

### 3. Combination Strategy
- Combines 1 to N tokens (user-configurable)
- Uses permutations for order variations
- Appends common suffixes (123, 2024, etc.)
- Adds symbol variants

### 4. Strength Assessment
- Calculates character pool entropy
- Checks character type diversity
- Identifies common weak patterns
- Categorizes into strength levels

## Security Considerations

### What This Demonstrates
- How attackers generate password guesses from personal info
- Why does personal information make weak passwords
- The importance of password entropy

### Best Practices Shown
1. **Long passwords** beat complex but short ones
2. **Character diversity** significantly increases strength
3. **Avoid personal information** in passwords
4. **Use password managers** for truly random passwords

## File Output

When saving to a file, the output includes:
- Generation timestamp
- Input parameters used
- Passwords organized by strength category
- Entropy estimates and lengths for each password

## Customization

You can modify the code to:
- Adjust strength classification thresholds
- Add new character substitution rules
- Include additional symbol sets
- Change combination strategies
- Modify output formatting

## Troubleshooting

### Common Issues

1. **No passwords generated**: Check that you provided sufficient input data
2. **Memory errors**: Reduce "passwords per category" or "max parts to combine"
3. **Weak passwords only**: Enable leet substitutions and symbols for stronger variants

### Performance Notes
- Generation time increases with more input data and higher combination limits
- For large sets (>1000 per category), consider running on a machine with sufficient RAM

## Educational Value

This tool helps understand:
- Password cracking techniques
- Importance of password entropy
- Risks of using personal information
- Benefits of password managers

## License

This project is for educational purposes. Use responsibly and only on systems you own or have permission to test.

## Contributing

Feel free to fork and improve:
- Add more sophisticated entropy calculations
- Implement additional substitution rules
- Improve the strength classification algorithm
- Add support for non-English characters
