def alternate_case_char(s):
    return ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(s)])

def alternate_case_word(s):
    return ' '.join([word.upper() if i % 2 != 0 else word.lower() for i, word in enumerate(s.split())])

# Test the functions with different sentences
print(alternate_case_char("Bing is helpful"))
print(alternate_case_word("I enjoy coding in Python"))
