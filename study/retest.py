import re

pattern = re.compile(r'hello')
result = re.match(pattern,"hellottthello")
print result.groups()