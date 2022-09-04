'''
Examination Scheduling algorithm is an
algorithm that will be used to schedule
MSUAS exam timetable

----User inputs-----
1. Sessions
2. Invigilators
3. rooms
4. 

'''
#random is the library that will be used
# to assign sessions to slots randomly

#prettytable is an imported library that was used 
# to display data in a table like format in console
import random as rnd
from .prettytable import PrettyTable

#Import data from the database
from Database.views import get_data

INVIGILATORS = get_data()['INVIGILATORS']
from Database.datastructures import *

# get data converted from database to arrays
PROGRAMS = PROGRAMS_ARRAY
MODULES = MODULE_ARRAY
SESSIONS = SESSIONS_ARRAY
ROOMS = ROOMS_ARRAY


#Population size defines number of cycles on each generation
POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES =1
TOURNAMENT_SELECTION_SIZE =3
MUTATION_RATE =0.05

'''
Class Population takes population size as input
and data from data class
then generate schedules based on the length of population size
Finally it return generated schedules using function
get_schedules()
'''
class Population:
    def __init__(self,size):
        self._size = size
        self._data = dataset
        self._schedules = []
        for i in range(0,size): self._schedules.append(Schedule().initialize())
    def get_schedules(self):return self._schedules

'''
It takes ROOMS,INVIGILATORS,SESSIONS,MODULES AND PROGRAMS
It assigns modules to their programs
and find the number of modules on each program 
'''
class Data:
    #sample data
    ROOMS = ROOMS
    SESSIONS = SESSIONS
    INVIGILATORS = INVIGILATORS

    def __init__(self):
        self._rooms =[] 
        self._sessions = [] 
        self._invigilators = []
        #Adding rooms 
        for i in range(0,len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i].get_room_number(),self.ROOMS[i].get_seating_capacity()))
        
        for i in range(0, len(self.SESSIONS)):
            self._sessions.append(Session(self.SESSIONS[i].get_session_id(),self.SESSIONS[i].get_date(),self.SESSIONS[i].get_time()))
        
        #initialising Invigilators
        for i in range(0,len(self.INVIGILATORS)):
            self._invigilators.append(Invigilator(self.INVIGILATORS[i].get_dept_id(),self.INVIGILATORS[i].get_name()))

        self._modules = MODULES
        self._programs = PROGRAMS
        self._numberOfModules = 0

        for i in range(0,len(self._programs)):
            self._numberOfModules += len(self._programs[i].get_modules())

    def get_rooms(self):return self._rooms
    def get_modules(self):return self._modules
    def get_programs(self):return self._programs
    def get_sessions(self):return self._sessions
    def get_invigilators(self):return self._invigilators
    def get_numberOfModules(self):return self._numberOfModules

#Invigilator class
class Invigilator:
    def __init__(self, dept_id, name):
        self._dept_id = dept_id
        self._name = name
    def get_dept_id(self):return self._dept_id
    def get_name(self):return self._name

    def __str__(self): return self._name

'''
Class Session stores the session id, date of exam and time
'''
class Session:
    def __init__(self,session_id,date,time):
        self._session_id = session_id
        self._date = date
        self._time = time

    def set_date(self,date):self._date =date
    def get_session_id(self):return self._session_id
    def get_date(self):return self._date
    def get_time(self):return self._time
    def __str__(self): return str((self._date + " " + self._time))

'''
class room stores the room numbe and seating capacity
of the room 
'''
class Room:
    def __init__(self,room_number,seating_capacity):
        self._room_number = room_number
        self._seating_capacity = seating_capacity
    
    def get_room_number(self):return self._room_number
    def get_seating_capacity(self):return self._seating_capacity

'''
class Slot is used to assign different modules
to different time slots
it takes in slot ID, program and modules
'''
class Slot:
    def __init__(self,slot_id,program,modules):
        self._slot_id = slot_id
        self._programs = program
        self._modules = modules
        self._session = None
        self._room = None
        self._invigilator = None
    
    def get_slot_id(self):return self._slot_id
    def get_programs(self):return self._programs
    def get_modules(self):return self._modules
    def get_session(self):return self._session
    def get_room(self):return self._room
    def get_invigilator(self):return self._invigilator
    def set_session(self,session):self._session = session
    def set_room(self,room):self._room = room
    def set_invigilator(self,invigilator):self._room = invigilator


    def __str__(self):
        return str(self._room.get_room_number()) + "," + str(self._session.get_session_id())

# initialise the data object
dataset = Data()

'''
class schedule used to initialise data using the
initialise function

it returns number of conflicts 
after checking constraints defined

'''
class Schedule:
    def __init__(self):
        self._data = dataset
        self._slots = []
        self._numOfConflicts =0
        self._fitness = -1
        self._slotNumb =0
        self._isFitnessChanged = True
        self.rooms_status = {}
    def get_slots(self):
        self._isFitnessChanged = True 
        return self._slots
    def get_numbOfConflicts(self):return self._numOfConflicts
    
    def get_fitness(self):
        if(self._isFitnessChanged ==True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
            return self._fitness
    #return initialised data
    def initialize(self):
        #return a list of programs
        time_slots =[
                    [0,1],[2,3],[4,5],[6,7],[8,9],[10,11],[12,13],[14,15],[16,17],[18,19],[20,21],[22,23],
                    [24,25],[26,27],[28,29],[30,31],[32,33],[34,35],[36,37],[38,39],[40,41],[42,43],[44,45]
                ]
        programs = self._data.get_programs()
        for i in range(0,len(programs)):
            modules = programs[i].get_modules() #return a list of modules per program
            grouped_modules =[
                programs[i].get_level_1_1_modules(),
                programs[i].get_level_1_2_modules(),
                programs[i].get_level_2_1_modules(),
                programs[i].get_level_2_2_modules(),
                programs[i].get_level_3_1_modules(),
                programs[i].get_level_3_2_modules(),
                programs[i].get_level_4_1_modules(),
                programs[i].get_level_4_2_modules(),
                programs[i].get_level_5_1_modules(),
                programs[i].get_level_5_2_modules()
            ]

            for level in grouped_modules:
                session_num =0
                session_length = len(SESSIONS)//2
                # print("======session length" + str(session_length)+ "=======")
                for j in range(0,len(level)):
                    if((session_length - session_num) == 1):
                        session_num = rnd.randrange(0,session_length-1)
                    else:
                        pass
                        # print("======session number" + str(session_num)+ "=======")
 
                    newSlot = Slot(self._slotNumb,programs[i],level[j])
                    
                    self._slotNumb+=1
                    newSlot.set_session(dataset.get_sessions()[rnd.choice(time_slots[session_num])])
                    room_number = rnd.randrange(0,len(dataset.get_rooms()))
                    newSlot.set_room(dataset.get_rooms()[room_number])
                    self._slots.append(newSlot)
                    # students = level[j].get_numOfStudents()
                    # if dataset.get_rooms()[room_number].get_room_number() in self.rooms_status:
                    #     self.rooms_status[dataset.get_rooms()[room_number].get_room_number()]+= students
                    #     print('Incremented...........')
                    # self.rooms_status[dataset.get_rooms()[room_number].get_room_number()]= students
                    session_num +=1

            grouped_modules=[]
        return self

    def calculate_fitness(self):
        self._numOfConflicts =0
        slots = self.get_slots()
        #Check if number of students allocated to the venue are no exceeding venue capacity
        for i in range(0,len(slots)):
            if(slots[i].get_room().get_seating_capacity() < slots[i].get_modules().get_numOfStudents()):
                self._numOfConflicts+=1
                
            for j in range(0,len(slots)):
                if(j >i):
                    #check if two modules of the same student are not written in the same day
                    if((j-i)==1):
                        if(slots[i].get_modules().get_program_code() ==slots[j].get_modules().get_program_code()): 
                            if(slots[i].get_modules().get_level() ==slots[j].get_modules().get_level()):
                                if(slots[i].get_session().get_date() == slots[j].get_session().get_date()):
                                    self._numOfConflicts +=1
                                    #print(slots[i].get_session().get_date())
                    
                    #Assigning different modules in one room and check if they are not exceeding room capacity
                    if(slots[i].get_session() == slots[j].get_session() and slots[i].get_slot_id() != slots[j].get_slot_id()):
                        if(slots[i].get_room() == slots[j].get_room()):
                            if((slots[i].get_modules().get_numOfStudents() + slots[j].get_modules().get_numOfStudents() > slots[j].get_room().get_seating_capacity() )):
                                self._numOfConflicts+=1

                    
                         
            #hard constraints check clashing modules from different programs
            if(slots[i].get_modules().get_isMassModule() ==True):
                shared_programs = slots[i].get_modules().get_shared_programs()
                for share in shared_programs:
                    for program in PROGRAMS_ARRAY:
                        if program._program_code == share.get_shared_programs():
                            for module in program.get_level_modules(share.get_level()):
                                for index in range(0,len(slots)):
                                    if(slots[index].get_modules().get_module_code() == module.get_module_code()):
                                        if(slots[index].get_session() ==slots[i].get_session()):
                                            self._numOfConflicts +=1
                    
        for i in range(0,len(slots)):
                for j in range(0,len(slots)):
                    if(j >i):
                        #check if two modules of the same student are not written in the same day
                        if((j-i)==1):
                            if(slots[i].get_modules().get_program_code() ==slots[j].get_modules().get_program_code()): 
                                if(slots[i].get_modules().get_level() ==slots[j].get_modules().get_level()):
                                    if(slots[i].get_session().get_date() == slots[j].get_session().get_date()):
                                        self._numOfConflicts +=1
                                        #print(slots[i].get_session().get_date())

                        if(slots[i].get_session() == slots[j].get_session() and slots[i].get_slot_id() != slots[j].get_slot_id()):
                            if(slots[i].get_room() == slots[j].get_room()):
                                if((slots[i].get_modules().get_numOfStudents() + slots[j].get_modules().get_numOfStudents() > slots[j].get_room().get_seating_capacity() )):
                                    self._numOfConflicts+=1

        #check if number of students allocated to the room does not
        # exceed the room seating capacity
        for session in SESSIONS_ARRAY:
            for room in ROOMS_ARRAY:
                students =0
                for slot in slots: 
                    if slot.get_session().get_time() == session.get_time() and slot.get_room().get_room_number() == room.get_room_number():
                        if slot.get_session().get_date() == session.get_date():
                            students += slot.get_modules().get_numOfStudents()
                            if room.get_seating_capacity() < students:
                                self._numOfConflicts+=1
        #return fitness value of the timetable
        return 1 / ((1.0 * self._numOfConflicts + 1))
    
    def __str__(self):
        returnValue =""
        for i in range(0,len(self._slots)-1):
            returnValue += str(self._slots[i]) + ", "
        returnValue += str(self._slots[len(self._slots)-1])
        return returnValue

class GeneticAlgorithm:
    def evolve(self,population):
        return self._mutate_population(self._crossover_population(population))
    
    def _crossover_population(self,pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1,schedule2))
            i +=1
        return crossover_pop

    def _mutate_population(self,population):
        for i in range(NUMB_OF_ELITE_SCHEDULES,POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population
    
    def _crossover_schedule(self,schedule1,schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0,len(crossoverSchedule.get_slots())):
            if(rnd.random()>0.5): crossoverSchedule.get_slots()[i] = schedule1.get_slots()[i]
            else: crossoverSchedule.get_slots()[i]=schedule2.get_slots()[i]
        return crossoverSchedule

    def _mutate_schedule(self,mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_slots())):
            if(MUTATION_RATE > rnd.random()): mutateSchedule.get_slots()[i] = schedule.get_slots()[i]
        return mutateSchedule
    
    def _select_tournament_population(self,pop):
        tournament_pop = Population(0)
        i =0
        while i < TOURNAMENT_SELECTION_SIZE:
            #print(schedules[i].calculate_fitness())
            #get_fitness()
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0,POPULATION_SIZE)])
            i +=1
        #tournament_pop.get_schedules()[i].calculate_fitness()
        #calculate_fitness()
        tournament_pop.get_schedules().sort(key=lambda x:x.calculate_fitness(),reverse=True)
        #tournament_pop.get_schedules().sort(key=lambda x:x.get_fitness(),reverse=True)
        return tournament_pop

class DisplayMgr:
    def print_available_data(self):
        print('> All Available Data')
        self.print_program()
        self.print_modules()
        self.print_room()
        self.print_sessions()
    def print_program(self):
        programs = dataset.get_programs()
        availableProgramTable = PrettyTable(['Program','modules'])
        for i in range(0,len(programs)):
            modules = programs[i].get_modules()
            tempStr = "["
            for j in range(0,len(modules)-1):
                tempStr += modules[j].__str__() + "]"
            tempStr += modules[len(modules)-1].__str__() + "]"
            availableProgramTable.add_row([programs[i].get_program_name(), tempStr])
            print(availableProgramTable)

    def print_modules(self):
        availableModulesTable = PrettyTable(['Module Code','Level','Num # of students','Is Mass Module'])
        modules = dataset.get_modules()
        for i in range(0,len(modules)):
            availableModulesTable.add_row(
                [modules[i].get_module_code(), modules[i].get_level(),str(modules[i].get_numOfStudents()),modules[i].get_isMassModule()])
        print(availableModulesTable)

    def print_room(self):
        availableRoomsTable = PrettyTable(['room #','max seating capacity'])
        rooms = dataset.get_rooms()
        for i in range(0,len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_room_number()),str(rooms[i].get_seating_capacity())])
            print(availableRoomsTable)

    def print_sessions(self):
        availableSessions = PrettyTable(['Session id','Date','Time'])
        sessions = dataset.get_sessions()
        for i in range(0,len(sessions)):
            availableSessions.add_row([sessions[i].get_session_id(), sessions[i].get_date(), sessions[i].get_time()])
        print(availableSessions)
    
    def print_generation(self, population):
        table1 = PrettyTable(['schedule #','fitness','# of conflicts'])
        schedules = population.get_schedules()
        for i in range(0,len(schedules)):
            #todo
            schedules[i].calculate_fitness()
            table1.add_row([str(i),round(schedules[i].get_fitness(),3),schedules[i].get_numbOfConflicts()])
            #table1.add_row([str(i),schedules[i].get_fitness(),schedules[i].get_numbOfConflicts(),schedules[i]])
        print(table1)

    def print_schedule_as_table(self,schedule):
        slots = schedule.get_slots()
        table = PrettyTable(['slot #','program','Module (code, max # of students)','Room (Capacity)','Session (Date,Time)'])
        for i in range(0,len(slots)):
            table.add_row([str(i),slots[i].get_programs().get_program_code(),slots[i].get_modules().get_title() + " (" +
            slots[i].get_modules().get_module_code() + ", " + str(slots[i].get_modules().get_numOfStudents()) + ")",
            slots[i]. get_room().get_room_number() + " ("  + str(slots[i].get_room().get_seating_capacity()) + ")",
            slots[i].get_session().get_session_id()+ " | " + str(slots[i].get_session().get_date())+ " (" + str(slots[i].get_session().get_time()) + ")"])
        print(table)

