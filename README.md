# Password List Generator

A Python tool that generates comprehensive password lists from personal information, organized by password strength categories. **This tool is for educational, security testing, and awareness purposes only.**

## ⚠️ Important Security Warning

**This tool should only be used for:**
- Security awareness training
- Password policy testing
- Educational demonstrations
- Authorized penetration testing
- Testing your own systems

**NEVER use these generated passwords for real accounts!**
- Personal-information-based passwords are inherently weak and easily guessable
- Always prefer long, random passwords or passphrases for real accounts
- Use a reputable password manager for secure password storage

## Features

- 📋 **High-Volume Generation**: Creates extensive password lists (up to 1,000,000+ entries)
- 🔐 **Strength-Based Categorization**: Organizes passwords by strength (Weak, Medium, Strong, Very Strong)
- 📊 **Advanced Entropy Analysis**: Calculates and displays password entropy bits
- 🎨 **Color-Coded Terminal Output**: Visual strength categorization in console
- 💾 **Multiple Export Formats**: Save results to organized text files
- 🔄 **Comprehensive Input Processing**: Uses multiple personal information sources
- ⚡ **Optimized Performance**: Efficient generation for large password lists
- 🎯 **Customizable Generation**: Control list size, complexity, and patterns

## Installation

1. **Download** the Python script to your local machine

2. **Requirements**: 
   - Python 3.6 or higher
   - No external dependencies required (uses only standard library)

## Quick Start

### Basic Usage

```bash
python password_list_generator.py
```

### Advanced Usage with Parameters

```bash
# Generate large list for security testing
python password_list_generator.py --size 10000 --strength strong
```

## Usage Guide

### Interactive Mode

1. **Run the script**:
   ```bash
   python password_list_generator.py
   ```

2. **Provide personal information** (all fields optional):
   - **Full Name**: Target's full name (e.g., "John Smith")
   - **Date of Birth**: Any format (e.g., "1990-05-15", "05151990", "15/05/1990")
   - **Favorite Place**: Cities, countries, vacation spots
   - **Favorite Person**: Family members, partners, celebrities, pet names
   - **Important Dates**: Anniversaries, graduations, special events

3. **Configure list generation**:
   - **List Size**: Total passwords to generate (100 - 1,000,000)
   - **Strength Distribution**: Balance between weak/strong passwords
   - **Max Combinations**: How many information pieces to combine (1-5)
   - **Character Substitutions**: Enable leet speak (a→4, e→3, etc.)
   - **Special Characters**: Include symbols (!, @, #, $, %, etc.)

4. **Review and Export**:
   - View generated lists organized by strength
   - Save complete list to file for security testing
   - Analyze password patterns and weaknesses

### Example Session

```
Password List Generator - Security Testing Tool
=======================================================
WARNING: For authorized security testing and educational use only.

Enter target full name: Alex Johnson
Enter date of birth: 1988-12-25
Enter favorite places (comma-separated): London,Paris,Beach
Enter important people/pets (comma-separated): Emma,Max,Sophie

Enter important dates (press Enter to skip):
Date 1: 2018-06-15
Date 2: 2020-03-10
Date 3: 

Total passwords to generate (100-100000): 5000
Max combination depth (1-5): 4
Use character substitutions? (y/n): y
Include special characters? (y/n): y
Strength balance (1=Most Weak, 5=Most Strong): 3
```

## Output Examples

### Terminal Display
```
Generated Password List: 5,000 entries
======================================================================

VERY STRONG (1,250 passwords)
------------------------------------------------------------
 1. Alex!London2018@Max#     (entropy:  72.1 bits, length: 20)
 2. Johnson25Paris$Sophie    (entropy:  69.8 bits, length: 19)
 3. AJS!1988London@June      (entropy:  67.3 bits, length: 17)
...

STRONG (1,250 passwords)
------------------------------------------------------------
 1. AlexJohnson2018          (entropy:  52.4 bits, length: 14)
 2. London25Emma!            (entropy:  49.1 bits, length: 12)
 3. MaxSophie8812            (entropy:  47.8 bits, length: 11)
...

MEDIUM (1,250 passwords)
------------------------------------------------------------
 1. AlexLondon               (entropy:  41.2 bits, length: 10)
 2. Johnson2018              (entropy:  39.5 bits, length: 10)
 3. EmmaParis                (entropy:  38.1 bits, length: 9)
...

WEAK (1,250 passwords)
------------------------------------------------------------
 1. Alex123                  (entropy:  29.8 bits, length: 7)
 2. London1                  (entropy:  27.3 bits, length: 7)
 3. 881225                   (entropy:  19.9 bits, length: 6)
...
```

### File Output Structure
```
Password List Generator Results
================================
Generated: 2024-01-15 14:30:25
Target: Alex Johnson
Total Passwords: 5,000
Configuration: max_depth=4, substitutions=yes, symbols=yes

VERY STRONG PASSWORDS (1,250)
-----------------------------
1. Alex!London2018@Max#
2. Johnson25Paris$Sophie
3. AJS!1988London@June
...

STRONG PASSWORDS (1,250)
------------------------
1. AlexJohnson2018
2. London25Emma!
3. MaxSophie8812
...
```

## Password Strength Classification

### Classification Criteria

| Category | Entropy Range | Length | Character Types | Typical Use |
|----------|---------------|---------|-----------------|-------------|
| **Very Strong** | 60+ bits | 12+ | 3-4 types | Critical systems |
| **Strong** | 45-59 bits | 10+ | 2-3 types | Important accounts |
| **Medium** | 35-44 bits | 8+ | 1-2 types | Low-risk services |
| **Weak** | <35 bits | Any | Limited | **Not recommended** |

### Entropy Calculation
- **Character Pool Analysis**: Evaluates uppercase, lowercase, digits, symbols
- **Length Multiplier**: Longer passwords significantly increase entropy
- **Pattern Detection**: Identifies and penalizes common weak patterns

## Generation Methodology

### 1. Input Processing Pipeline
- **Text Tokenization**: Splits names and places into meaningful components
- **Date Extraction**: Processes multiple date formats and variations
- **Pattern Recognition**: Identifies common naming conventions
- **Variant Creation**: Generates initials, abbreviations, common mutations

### 2. Advanced Transformation Rules
- **Case Variations**: Upper, lower, title case, mixed case
- **Leet Substitutions**: Comprehensive character replacement (a→4, e→3, i→1, etc.)
- **Symbol Integration**: Strategic symbol placement (prefix, suffix, infix)
- **Date Formatting**: Multiple date representations (YYYYMMDD, DDMMYY, etc.)

### 3. Smart Combination Strategies
- **Permutation-Based**: All possible ordered combinations
- **Depth-Control**: Configurable combination complexity (1-5 levels)
- **Pattern Injection**: Common password patterns and suffixes
- **Strength Optimization**: Balances complexity and memorability

## Use Cases

### 🛡️ Security Professionals
- **Penetration Testing**: Generate targeted wordlists for authorized testing
- **Password Policy Validation**: Test organization password policies
- **Security Awareness**: Demonstrate password vulnerability to users

### 👨‍🏫 Educators & Trainers
- **Cybersecurity Courses**: Teach password security principles
- **Workshop Demonstrations**: Show how personal info creates weak passwords
- **Policy Development**: Help create effective password guidelines

### 🔍 Researchers
- **Password Analysis**: Study common password construction patterns
- **Algorithm Testing**: Test password strength meters and validators
- **Behavior Studies**: Understand how people create memorable passwords

## Customization Options

### Generation Parameters
- **List Size**: 100 to 1,000,000 passwords
- **Strength Distribution**: Control weak/strong password ratio
- **Complexity Depth**: How many information pieces to combine
- **Character Sets**: Enable/disable specific transformation rules

### Output Options
- **Strength-Based Grouping**: Organize by security levels
- **Entropy Scoring**: Include password strength metrics
- **Formatted Export**: Structured file output for tools
- **Sample Previews**: Show subsets without full generation

## Performance Optimization

### For Large Lists (>10,000 passwords)
- Use lower combination depth (2-3)
- Disable less effective transformations
- Generate in batches if memory constrained
- Use strength-focused generation

### Memory Management
- Progressive generation with yield patterns
- Efficient data structures for large sets
- Optional streaming to file for huge lists

## Integration with Security Tools

### Compatible Output Formats
- **Plain Text**: Standard wordlist format for tools like Hashcat, John the Ripper
- **Structured Text**: Organized by categories with metadata
- **CSV Format**: For analysis in spreadsheets or databases

### Typical Tool Usage
```bash
# Use with Hashcat
hashcat -m 0 hashes.txt generated_password_list.txt

# Use with John the Ripper
john --wordlist=generated_password_list.txt hashes.txt
```

## Best Practices for Usage

### ✅ Appropriate Uses
- Authorized penetration testing
- Security awareness training
- Password policy testing
- Educational demonstrations
- Personal security assessment (your own accounts only)

### ❌ Inappropriate Uses
- Unauthorized system access
- Real account password creation
- Harassment or stalking
- Any illegal activities

## Troubleshooting

### Common Issues & Solutions

**"No passwords generated"**
- Provide more diverse input information
- Increase combination depth
- Enable more transformation options

**"Memory error" with large lists**
- Reduce total list size
- Lower combination depth
- Generate in smaller batches

**"Weak passwords only"**
- Enable character substitutions and symbols
- Increase combination depth
- Provide more input data sources

## Educational Value

This tool demonstrates:
- 🔓 How attackers build targeted wordlists
- 📉 The risks of personal information in passwords
- 📈 The importance of password entropy
- 🛡️ Why password managers are essential
- ⚖️ Balance between memorability and security

## Legal & Ethical Considerations

- **Authorization Required**: Only use on systems you own or have explicit permission to test
- **Educational Purpose**: Primary use should be for learning and security improvement
- **Responsible Disclosure**: If you find vulnerabilities, follow responsible disclosure practices
- **Privacy Respect**: Never use others' personal information without consent

## Contributing

This tool can be extended with:
- Additional language support
- More sophisticated entropy algorithms
- Integration with common security tools
- Advanced pattern recognition
- Machine learning for better password generation
