import re

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('Searching for {}'.format(pat))
        print(re.findall(pat, phrase))
        print('\n')

# repetition syntax
# * is for 0 or more
# + is for 1 or more
# ? is for 0 or 1 times
# {#,#} is for the exact number (or multiple numbers)
# x[xy]+ is for x followed by 1 or more x or y
# ^ is for exclusion
# \d is for digits
# \D is for non-digits
# \s is for whitespace
# \S is for non-whitespace
# \w is for alphanumeric
# \W is for non-alphanumeric

# test_phrase = 'sdsd..sssddd..sdddsddd..dsds..dsssss..sddddd'
# test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_phrase = 'This is a string with numbers 12343 and a symbol #hashtag'

# test_patterns = ['s[sd]+']
# test_patterns = ['[^!.?]+']
# test_patterns = ['[a-z]+'] #sequence of lowercase characters
# test_patterns = ['[A-Z]+'] #sequence of uppercase characters
# test_patterns = [r'\d+']
# test_patterns = [r'\D+']
# test_patterns = [r'\s+']
# test_patterns = [r'\S+']
test_patterns = [r'\W+']

multi_re_find(test_patterns, test_phrase)
