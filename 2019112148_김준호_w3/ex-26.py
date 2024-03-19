#2019112148 김준호

import re

pattern = r'ab+'
text = 'abnormal'
case = re.match(pattern, text)

if case:
    print("Match")
else:
    print("Not Match")
