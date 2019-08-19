import requests
import urllib3
import json

import datetime
baseURI = 'https://onewiki/'
resource = 'rest/calendar-services/1.0/calendar/events.json?subCalendarId=9fb047a8-f0d2-49ff-a01c-c64824da939f'
headers = { "content-type" : "application/json" }
data = {"subCalendarId":'9fb047a8-f0d2-49ff-a01c-c64824da939f'} #,
        #"eventType":'Events', 
        #"what":'Fridays Meeting', 
        #"person": ['userkey (can find using http://localhost:8090/rest/api/user?username=someusername)'],
        #"startDate": '06-Jun-2019',
        #"startTime": '10:00',
        #"endDate": '06-Jun-2019',
        #"endTime": '11:00',
        #"allDayEvent": "false"}
        #"where": 'Blue Room'}

#response = requests.put(baseURI + resource, headers=headers, auth=('user', 'password'), data=data, timeout=15)
response = requests.get(baseURI + resource, headers=headers, data=data, timeout=15, verify=False)
print('\n\n\n')
print(response)
print(response.text)
