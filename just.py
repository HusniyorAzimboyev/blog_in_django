import unicodedata

char = '🫤'  # Replace 'H' with any character you want

# Get the Unicode code point in U+XXXX format
unicode_code = f"U+{ord(char):04X}"
print(f"The Unicode code point of '{char}' is {unicode_code}")
print(unicode_code)

character_name = unicodedata.name(char)
print(f"The character name of '{char}' is '{character_name}'")



unicode_code = 0x002e

symbol = chr(unicode_code)
print(f"The symbol for Unicode U+{unicode_code:04X} is '{symbol}'")