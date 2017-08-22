import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other!'

# for pattern in patterns:
#     print('I\'m searching for: {}'.format(pattern))
#
#     if re.search(pattern, text):
#         print('\tMatch found')
#     else:
# #         print('\tNo match found')
#
# match = re.search(patterns[0], text)
#
# print(type(match))
# print(match.start())
#
# split_term = '@'
# email = 'user@gmail.com'
#
# #Same as email.split('@')
#
# match = re.split(split_term, email)
# print(match)
#

print(re.findall('match', 'test phrase match in middle and match towards end'))
