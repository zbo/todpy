__author__ = 'bob.zhu'
import base64
base1 = '/Users/bob.zhu/project/todpy/libraries/web/action/features/web_browser.py'
base2 = "I click element with class '([^']*)'"

text = base1 + '|' + base2
base64_text = base64.b64encode(text)
print base64_text
original_text = base64.b64decode(base64_text)
print original_text