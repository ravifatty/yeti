import pyeti, json    # json is only used for pretty printing in the examples below 
api = pyeti.YetiApi("http://192.168.66.137:5000/api/", verify_ssl=False)
#result = api.observable_search(value="applicationzip", regex=True)
#print(json.dumps(result, indent=4, sort_keys=True)
tag = "lokibot"
#api.observable_add([tag])
results = api.observable_search(tags=tag)
#results = api.observable_search(value="myplatonca.com", regex=True)
print(results)

