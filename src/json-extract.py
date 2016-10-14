import json

with open('shoes.json', 'r') as jsonData:
	#dump the jsonData into a string
	#shoeDump = json.dumps(jsonData)

	#now load the data into a string
        with open('shoes.json', "r") as f:
		shoeName = json.load(f)
	for i in shoeName:
		if i['id'] == '01':	
			shoeID = i['id']
			shoeName = i['name']
