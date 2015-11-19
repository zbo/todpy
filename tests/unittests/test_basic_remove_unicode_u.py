__author__ = 'bob.zhu'

raw = "{u'url': u'http://cn.bing.com/',u'text': u'buy'}"
raw = raw.replace('{', '')
raw = raw.replace('}', '')
raw = raw.replace('\'', '"')
print raw
array = raw.split(',')
# print array

temp_array=[]
for item in array:
    result = ""
    item = item.split(':')
    key = item[0][1:]
    value = item[1][1:]
    result += key+":"+value
    temp_array.append(result)
print temp_array
