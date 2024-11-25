import re

"""
^ 匹配字符串开头
    'abc': 以abc开头
    '[abc]': 以a、b、c任意一个字符开头
    '^abc': 以abc开头
    '^[abc]': 以a、b、c任意一个字符开头
    '[^abc]': 以非a、b、c的字符开头
"""

print(re.match("abc", "abc1234"))
print(re.match("abc", "11abc1234"))
print()

print(re.match("[abc]", "abc1234"))
print(re.match("[abc]", "dabc1234"))
print()

print(re.match("^abc", "abc1234"))
print(re.match("^abc", "aabc1234"))
print()

print(re.match("^[abc]", "abc1234"))
print(re.match("^[abc]", "bca1234"))
print()

print(re.match("[^abc]", "abc12345"))
print(re.match("[^abc]", "dabc12345"))
print()
