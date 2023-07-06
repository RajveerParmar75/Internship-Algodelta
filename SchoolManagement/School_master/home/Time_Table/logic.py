from pprint import pprint

from .models import Time_table
from ..Teacher.models import Teacher
from ..Teacher.subject.models import Subject
def check_data_existence(class_name, slot, day):
    exists = Time_table.objects.filter(day=day, class_name=class_name, slot=slot).exists()
    if exists:
        return True
    else:
        return False

def slot_time(slot):
    if slot == "1":
        return "9:30"
    elif slot == '2':
        return '10:30'
    elif slot == '3':
        return '3'
    elif slot == '4':
        return '4'
    elif slot == '5':
        return '5'
    elif slot == '6':
        return '6'

def int_day(int):
    if int == 1:
        return "monday"
    elif int == 2:
        return 'tuesday'
    elif int == 3:
        return 'wednesday'
    elif int == 4:
        return 'thrusday'
    elif int == 5:
        return 'friday'
    elif int == 6:
        return 'saturday'
def teacher_formated(raw_data):
    new_data=[]
    for i in raw_data:
        new_data.append({"day":i["day"],"slot":i['slot'],"subject":i['subject'],"std":i['class_name']})
    return  (new_data)

def formate_data(raw_data):
    new_data=[{"monday":[{"1":{"subject":None,"teacher":None}},{"2":{"subject":None,"teacher":None}},{"3":{"subject":None,"teacher":None}},{"4":{"subject":None,"teacher":None}},{"5":{"subject":None,"teacher":None}},{"6":{"subject":None,"teacher":None}}]},
              {"tuesday":[{"1":{"subject":None,"teacher":None}},{"2":{"subject":None,"teacher":None}},{"3":{"subject":None,"teacher":None}},{"4":{"subject":None,"teacher":None}},{"5":{"subject":None,"teacher":None}},{"6":{"subject":None,"teacher":None}}]},
              {"wednesday":[{"1":{"subject":None,"teacher":None}},{"2":{"subject":None,"teacher":None}},{"3":{"subject":None,"teacher":None}},{"4":{"subject":None,"teacher":None}},{"5":{"subject":None,"teacher":None}},{"6":{"subject":None,"teacher":None}}]},
              {"thrusday":[{"1":{"subject":None,"teacher":None}},{"2":{"subject":None,"teacher":None}},{"3":{"subject":None,"teacher":None}},{"4":{"subject":None,"teacher":None}},{"5":{"subject":None,"teacher":None}},{"6":{"subject":None,"teacher":None}}]},
              {"friday":[{"1":{"subject":None,"teacher":None}},{"2":{"subject":None,"teacher":None}},{"3":{"subject":None,"teacher":None}},{"4":{"subject":None,"teacher":None}},{"5":{"subject":None,"teacher":None}},{"6":{"subject":None,"teacher":None}}]},
              {"saturday":[{"1":{"subject":None,"teacher":None}},{"2":{"subject":None,"teacher":None}},{"3":{"subject":None,"teacher":None}},{"4":{"subject":None,"teacher":None}},{"5":{"subject":None,"teacher":None}},{"6":{"subject":None,"teacher":None}}]}]
    for i in raw_data:
        teacher_name=Teacher.objects.get(id=i['teacher'])
        subject=Subject.objects.get(id=i['subject'])
        day=int_day(i['day'])
        if day=="monday":
            new_data[0]["monday"][i['slot']-1][str(i['slot'])]['subject'],new_data[0]["monday"][i['slot']-1][str(i['slot'])]['teacher']=subject.subject_name,teacher_name.name
        elif day=="tuesday":
            new_data[1]["tuesday"][i['slot']-1][str(i['slot'])]['subject'],new_data[1]["tuesday"][i['slot']-1][str(i['slot'])]['teacher']=subject.subject_name,teacher_name.name
        elif day=="wednesday":
            new_data[2]["wednesday"][i['slot']-1][str(i['slot'])]['subject'],new_data[2]["wednesday"][i['slot']-1][str(i['slot'])]['teacher']=subject.subject_name,teacher_name.name
        elif day=="thrusday":
            new_data[3]["thrusday"][i['slot']-1][str(i['slot'])]['subject'],new_data[3]["thrusday"][i['slot']-1][str(i['slot'])]['teacher']=subject.subject_name,teacher_name.name
        elif day=="friday":
            new_data[4]["friday"][i['slot']-1][str(i['slot'])]['subject'],new_data[4]["friday"][i['slot']-1][str(i['slot'])]['teacher']=subject.subject_name,teacher_name.name
        elif day=="saturday":
            new_data[5]["saturday"][i['slot']-1][str(i['slot'])]['subject'],new_data[5]["saturday"][i['slot']-1][str(i['slot'])]['teacher']=subject.subject_name,teacher_name.name
    return new_data