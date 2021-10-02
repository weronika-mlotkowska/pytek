import json


f = open('data\example_questions.json', "r")
data = json.loads(f.read())

print(data)
