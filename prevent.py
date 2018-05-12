import json
import csv
from jira import JIRA
from config import basic_auth
from collections import Counter


options = {'server': 'https://jira.photobox.com'}
jira = JIRA(options, basic_auth=basic_auth)

prevent= jira.search_issues('project = RISK',maxResults=2000)


#preventdata_old = {"items":[{"Key":i.key,
#				"Summary": i.fields.summary,
#				"Rating":i.fields.customfield_12639.value,
#				"Links": [{"Key":link.outwardIssue.key, }for link in i.fields.issuelinks if hasattr(link,"outwardIssue")]}
#				 for i in prevent]}

preventdata = {"items":[{"Key":issue.key,
                  "Summary":issue.fields.summary,
				  "Status":issue.fields.status.name,
				  "Rating":issue.fields.customfield_12639.value,
				  "Risk Owner":issue.fields.customfield_12622.displayName}
				  for issue in prevent]}



with open('prevent.json','w') as outfile:
    json.dump(preventdata, outfile, indent=4)







