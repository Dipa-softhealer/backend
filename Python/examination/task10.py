# Parse JSON and Check Keys

import json


inp = '{"name": "Alice", "age": 25}'
jsonData = ''
# can use load function to make it dictionary i guess
tmp = json.loads(inp)
# checking if there is a key named 'name' and 'age' or not
if('name' in tmp.keys() and 'age' in tmp.keys()):
    jsonData = json.dumps(tmp)
print(jsonData)