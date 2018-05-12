import json
from jira import JIRA
from config import basic_auth
from collections import Counter

options = {'server': 'https://jira.photobox.com'}
jira = JIRA(options, basic_auth=basic_auth)


issues = jira.search_issues('project = RISK',maxResults=2000)

mydata = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,

				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value,
				  "Risk Description": issue.fields.customfield_12621,
				  "Risk Owner":issue.fields.customfield_12622.displayName,
				  "Issuetype": issue.fields.issuetype.name,
                  "child": [{"Key":link.outwardIssue.key, "Summary": link.outwardIssue.fields.summary,"Status" : link.outwardIssue.fields.status.name,"Issuetype" : link.outwardIssue.fields.issuetype.name} for link in issue.fields.issuelinks if hasattr(link,"outwardIssue")],
                  "parent": [{"Key":link.inwardIssue.key, "Summary": link.inwardIssue.fields.summary,"Status" : link.inwardIssue.fields.status.name,"Issuetype" : link.inwardIssue.fields.issuetype.name} for link in issue.fields.issuelinks if hasattr(link,"inwardIssue")],
				  "Components":[{"name":i.name}for i in issue.fields.components]} 
				  for issue in issues]}



with open('risks.json','w') as outfile:
    json.dump(mydata, outfile, indent=4)




