import json
from pymongo import MongoClient
from my_mongodb_functions import project_docs

client = MongoClient("mongodb://localhost:27017/")
db = client['my_doctors_db']
collection = db['nyu_doctors']
collection.drop()

doctor_proj = {
    'videoVisitSlots': 0, 'fgpFlag': 0, 'hasOpenScheduling': 0, 'hasRequestAnAppointmentEnabled': 0,
    'thumbImage': 0, 'squareImage': 0, 'firstAvailableApointment': 0, 'firstAvailableAppointmentAllDays': 0,
}

location_proj = {
    'schedules': 0, 'wayfindingSuite': 0, 'wayfindingFloor': 0, 'wayfindingElevator': 0,
    'isOpenSchedulingEnabled': 0, 'isRequestAppointmentEnabled': 0, 'epicDepartmentId': 0,
    'rankOrder': 0, 'epicRankOrder': 0, 'distance': 0, 'restrictedVisitTypes': 0
}

pages = [str(i) for i in range(1, 25)]
for page_nr in pages:
    with open(f'pages/doctors_page{page_nr}.json', 'r') as f_read:
        doctors = json.load(f_read)['doctors']

    doctors = project_docs(doctors, doctor_proj)
    for k, doctor in enumerate(doctors):
        doctors[k]['locations'] = project_docs(doctor['locations'], location_proj)
    
    collection.insert_many(doctors)
