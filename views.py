from app import app
from flask import render_template
import json
from collections import Counter
from data import new_data, projectData
from chartdata import *


@app.route('/')
def home():

	return render_template('home.html')

@app.route('/projects')
def projects():

	return render_template('mappings/projects.html', projectData=projectData)

@app.route('/programme')
def programme():

	return render_template('mappings/programme.html', projectData=projectData)

@app.route('/mappingOne')
def mappingOne():

	return render_template('mappings/mappingOne.html',new_data=new_data)

@app.route('/mappings')
def mappings():

	return render_template('mappings/mappings.html',new_data=new_data)

@app.route('/groupmappings')
def groupmappings():

	return render_template('mappings/groupmappings.html',new_data=new_data)

@app.route('/photoboxmappings')
def photoboxmappings():

	return render_template('mappings/photoboxmappings.html',new_data=new_data)

@app.route('/moonpigmappings')
def moonpigmappings():

	return render_template('mappings/moonpigmappings.html',new_data=new_data)

@app.route('/hofmannmappings')
def hofmannmappings():

	return render_template('mappings/hofmannmappings.html',new_data=new_data)

@app.route('/posterxxlmappings')
def posterxxlmappings():

	return render_template('mappings/posterxxlmappings.html',new_data=new_data)

@app.route('/mappingsdetail/<id>')
def mappingsdetail(id):

	for item in new_data['items']:
		for component in item['Components']:
			if component['name'] == "Level1Risk":
				if item['Key'] == (id):
					key = (item['Key'])
					summary = (item['Summary'])

	return render_template('mappings/mappingsdetail.html',new_data=new_data, key=key,summary=summary)

@app.route('/riskdetail/<id>')
def riskdetail(id):

	for item in new_data['items']:
		if item['Key'] == (id):
			key = (item['Key'])
			summary = (item['Summary'])
			rating = (item['Rating'])
			status = (item['Status'])
			owner =(item['Risk Owner'])
		for link in item['parent']:
			parentItem = link['Key']
			if link['Key'] == (item['Key']):
				newItem = (item['Key'])
				newItemSummary = (item['Summary'])
			#print('Parent Link: ' + parentItem)
		for link in item['child']:
			childItem = link['Key']
			#print('Child Link: ' + childItem)	

	return render_template('riskdetail.html',new_data=new_data,
											 key=key,  
											 rating=rating,
											 summary=summary, 
											 status=status,
											 owner=owner,
											 childItem=childItem,
											 parentItem=parentItem)


@app.route('/group')
def group():


	return render_template('group.html',new_data=new_data, 
										groupLowData=groupLowData, 
										groupMediumData=groupMediumData, 
										groupHighData=groupHighData, 
										groupCriticalData=groupCriticalData, 
										pbxtotalCount=pbxtotalCount)


@app.route('/techops')
def techops():

	techopsRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "TechOps":
					techopsRisks+=1

	techopsCount = ("TechOps: {} Risks".format(techopsRisks))
	print(techopsCount)

	return render_template('pbx_group/techops.html',new_data=new_data,
											 techopsCount=techopsCount)

@app.route('/webops')
def webops():
	webopsRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Webops":
					webopsRisks+=1

	webopsCount = ("WebOps: {} Risks".format(webopsRisks))
	print(webopsCount)

	return render_template('photobox/webops.html',new_data=new_data,
										 webopsCount=webopsCount)

@app.route('/architecture')
def architecture():

	architectureRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Architecture":
					architectureRisks+=1

	architectureCount = ("Architecture: {} Risks".format(architectureRisks))
	print(architectureCount)

	return render_template('pbx_group/architecture.html',new_data=new_data,
											 architectureCount=architectureCount)


@app.route('/prod')
def prod():
	prodRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Production-Eng":
					prodRisks+=1

	prodCount = ("Production Engineering: {} Risks".format(prodRisks))
	print(prodCount)

	return render_template('photobox/prod.html',new_data=new_data,
									   prodCount=prodCount)

@app.route('/photoscience')
def photoscience():

	photoscienceRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-imageupload":
					photoscienceRisks+=1
				

	photoscienceCount= ("Photoscience: {} Risks".format(photoscienceRisks))
	print(photoscienceCount)

	return render_template('pbx_group/photoscience.html',new_data=new_data,
											   photoscienceCount=photoscienceCount)

@app.route('/groupsecurity')
def groupsecurity():

	groupSecurityRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "Group-Security":
					groupSecurityRisks+=1
				

	groupSecurityCount= ("Group Security : {} Risks".format(groupSecurityRisks))
	print(groupSecurityCount)

	return render_template('pbx_group/groupsecurity.html',new_data=new_data,
												groupSecurityCount=groupSecurityCount)

@app.route('/businessintel')
def businessintel():

	businessintelRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Data":
					businessintelRisks+=1
				

	businessintelCount= ("Business Data and Intelligence: {} Risks".format(businessintelRisks))
	print(businessintelCount)

	return render_template('pbx_group/businessintel.html',new_data=new_data,
												businessintelCount=businessintelCount)

@app.route('/hr')
def hr():

	hrRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "Human Resources":
					hrRisks+=1
				

	hrCount= ("Human Resource: {} Risks".format(hrRisks))
	print(hrCount)

	return render_template('pbx_group/hr.html',new_data=new_data,
												hrCount=hrCount)

@app.route('/photobox')
def photobox():

	return render_template('photobox.html',new_data=new_data, 
										   photoboxLowData = photoboxLowData,photoboxMediumData=photoboxMediumData,
										   photoboxHighData=photoboxHighData,photoboxCriticalData=photoboxCriticalData)


@app.route('/babel')
def babel():
	babelRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Babel":
					babelRisks+=1

	babelCount = ("Babel & BackOffice: {} Risks".format(babelRisks))
	print(babelCount)

	babelCritical = 0

	return render_template('photobox/babel.html',new_data=new_data,
										babelCount=babelCount)


@app.route('/studio')
def studio():
	studioRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-Studio":
					studioRisks+=1

	studioCount = ("Studio: {} Risks".format(studioRisks))
	print(studioCount)

	return render_template('photobox/studio.html', new_data=new_data,
										  studioCount=studioCount)


@app.route('/shop')
def shop():
	shopRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX_shop":
					shopRisks+=1

	shopCount = ("Shop: {} Risks".format(shopRisks))
	print(shopCount)

	return render_template('photobox/shop.html',new_data=new_data,
									   shopCount=shopCount)


@app.route('/checkout')
def checkout():
	checkoutRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-checkout":
					checkoutRisks+=1

	checkoutCount = ("Supreme Checkout: {} Risks".format(checkoutRisks))
	print(checkoutCount)

	return render_template('photobox/checkout.html',new_data=new_data,
		                                   checkoutCount=checkoutCount)

@app.route('/mobile')
def mobile():
	mobileAppRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PBX-NativeApps":
					mobileAppRisks+=1

	mobileAppCount = ("Mobile App: {} Risks".format(mobileAppRisks))
	print(mobileAppCount)

	return render_template('photobox/mobile.html',new_data=new_data,
										 mobileAppCount=mobileAppCount)


@app.route('/moonpig')
def moonpig():

	return render_template('moonpig.html',new_data=new_data)

@app.route('/moonpigpci')
def moonpigpci():

	return render_template('moonpig/moonpigpci.html',new_data=new_data, vulnData=vulnData)

@app.route('/mpecommerce')
def mpecommerce():
	mpecommerceRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "mp-ecommerce":
					mpecommerceRisks+=1

	mpecommerceCount = ("Moonpig Ecommerce: {} Risks".format(mpecommerceRisks))
	print(mpecommerceCount)

	return render_template('moonpig/mpecommerce.html',new_data=new_data,
										 mpecommerceCount=mpecommerceCount)

@app.route('/mpmobile')
def mpmobile():
	mpMobileRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "MP-Mobile":
					mpMobileRisks+=1

	mpMobileCount = ("Moonpig Mobile: {} Risks".format(mpMobileRisks))
	print(mpMobileCount)

	return render_template('moonpig/mpMobile.html',new_data=new_data,
										 mpMobileCount=mpMobileCount)

@app.route('/hofmann')
def hofmann():

	return render_template('hofmann.html',new_data=new_data)

@app.route('/desktopApp')
def desktopApp():
	desktopAppRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == " hofmann-desktop":
					desktopAppRisks+=1

	desktopAppCount = ("Desktop Application: {} Risks".format(desktopAppRisks))
	print(desktopAppCount)

	return render_template('hofmann/desktopapp.html',new_data=new_data,
										 desktopAppCount=desktopAppCount)

@app.route('/webandmobile')
def webandmobile():
	webandmobileRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "hofmann-app":
					webandmobileRisks+=1

	webandmobileCount = ("Web & Mobile: {} Risks".format(webandmobileRisks))
	print(webandmobileCount)

	return render_template('hofmann/webandmobile.html',new_data=new_data,
										 webandmobileCount=webandmobileCount)

@app.route('/hfproductionEng')
def hfproductionEng():
	hfproductionEngRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "Hofmann-Prod":
					hfproductionEngRisks+=1

	hfproductionEngCount = ("Production & Engineering: {} Risks".format(hfproductionEngRisks))
	print(hfproductionEngCount)

	return render_template('hofmann/hfproductioneng.html',new_data=new_data,
										 hfproductionEngCount=hfproductionEngCount)

@app.route('/posterXXL')
def posterXXL():				

	return render_template('posterXXL.html',new_data=new_data)

@app.route('/pxlprod')
def pxlprod():
	pxlprodRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PXL-Prod":
					pxlprodRisks+=1

	pxlprodCount = ("Production & Engineering: {} Risks".format(pxlprodRisks))
	print(pxlprodCount)

	return render_template('poster/pxlprod.html',new_data=new_data,
										 pxlprodCount=pxlprodCount)

@app.route('/pxlmobileweb')
def pxlmobileweb():
	pxlmobilewebRisks = 0

	counter=Counter()
	for item in new_data['items']:
		if item['Issuetype'] =='RISK' and  item['Status'] !='Closed' and (item['Status'] != 'Fixed') and (item['Status'] != 'Not a Risk'):
			for component in item['Components']:
				if component['name'] == "PXL-WebandMobile":
					pxlmobilewebRisks+=1

	pxlmobilewebCount = ("Mobile and Web: {} Risks".format(pxlmobilewebRisks))
	print(pxlmobilewebCount)

	return render_template('poster/pxlmobileweb.html',new_data=new_data,
										 pxlmobilewebCount=pxlmobilewebCount)

@app.route('/security')
def security():

	return render_template('security.html',new_data=new_data)


@app.route('/brand')
def brand():


	return render_template('brand.html',new_data=new_data,
										groupData=groupData,
										photoboxData=photoboxData,
										moonpigData=moonpigData,
										hofmannData=hofmannData,
										posterData=posterData,
										gsData=gsData, 
										groupCount=groupCount,
										photoboxCount=photoboxCount,
										moonpigCount=moonpigCount,
										hofmannCount=hofmannCount,
										posterCount=posterCount,
										gsCount=gsCount,
										openRisks=openRisks
										)

def owners(values):
	owners = []
	seen= list()


	for value in values:
		if value not in seen:
			owners.append(value)
			seenTwo.append(value)
	return owners

@app.route('/riskowners')
def riskowners():

	for item in new_data['items']:
		values = item['Risk Owner']
		result = owners(values)
		print(result)

	return render_template('people/riskowners.html', new_data=new_data)


@app.route('/davidvale')
def davidvale():

	return render_template('people/davidvale.html',new_data=new_data)

@app.route('/iankershaw')
def iankershaw():

	return render_template('people/iankershaw.html',new_data=new_data)

@app.route('/ikdetails')
def ikdetails():

	return render_template('ikdetails.html',new_data=new_data)





