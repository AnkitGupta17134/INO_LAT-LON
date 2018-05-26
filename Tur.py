import osmapi
api = osmapi.OsmApi()
#print (api.NodeGet(123))
print (api.NodeGet(123).get("lat"))
print (api.NodeGet(123).get("lon"))