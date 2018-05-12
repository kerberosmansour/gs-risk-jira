import json
from jira import JIRA
from config import basic_auth

options = {'server': 'https://jira.photobox.com'}
jira = JIRA(options, basic_auth=basic_auth)

vulns = jira.search_issues('project = VULN', maxResults=5)

myvulns = {"items":[{"Key":vuln.key,
				   "Summary": vuln.fields.summary,
				   "Components":[{"name":i.name}for i in vuln.fields.components]}  
				   for vuln in vulns]}

with open('vulns.json','w')as outfile:
 	json.dump(myvulns, outfile, indent=4)



projects = jira.search_issues('project = SEC and issuetype = Project or issuetype = Programme', maxResults=2000)

myprojects = {"items":[{"Key":project.key,
				   "Summary": project.fields.summary,
				   "Status": project.fields.status.name,
				   "Issuetype" : project.fields.issuetype.name,
				   "child": [{"Key":link.outwardIssue.key, "Summary": link.outwardIssue.fields.summary,"Status" : link.outwardIssue.fields.status.name, "Issuetype" : link.outwardIssue.fields.issuetype.name} for link in project.fields.issuelinks if hasattr(link,"outwardIssue")],
                   "parent": [{"Key":link.inwardIssue.key, "Summary": link.inwardIssue.fields.summary,"Status" : link.inwardIssue.fields.status.name, "Issuetype": link.inwardIssue.fields.issuetype.name} for link in project.fields.issuelinks if hasattr(link,"inwardIssue")],} 
				   for project in projects]}

with open('projects.json','w')as outfile:
 	json.dump(myprojects, outfile, indent=4)



epics = jira.search_issues('project = SEC and issuetype = Epic', maxResults=2000)


myepics = {"items":[{"Key":epic.key,
				   "Summary": epic.fields.summary} 
				   for epic in epics]}

with open('epics.json','w')as outfile:
 	json.dump(myepics, outfile, indent=4)




