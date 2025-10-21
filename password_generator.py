import itertools
import random
import re
from datetime import datetime
from math import log2
from collections import defaultdict

# --- Password Strength Categories ---
class PasswordStrength:
    WEAK = "Weak"
    MEDIUM = "Medium"
    STRONG = "Strong"
    VERY_STRONG = "Very Strong"

def classify_password_strength(password, entropy):
    """Classify password into strength categories based on entropy and characteristics"""
    length = len(password)
    
    # Check for common weak patterns
    if (entropy < 30 or 
        length < 6 or 
        password.isdigit() or 
        password.isalpha() or 
        password.lower() in ['password', '123456', 'qwerty']):
        return PasswordStrength.WEAK
    
    # Check characteristics
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    # Count unique character types
    char_types = sum([has_upper, has_lower, has_digit, has_special])
    
    if entropy >= 60 and length >= 12 and char_types >= 3:
        return PasswordStrength.VERY_STRONG
    elif entropy >= 45 and length >= 10 and char_types >= 2:
        return PasswordStrength.STRONG
    elif entropy >= 35 and length >= 8:
        return PasswordStrength.MEDIUM
    else:
        return PasswordStrength.WEAK

def get_strength_color(strength):
    """Get color codes for strength categories"""
    colors = {
        PasswordStrength.WEAK: "\033[91m",      # Red
        PasswordStrength.MEDIUM: "\033[93m",     # Yellow
        PasswordStrength.STRONG: "\033[92m",     # Green
        PasswordStrength.VERY_STRONG: "\033[94m" # Blue
    }
    return colors.get(strength, "\033[0m")

# --- helpers --------------------------------------------------------------
def normalize_words(text):
    if not text:
        return []
    # split on non-word characters, preserve meaningful tokens
    parts = re.split(r'\W+', text)
    return [p for p in parts if p]

def leet_variants(s):
    # simple leet mapping
    mapping = {'a':'4','e':'3','i':'1','o':'0','s':'5','t':'7','l':'1'}
    variants = {s, s.lower(), s.upper(), s.capitalize()}
    # create a single leet replacement and a full replacement
    leet = ''.join(mapping.get(ch.lower(), ch) for ch in s)
    variants.add(leet)
    # partial substitutions (every possible single-letter substitution -> limited)
    for i,ch in enumerate(s):
        if ch.lower() in mapping:
            v = s[:i] + mapping[ch.lower()] + s[i+1:]
            variants.add(v)
    return variants

def date_variants(date_str):
    # Accept many date formats like "1990-01-23", "23/01/1990", "01011990", "19900123"
    if not date_str:
        return set()
    clean = re.sub(r'[^0-9]', '', date_str)
    vals = set()
    try:
        if len(clean) == 8:
            # try yyyy mm dd or dd mm yyyy
            y = clean[0:4]; m = clean[4:6]; d = clean[6:8]
            vals.update({y, y[2:], d+m+y, d+m+y[2:], d+m, m+d, d})
        elif len(clean) == 6:
            # maybe ddmmyy or yymmdd
            vals.add(clean)
        elif len(clean) >= 4:
            vals.add(clean)  # fallback
    except Exception:
        pass
    return vals

def add_symbol_variants(s):
    symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '=', '?']
    out = {s}
    # Add symbols at beginning, end, or both
    for sym in symbols:
        out.add(s + sym)
        out.add(sym + s)
        out.add(sym + s + sym)
    return out

def estimate_entropy(password):
    # rough estimator: determine character pool size then compute length*log2(pool)
    pool = 0
    if re.search(r'[a-z]', password): pool += 26
    if re.search(r'[A-Z]', password): pool += 26
    if re.search(r'[0-9]', password): pool += 10
    if re.search(r'[^A-Za-z0-9]', password): pool += 32  # rough for punctuation
    if pool == 0:
        return 0.0
    return round(len(password) * log2(pool), 1)

# --- main generator ------------------------------------------------------
def generate_passwords_by_strength(
    full_name='',
    dob='',
    fav_place='',
    fav_person='',
    important_dates=None,
    max_parts=3,
    passwords_per_category=500,  # Number per strength category
    prefer_leet=True,
    include_symbols=True
):
    important_dates = important_dates or []
    
    # tokenize ALL inputs properly
    tokens = []
    
    # Process all text fields
    all_text_fields = [full_name, fav_place, fav_person]
    for field in all_text_fields:
        if field:
            tokens.extend(normalize_words(field))
    
    # initials from full name only
    if full_name:
        name_parts = normalize_words(full_name)
        if name_parts:
            initials = ''.join(part[0] for part in name_parts)
            tokens.append(initials)
            # Also add first letter of each name part as separate tokens
            for part in name_parts:
                if len(part) > 0:
                    tokens.append(part[0])

    # add date variants from ALL date sources
    date_tokens = set()
    if dob:
        date_tokens.update(date_variants(dob))
    for d in important_dates:
        if d:
            date_tokens.update(date_variants(d))
    
    # Add date tokens as regular tokens too (for combinations)
    for dt in date_tokens:
        tokens.append(dt)
    
    # Remove duplicates and empty tokens
    tokens = [t for t in tokens if t and len(t) > 0]
    
    if not tokens:
        return defaultdict(list)
    
    # create base variants for each token
    token_variants = {}
    for t in set(tokens):
        var = set()
        var.update({t, t.lower(), t.upper(), t.capitalize()})
        if prefer_leet:
            var.update(leet_variants(t))
        token_variants[t] = list(var)[:8]  # Limit variants

    # Initialize strength categories
    strength_categories = defaultdict(list)
    
    # Generate passwords and categorize by strength
    token_list = list(token_variants.keys())
    max_combinations = passwords_per_category * 4  # Target total
    
    print(f"Generating passwords and categorizing by strength...")
    
    # Generate combinations
    combinations_generated = 0
    for r in range(1, min(max_parts, len(token_list)) + 1):
        for combo in itertools.permutations(token_list, r):
            variant_choices = [token_variants[c][:4] for c in combo]
            
            for prod in itertools.product(*variant_choices):
                core = ''.join(prod)
                
                # Generate multiple variants for this combination
                variants_to_try = [
                    core,
                    core.capitalize(),
                    core.upper(),
                    core + '123',
                    core + '2024',
                    core + '!',
                    '!' + core,
                    core + '@123',
                ]
                
                if include_symbols:
                    variants_to_try.extend(add_symbol_variants(core))
                
                # Add date combinations
                for dt in list(date_tokens)[:3]:
                    variants_to_try.extend([core + dt, dt + core])
                
                # Process each variant
                for pwd in variants_to_try:
                    if len(pwd) >= 4 and len(pwd) <= 64:
                        entropy = estimate_entropy(pwd)
                        strength = classify_password_strength(pwd, entropy)
                        
                        # Add to appropriate category if not full
                        if len(strength_categories[strength]) < passwords_per_category:
                            strength_categories[strength].append((pwd, entropy))
                        
                        combinations_generated += 1
                
                # Check if all categories are filled
                all_filled = all(len(strength_categories[cat]) >= passwords_per_category 
                               for cat in [PasswordStrength.WEAK, PasswordStrength.MEDIUM, 
                                         PasswordStrength.STRONG, PasswordStrength.VERY_STRONG])
                if all_filled or combinations_generated >= max_combinations:
                    break
                    
            if all_filled or combinations_generated >= max_combinations:
                break
                
        if all_filled or combinations_generated >= max_combinations:
            break

    # Add standalone variants to fill categories
    if not all_filled:
        # Generate simple variants to fill weak category
        while len(strength_categories[PasswordStrength.WEAK]) < passwords_per_category and tokens:
            pwd = random.choice(tokens) + str(random.randint(1, 999))
            entropy = estimate_entropy(pwd)
            strength = classify_password_strength(pwd, entropy)
            if strength == PasswordStrength.WEAK:
                strength_categories[strength].append((pwd, entropy))
        
        # Generate complex variants to fill strong categories
        while (len(strength_categories[PasswordStrength.STRONG]) < passwords_per_category or 
               len(strength_categories[PasswordStrength.VERY_STRONG]) < passwords_per_category):
            if tokens:
                pwd = (random.choice(tokens).capitalize() + 
                       random.choice(tokens).lower() + 
                       str(random.randint(10, 999)) + 
                       random.choice(['!', '@', '#']))
                entropy = estimate_entropy(pwd)
                strength = classify_password_strength(pwd, entropy)
                if (strength in [PasswordStrength.STRONG, PasswordStrength.VERY_STRONG] and 
                    len(strength_categories[strength]) < passwords_per_category):
                    strength_categories[strength].append((pwd, entropy))

    # Sort each category by entropy
    for strength in strength_categories:
        strength_categories[strength].sort(key=lambda x: x[1], reverse=True)
        # Trim to exact count
        strength_categories[strength] = strength_categories[strength][:passwords_per_category]

    return strength_categories

def get_user_input():
    """Get input from user interactively"""
    print("Password Candidate Generator - Strength-Based")
    print("=" * 55)
    print("WARNING: Using personal-info-based passwords is weak for real accounts.")
    print("Prefer long random passwords or passphrases and a password manager.")
    print()
    
    full_name = input("Enter full name: ").strip()
    dob = input("Enter date of birth (YYYY-MM-DD or any format): ").strip()
    fav_place = input("Enter favorite place: ").strip()
    fav_person = input("Enter favorite person/pet/hero: ").strip()
    
    important_dates = []
    print("\nEnter important dates (wedding, graduation, etc.)")
    print("Press Enter with empty input to finish")
    i = 1
    while True:
        date_input = input(f"Date {i}: ").strip()
        if not date_input:
            break
        important_dates.append(date_input)
        i += 1
    
    try:
        max_parts = int(input("\nMax parts to combine (1-4, default 3): ").strip() or "3")
        max_parts = max(1, min(4, max_parts))
    except ValueError:
        max_parts = 3
    
    # Ask for passwords per category
    try:
        per_category = int(input("Passwords per strength category (default 100): ").strip() or "100")
        passwords_per_category = max(10, min(10000, per_category))
    except ValueError:
        passwords_per_category = 100
    
    leet_choice = input("Use leet substitutions? (y/n, default y): ").strip().lower()
    prefer_leet = leet_choice != 'n'
    
    symbols_choice = input("Include symbols? (y/n, default y): ").strip().lower()
    include_symbols = symbols_choice != 'n'
    
    return {
        'full_name': full_name,
        'dob': dob,
        'fav_place': fav_place,
        'fav_person': fav_person,
        'important_dates': important_dates,
        'max_parts': max_parts,
        'passwords_per_category': passwords_per_category,
        'prefer_leet': prefer_leet,
        'include_symbols': include_symbols
    }

def display_results_by_strength(strength_categories, samples_per_category=10):
    """Display results organized by strength categories"""
    if not strength_categories:
        print("\nNo passwords generated. Please check your input.")
        return
    
    total_passwords = sum(len(passwords) for passwords in strength_categories.values())
    print(f"\nGenerated {total_passwords} total passwords across {len(strength_categories)} strength categories")
    print("=" * 70)
    
    # Display in order of strength
    strength_order = [PasswordStrength.VERY_STRONG, PasswordStrength.STRONG, 
                     PasswordStrength.MEDIUM, PasswordStrength.WEAK]
    
    for strength in strength_order:
        if strength in strength_categories and strength_categories[strength]:
            passwords = strength_categories[strength]
            color = get_strength_color(strength)
            reset = "\033[0m"
            
            print(f"\n{color}{strength} Passwords ({len(passwords)} total):{reset}")
            print("-" * 60)
            
            # Show samples from this category
            samples = min(samples_per_category, len(passwords))
            for i, (pwd, entropy) in enumerate(passwords[:samples], 1):
                print(f"{i:2d}. {pwd:<30} (entropy: {entropy:>5.1f} bits, length: {len(pwd):2d})")
            
            if len(passwords) > samples:
                print(f"... and {len(passwords) - samples} more {strength.lower()} passwords")

def save_results_by_strength(strength_categories, filename="passwords_by_strength.txt"):
    """Save all passwords organized by strength categories"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Password Candidates by Strength Category\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total passwords: {sum(len(passwords) for passwords in strength_categories.values())}\n\n")
            
            # Save in order of strength
            strength_order = [PasswordStrength.VERY_STRONG, PasswordStrength.STRONG, 
                            PasswordStrength.MEDIUM, PasswordStrength.WEAK]
            
            for strength in strength_order:
                if strength in strength_categories and strength_categories[strength]:
                    f.write(f"\n{strength} PASSWORDS ({len(strength_categories[strength])} total):\n")
                    f.write("-" * 40 + "\n")
                    
                    for i, (pwd, entropy) in enumerate(strength_categories[strength], 1):
                        f.write(f"{i:3d}. {pwd:<30} (entropy: {entropy:>5.1f} bits, length: {len(pwd):2d})\n")
                    f.write("\n")
        
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

# --- main program -------------------------------------------------------
if __name__ == "__main__":
    # Get user input
    user_input = get_user_input()
    
    # Generate passwords by strength
    print(f"\nGenerating {user_input['passwords_per_category']} passwords per strength category...")
    strength_categories = generate_passwords_by_strength(**user_input)
    
    # Display results
    display_results_by_strength(strength_categories, samples_per_category=15)
    
    # Option to save to file
    if any(strength_categories.values()):
        save_choice = input(f"\nSave all generated passwords to file? (y/n): ").strip().lower()
        if save_choice == 'y':
            filename = input("Enter filename (default: passwords_by_strength.txt): ").strip() or "passwords_by_strength.txt"
            if save_results_by_strength(strength_categories, filename):
                total = sum(len(passwords) for passwords in strength_categories.values())
                print(f"All {total} passwords saved to {filename} organized by strength")
    

    print("\nDone!")
