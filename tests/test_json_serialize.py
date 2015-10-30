__author__ = 'bob.zhu'
from datetime import  datetime
import json

class DateEncoder(json.JSONEncoder ):
  def default(self, obj):
    if isinstance(obj, datetime):
      return obj.__str__()
    return json.JSONEncoder.default(self, obj)

json_1 = {'num':1112, 'date':datetime.now()}
print json.dumps(json_1,cls=DateEncoder)