

class Invigilator:
    def __init__(self, dept_id, name):
        self._dept_id = dept_id
        self._name = name
    def get_dept_id(self):return self._dept_id
    def get_name(self):return self._name

    def __str__(self): return self._name

#Available rooms for exams
ROOMS = [
    ['R1',80],['R2',100],
    ['R3',60],['R4',60],
    ['R5',60],['R6',100],
    ['R7',60],['R8',60],
    ['R9',60],['R10',60],
    ['R11',100],['R12',100],
    ['R13',100],['R13',100]
]

#Exam sessions
#Step 1 define session period(5 may - 19 May)
#Step 2 Generate session slots []
SESSIONS = [
        ['S1AM','11-04-2022','09:00 - 12:00'],
        ['S1PM','11-04-2022','14:00 - 17:00'],
        ['S2AM','12-04-2022','09:00 - 12:00'],
        ['S2PM','12-04-2022','14:00 - 17:00'],
        ['S3AM','13-04-2022','09:00 - 12:00'],
        ['S3PM','13-04-2022','14:00 - 17:00'],
        ['S4AM','14-04-2022','09:00 - 12:00'],
        ['S4PM','14-04-2022','14:00 - 17:00'],
        ['S5AM','15-04-2022','09:00 - 12:00'],
        ['S5PM','15-04-2022','14:00 - 17:00'],

        ['S6AM','18-04-2022','09:00 - 12:00'],
        ['S6PM','18-04-2022','14:00 - 17:00'],
        ['S7AM','19-04-2022','09:00 - 12:00'],
        ['S7PM','19-04-2022','14:00 - 17:00'],
        ['S8AM','20-04-2022','09:00 - 12:00'],
        ['S8PM','20-04-2022','14:00 - 17:00'],
        ['S9AM','21-04-2022','09:00 - 12:00'],
        ['S9PM','21-04-2022','14:00 - 17:00'],
        ['S10AM','22-04-2022','09:00 - 12:00'],
        ['S10PM','22-04-2022','14:00 - 17:00']
    ]

INVIGILATORS = [
        #dept id , Name , invigilator ID
        ['CS50','Mr Muwani'],
        ['CS50','Ms Katsande'],
        ['CS50','Mr R Njodzi'],
        ['CS50','Mr Muwani'],
        ['CS50','Ms GD'],
        ['CS50','Mr HD'],
        ['CS50','OH'],
        ['CS50','Mr GR'],
        ['CS50','Mr OG'],
        ['BM20','Mr SVO'],
        ['BM20','Ms GTR'],
        ['BM20','Mr SVF'],
        ['BM20','Ms GTG'],
        ['BM20','Mr SVS'],
        ['BM20','Ms GTU'],
        ['BM20','Mr SVE'],
        ['BM20','Ms GTH'],
        ['HACC45','Mrs PD'],
        ['HACC45','Mrs P Mandongwe'],
        ['HACC45','OT'],
        ['HACC45','JGH'],
        ['HACC45','KFG'],
        ['HACC45','Ms HER'],
        ['HACC45','Mr GER'],
        ['HACC45','Mr GEJ'],
        ['HACC45','Mrs HGJH'],
        ['MNG20','Ms OF'],
        ['MNG20','Mr KD'],
        ['MNG20','Mr OD'],
        ['MNG20','Mrs PS'],
        ['MNG20','Ms OS'],
        ['MNG20','Mr OGH'],
        ['MNG20','Mr PFD'],
        ['MNG20','Mrs PEG'],
        ['CHEM35','Mr PEGH'],
        
    ]

#get invigilator
def get_invigilators(invigilators,dept):
    non_dept = []
    for invigilator in invigilators:
        if not invigilator[0] ==dept:
            non_dept.append(invigilator[1])
    return non_dept

# for i in range(1,33):
#     if i < 10:
#         print('module_MNG0'+ str(i))
#     else:
#         print('module_MNG'+ str(i))
