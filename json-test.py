import json

jString = '{"first_name": "Josh", "last_name" : "Tait"}'

parsed_json = json.loads(jString)

print(parsed_json['first_name'])
