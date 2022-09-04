from Database.views import get_data

PROGRAMS = get_data()['PROGRAMS']
MODULES = get_data()['MODULES']
SESSIONS = get_data()['SESSIONS']
ROOMS = get_data()['ROOMS']


class Module:
    def __init__(self,module_code,title,program_code,level,numOfStudents,dept_id,isMassModule, shared_programs=[]):
        self._module_code = module_code
        self._title =title
        self._program_code = program_code
        self._level = level
        self._numOfStudents = numOfStudents
        self._isMassModule = isMassModule
        self._shared_programs = shared_programs
        self._dept_id = dept_id
    
    def get_module_code(self):return self._module_code
    def get_title(self):return self._title
    def get_program_code(self):return self._program_code
    def get_level(self):return self._level
    def get_numOfStudents(self):return self._numOfStudents
    def get_isMassModule(self):return self._isMassModule
    def get_shared_programs(self):return self._shared_programs
    def get_dept_id(self):return self._dept_id

    def __str__(self):return self._module_code

class SharedPrograms:
    def __init__(self,shared_programs,shared_level):
        self._shared_programs = shared_programs
        self._shared_level = shared_level
    def get_shared_programs(self): return self._shared_programs
    def get_level(self): return self._shared_level

class Program:
    def __init__(self,program_code,program_name,modules):
        self._program_code = program_code
        self._program_name = program_name
        self._modules = modules

    def get_program_code(self):return self._program_code
    def get_program_name(self):return self._program_name
    def get_modules(self):return self._modules
    def get_level_modules(self,level):
        modules =[]
        for module in self._modules:
            if module._level ==level:
                modules.append(module)
        return modules
    #get level modules
    def get_level_1_1_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="1.1":
                modules.append(module)
        return modules
    def get_level_1_2_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="1.2":
                modules.append(module)
        return modules
    def get_level_2_1_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="2.1":
                modules.append(module)
        return modules
    def get_level_2_2_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="2.2":
                modules.append(module)
        return modules
    def get_level_3_1_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="3.1":
                modules.append(module)
        return modules
    def get_level_3_2_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="3.2":
                modules.append(module)
        return modules
    def get_level_4_1_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="4.1":
                modules.append(module)
        return modules
    def get_level_4_2_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="4.2":
                modules.append(module)
        return modules
    def get_level_5_1_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="5.1":
                modules.append(module)
        return modules
    def get_level_5_2_modules(self):
        modules =[]
        for module in self._modules:
            if module._level =="5.2":
                modules.append(module)
        return modules

class Session:
    def __init__(self,session_id,date,time):
        self._session_id = session_id
        self._date = date
        self._time = time

    def set_date(self,date):self._date =date
    def get_session_id(self):return self._session_id
    def get_date(self):return self._date
    def get_time(self):return self._time

class Room:
    def __init__(self,room_number,seating_capacity):
        self._room_number = room_number
        self._seating_capacity = seating_capacity
    
    def get_room_number(self):return self._room_number
    def get_seating_capacity(self):return self._seating_capacity
#GET all the modules
MODULE_ARRAY =[]
for program in PROGRAMS:
    for module in program.get_modules():
        SHARED = []
        if module.isMassModule:
            shared_programs = module.get_shared_programs()
            for prog in shared_programs:
                SHARED.append(SharedPrograms(prog.shared_programs.programme_code, prog.shared_level))

        MODULE_ARRAY.append(Module(module.module_code,module.title,module.programme_code,module.level,module.get_numOfStudents(),module.department_code,module.isMassModule,SHARED))

#GET PROGRAM AND PROGRAM MODULES
PROGRAMS_ARRAY = []
for program in PROGRAMS:
    PROGRAM_MODULES = []
    for module in program.get_modules():
        SHARED = []
        if module.isMassModule:
            shared_programs = module.get_shared_programs()
            for prog in shared_programs:
                SHARED.append(SharedPrograms(prog.shared_programs.programme_code, prog.shared_level))

        PROGRAM_MODULES.append(Module(module.module_code,module.title,module.programme_code,module.level,module.get_numOfStudents(),module.department_code,module.isMassModule,SHARED))

    PROGRAMS_ARRAY.append(Program(program.programme_code,program.programme_name,PROGRAM_MODULES))

SESSIONS_ARRAY = []
for session in SESSIONS:
    SESSIONS_ARRAY.append(Session(session.session_id,session.date,session.time))

ROOMS_ARRAY = []
for room in ROOMS:
    ROOMS_ARRAY.append(Room(room.room_number,room.seating_capacity))

