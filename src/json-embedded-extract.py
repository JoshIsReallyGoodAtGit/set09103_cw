import json

#with open('shoes.json') as jsonData:

jsonData = {"id": "01", "testElement": "TestElementData"}

	#if I'm getting an error that has 'buffer' in it, check im using
	#json.load instead of json.loads
	#ooh, also, json objects need to be 'dumped' first, using json.dump(json	#Data)
shoeDump = json.dumps(jsonData)
	#now load the data into a string
shoeName = json.loads(shoeDump)
	
print shoeName['id']

