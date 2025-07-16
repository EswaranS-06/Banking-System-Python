import json
def none_check(cus, ac):
    return cus.get(ac) == None
def write(cus):
    with open('info.txt', 'w') as info:
        info.write(cus)
        
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)