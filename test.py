from lxml import etree
import lxml
import os
from os.path import join, getsize
from xml.etree.ElementTree import ElementTree
import csv

f = open('NSF_data/2014/1427987.xml')

doc = etree.parse(f)

title = doc.xpath('//AwardTitle')
effdate = doc.xpath('//AwardEffectiveDate')
expirdate = doc.xpath('//AwardExpirationDate')
amount = doc.xpath('//AwardAmount')
directorate = doc.xpath('//Organization/Directorate/LongName')
division = doc.xpath('//Organization/Division/LongName')
abstract = doc.xpath('//AbstractNarration')
awardid = doc.xpath('//AwardID')
			
# need to get all invesgigators and contact info
first = doc.xpath('//Investigator/FirstName')
last = doc.xpath('//Investigator/LastName')
#investigatorname = first[0].text + " " + last[0].text
investigatoremail = doc.xpath('//Investigator/EmailAddress')
institution = doc.xpath('//Institution/Name')

# print fullpath
print title[0].text
print effdate[0].text
print expirdate[0].text
print amount[0].text
print directorate[0].text
print division[0].text
print abstract[0].text
print awardid[0].text
print investigatoremail
print institution[0].text


peopleheaders = ['PersonID', 'FirstName', 'LastName', 'Email', 'Institution']

grantheaders = ['PersonID', 'Title', 'EffDate','ExpirDate',
				'Amount', 'Directorate', 'Division' , 'Abstract' , 'AwardID']

id = 1; #need to make unique for each person

peoplerows = [{'PersonID': investigatoremail[0].text, 'FirstName': first[0].text, 'LastName': last[0].text,
			'Email': investigatoremail[0].text, 'Institution': institution[0].text}
			]

grantrows = [{'PersonID': id, 'Title': title[0].text, 'EffDate': effdate[0].text,
			'ExpirDate': expirdate[0].text, 'Amount': amount[0].text, 'Directorate': directorate[0].text,
			'Division': division[0].text, 'Abstract': abstract[0].text, 'AwardID': awardid[0].text}
			]

#write people XML data to csv
with open('people.csv', 'w') as f:
	f_csv = csv.DictWriter(f, peopleheaders)
	f_csv.writeheader()
	f_csv.writerows(peoplerows)

#write grant XML data to csv
with open('grants.csv', 'w') as f:
	f_csv = csv.DictWriter(f, grantheaders)
	f_csv.writeheader()
	f_csv.writerows(grantrows)


"""
TABLE people
id varchar(20), 
first_name text,
last_name text,
email text,

TABLE grant
id varchar(20),
person_id ....
title text
eff_date date
expir_date date
amount int 
directorate text
division text
abstract text
awardid text

TABLE grant_for
grant_id
person_id

"""