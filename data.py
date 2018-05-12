import json

f=open("risks.json", "r")
data= f.read()
new_data = json.loads(data)


r=open("projects.json", "r")
pdata= r.read()
projectData = json.loads(pdata)

v=open("vulns.json", "r")
vdata= v.read()
vulnData = json.loads(vdata)


to=open("techops.json", "r")
todata= to.read()
techopsData = json.loads(todata)



