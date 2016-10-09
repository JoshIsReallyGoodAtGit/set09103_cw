import json

jString = '{"first_name": "Josh", "last_name" : "Tait"}'

#SeeWhatIDidThere?
shoeString = '{"id" : "01", "name" : "All Stars"}'

parsed_json = json.loads(shoeString)

print(parsed_json['id'])
