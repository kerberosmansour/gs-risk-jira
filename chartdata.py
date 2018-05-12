from collections import Counter
from data import new_data, projectData

# Photobox Group Data

techops = 0
groupsecurity = 0
architecture = 0
productionEng = 0
photos = 0
hr = 0



for item in new_data['items']:
	if item['Issuetype'] =='RISK' and item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] !='Not a Risk':
			for component in item['Components']:
				if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
					techops+=1					
				elif component['name'] == "Group-Security":
					groupsecurity+=1
				elif component['name'] == "PBX-Architecture":
					architecture+=1
				elif component['name'] == "PBX-Production-Eng":
					productionEng+=1
				elif component['name'] == "PBX-imageupload" or component['name']=="PBX-Data":
					photos+=1
				elif component['name'] == "Human Resources":
					hr+=1

techopsCount = ("TechOps {}".format(techops))
groupsecurityCount = ("Group Security {}".format(techops))
architectureCount = ("Architecture {}".format(techops))
productionEngCount = ("Production Engineering {}".format(techops))
photoCount = ("PhotoScience {}".format(techops))
hrCount = ("Human Resources {}".format(hr))
print(techops)
print(groupsecurity)
print(architecture)
print(productionEng)
print(photos)
print(hr)
pbxtotal = techops + groupsecurity + architecture + productionEng + photos + hr
pbxtotalCount = ("Group Total Risks {}".format(pbxtotal))
print(pbxtotalCount)




groupLowData = []
groupMediumData = []
groupHighData = []
groupCriticalData = []

counter = Counter()
for item in new_data['items']:
	if item['Rating'] == 'Critical' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		for component in item['Components']:
			if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
				counter['techopsCritical']+=1
			else:
				if component['name']=="Group-Security":
					counter['gsCritical']+=1
				elif component['name']=="PBX-Architecture":
					counter['architectureCritical']+=1
				elif component['name']=="PBX-Production-Eng" :
					counter['productionengCritical']+=1
				elif component['name']=="PBX-imageupload" or component['name']=="PBX-Data":
					counter['photosCritical']+=1
				elif component['name']=="Human Resources" :
					counter['hrCritical']+=1



for item in new_data['items']:
	if item['Rating'] == 'High' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):			
		for component in item['Components']:
			if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
				counter['techopsHigh']+=1
			else:
				if component['name']=="Group-Security":
					counter['gsHigh']+=1
				elif component['name']=="PBX-Architecture":
					counter['architectureHigh']+=1
				elif component['name']=="PBX-Production-Eng":
					counter['productionengHigh']+=1
				elif component['name']=="PBX-imageupload" or component['name']=="PBX-Data":
					counter['photosHigh']+=1
				elif component['name']=="Human Resources":
					counter['hrHigh']+=1
					

for item in new_data['items']:
	if item['Rating'] == 'Medium' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):			
		for component in item['Components']:
			if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
				counter['techopsMedium']+=1
			else:
				if component['name']=="Group-Security":
					counter['gsMedium']+=1
				elif component['name']=="PBX-Architecture":
					counter['architectureMedium']+=1
				elif component['name']=="PBX-Production-Eng":
					counter['productionengMedium']+=1
				elif component['name']=="PBX-imageupload" or component['name']=="PBX-Data":
					counter['photosMedium']+=1
				elif component['name']=="Human Resources":
					counter['hrMedium']+=1

for item in new_data['items']:
	if item['Rating'] == 'Low' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		for component in item['Components']:
			if component['name'] == "TechOps" or component['name'] == "PBX-Webops":
				counter['techopsLow']+=1
			else:
				if component['name']=="Group-Security":
					counter['gsLow']+=1
				elif component['name']=="PBX-Architecture":
					counter['architectureLow']+=1
				elif component['name']=="PBX-Production-Eng":
					counter['productionengLow']+=1
				elif component['name']=="PBX-imageupload" or component['name']=="PBX-Data":
					counter['photosLow']+=1
				elif component['name']=="Human Resources":
					counter['hrLow']+=1

groupLowData.append(counter['techopsLow'])
groupLowData.append(counter['gsLow'])
groupLowData.append(counter['architectureLow'])
groupLowData.append(counter['productionengLow'])
groupLowData.append(counter['photosLow'])
groupLowData.append(counter['hrLow'])

groupMediumData.append(counter['techopsMedium'])
groupMediumData.append(counter['gsMedium'])
groupMediumData.append(counter['architectureMedium'])
groupMediumData.append(counter['productionengMedium'])
groupMediumData.append(counter['photosMedium'])
groupMediumData.append(counter['hrMedium'])

groupHighData.append(counter['techopsHigh'])
groupHighData.append(counter['gsHigh'])
groupHighData.append(counter['architectureHigh'])
groupHighData.append(counter['productionengHigh'])
groupHighData.append(counter['photosHigh'])
groupHighData.append(counter['hrHigh'])

groupCriticalData.append(counter['techopsCritical'])
groupCriticalData.append(counter['gsCritical'])
groupCriticalData.append(counter['architectureCritical'])
groupCriticalData.append(counter['productionengCritical'])
groupCriticalData.append(counter['photosCritical'])
groupCriticalData.append(counter['hrCritical'])




photoboxLowData = []
photoboxMediumData = []
photoboxHighData = []
photoboxCriticalData = []

counter = Counter()
for item in new_data['items']:
	if item['Rating'] == 'Critical' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		for component in item['Components']:
			if component['name'] == "PBX-Babel":
				counter['BabelCritical']+=1
			else:
				if component['name']=="PBX-Studio":
					counter['studioCritical']+=1
				elif component['name']=="PBX-Shop":
					counter['shopCritical']+=1
				elif component['name']=="PBX-checkout" :
					counter['checkoutCritical']+=1
				elif component['name']=="PBX-NativeApps" :
					counter['mobileCritical']+=1



for item in new_data['items']:
	if item['Rating'] == 'High' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):			
		for component in item['Components']:
			if component['name'] == "PBX-Babel":
				counter['BabelHigh']+=1
			else:
				if component['name']=="PBX-Studio":
					counter['studioHigh']+=1
				elif component['name']=="PBX-Shop":
					counter['shopHigh']+=1
				elif component['name']=="PBX-checkout":
					counter['checkoutHigh']+=1
				elif component['name']=="PBX-NativeApps" :
					counter['mobileHigh']+=1
					

for item in new_data['items']:
	if item['Rating'] == 'Medium' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):			
		for component in item['Components']:
			if component['name'] == "PBX-Babel":
				counter['BabelMedium']+=1
			else:
				if component['name']=="PBX-Studio":
					counter['studioMedium']+=1
				elif component['name']=="PBX-Shop":
					counter['shopMedium']+=1
				elif component['name']=="PBX-checkout":
					counter['checkoutMedium']+=1
				elif component['name']=="PBX-NativeApps":
					counter['mobileMedium']+=1

for item in new_data['items']:
	if item['Rating'] == 'Low' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		for component in item['Components']:
			if component['name'] == "PBX-Babel":
				counter['BabelLow']+=1
			else:
				if component['name']=="PBX-Studio":
					counter['studioLow']+=1
				elif component['name']=="PBX-Shop":
					counter['shopLow']+=1
				elif component['name']=="PBX-checkout":
					counter['checkoutLow']+=1
				elif component['name']=="PBX-NativeApps":
					counter['mobileLow']+=1


photoboxLowData.append(counter['BabelLow'])
photoboxLowData.append(counter['studioLow'])
photoboxLowData.append(counter['shopLow'])
photoboxLowData.append(counter['checkoutLow'])
photoboxLowData.append(counter['mobileLow'])

photoboxMediumData.append(counter['BabelMedium'])
photoboxMediumData.append(counter['studioMedium'])
photoboxMediumData.append(counter['shopMedium'])
photoboxMediumData.append(counter['checkoutMedium'])
photoboxMediumData.append(counter['mobileMedium'])

photoboxHighData.append(counter['BabelHigh'])
photoboxHighData.append(counter['studioHigh'])
photoboxHighData.append(counter['shopHigh'])
photoboxHighData.append(counter['checkoutHigh'])
photoboxHighData.append(counter['mobileHigh'])

photoboxCriticalData.append(counter['BabelCritical'])
photoboxCriticalData.append(counter['studioCritical'])
photoboxCriticalData.append(counter['shopCritical'])
photoboxCriticalData.append(counter['checkoutCritical'])
photoboxCriticalData.append(counter['mobileCritical'])

######## NEEDS TO BE REFACTORED ####################
counter = Counter()
for item in new_data['items']:
	if item['Issuetype'] =='RISK' and item['Rating'] == 'Critical' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['critical_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'High' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['high_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'Medium' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['medium_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'Low' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['low_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'Info' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['info_not_fixed']+=1
	if item['Issuetype'] =='RISK' and item['Rating'] == 'To be determined' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		counter['tbd_not_fixed']+=1

totalRisks = sum(counter.values())
#print(totalRisks)

###### Risks by Brand

gsRisks = 0
groupRisks = 0
photoboxRisks = 0
moonpigRisks = 0
hofmannRisks = 0
posterRisks = 0


for item in new_data['items']:
	if item['Issuetype'] =='RISK' and item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] !='Not a Risk':
		if len(item['Components']) == 0:
			gsRisks+=1
		else:
			for component in item['Components']:
				if component['name'] == "PBX-Group-Risk":
					groupRisks+=1					
				elif component['name'] == "Photobox-Risk":
					photoboxRisks+=1
				elif component['name'] == "Moonpig-Risk":
					moonpigRisks+=1
				elif component['name'] == "Hofmann-Risk":
					hofmannRisks+=1
				elif component['name'] == "posterXXL-Risk":
					posterRisks+=1

photoboxCount = ("Photobox Risks {}".format(photoboxRisks))
groupCount = ("Group Risks {}".format(groupRisks))
moonpigCount = ("Moonpig Risks {}".format(moonpigRisks))
hofmannCount = ("Hofmann Risk {}".format(hofmannRisks))
posterCount = ("Poster Risk {}".format(posterRisks))
gsCount = ("Group Security under review {}".format(gsRisks))
openRisks = photoboxRisks + groupRisks + moonpigRisks +posterRisks + hofmannRisks

#print(openRisks)


#exceptions = totalRisks - openRisks
#print(exceptions)

groupData = []
moonpigData = []
photoboxData = []
posterData = []
hofmannData = []
gsData = []

counter = Counter()
for item in new_data['items']:
	if item['Rating'] == 'Critical' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsCritical']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupCritical']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxCritical']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigCritical']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmannCritical']+=1
				elif component['name']=="posterXXL-Risk":
					counter['posterCritical']+=1


for item in new_data['items']:
	if item['Rating'] == 'High' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsHigh']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupHigh']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxHigh']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigHigh']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmannHigh']+=1
				elif component['name']=="posterXXL-Risk":
					counter['posterHigh']+=1
					

for item in new_data['items']:
	if item['Rating'] == 'Medium' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsMedium']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupMedium']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxMedium']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigMedium']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmannMedium']+=1
				elif component['name']=="posterXXL-Risk":
					counter['posterMedium']+=1

for item in new_data['items']:
	if item['Rating'] == 'Low' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsLow']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupLow']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxLow']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigLow']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmannLow']+=1
				elif component['name']=="posterXXL-Risk":
					counter['posterLow']+=1

for item in new_data['items']:
	if item['Rating'] == 'Info' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gsinfo']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['groupinfo']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxinfo']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpiginfo']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmanninfo']+=1
				elif component['name']=="posterXXL-Risk":
					counter['posterinfo']+=1


for item in new_data['items']:
	if item['Rating'] == 'To be determined' and (item['Status'] !='Closed' and item['Status'] != 'Fixed' and item['Status'] != 'Not a Risk'):
		if len(item['Components']) ==0:
			counter['gstbd']+=1
		for component in item['Components']:
			if component['name'] == "PBX-Group-Risk":
				counter['grouptbd']+=1
			else:
				if component['name']=="Photobox-Risk":
					counter['photoboxtbd']+=1
				elif component['name']=="Moonpig-Risk":
					counter['moonpigtbd']+=1
				elif component['name']=="Hofmann-Risk":
					counter['hofmanntbd']+=1
				elif component['name']=="posterXXL-Risk":
					counter['postertbd']+=1


groupData.append(counter['groupCritical'])
groupData.append(counter['groupHigh'])
groupData.append(counter['groupMedium'])
groupData.append(counter['groupLow'])
groupData.append(counter['groupinfo'])
groupData.append(counter['grouptbd'])
#print(groupData)

photoboxData.append(counter['photoboxCritical'])
photoboxData.append(counter['photoboxHigh'])
photoboxData.append(counter['photoboxMedium'])
photoboxData.append(counter['photoboxLow'])
photoboxData.append(counter['photoboxinfo'])
photoboxData.append(counter['photoboxtbd'])
#print(photoboxData)

moonpigData.append(counter['moonpigCritical'])
moonpigData.append(counter['moonpigHigh'])
moonpigData.append(counter['moonpigMedium'])
moonpigData.append(counter['moonpigLow'])
moonpigData.append(counter['moonpiginfo'])
moonpigData.append(counter['moonpigtbd'])
#print(moonpigData)

hofmannData.append(counter['hofmannCritical'])
hofmannData.append(counter['hofmannHigh'])
hofmannData.append(counter['hofmannMedium'])
hofmannData.append(counter['hofmannLow'])
hofmannData.append(counter['hofmanninfo'])
hofmannData.append(counter['hofmanntbd'])
#print(hofmannData)

posterData.append(counter['posterCritical'])
posterData.append(counter['posterHigh'])
posterData.append(counter['posterMedium'])
posterData.append(counter['posterLow'])
posterData.append(counter['posterinfo'])
posterData.append(counter['postertbd'])
#print(posterData)

gsData.append(counter['gsCritical'])
gsData.append(counter['gsHigh'])
gsData.append(counter['gsMedium'])
gsData.append(counter['gsLow'])
gsData.append(counter['gsinfo'])
gsData.append(counter['gstbd'])
#print(gsData)
