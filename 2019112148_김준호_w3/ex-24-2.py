#2019112148 김준호

import re

pattern = r'ab+'

input_string = 'abnormal'

match = re.match(pattern, input_string)

if match:
    print("String 'abnormal' matches the pattern.")
else:
    print("String 'abnormal' does not match the pattern.")
