
'''
class Module stores module information
it stores module code, title,program_code
semester level, number_of_students and also 
isSharedModule to indicate that this module is shared 
between different programs
'''
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

'''
class Program stores the program_code
program name and an array of modules
for that program
'''
class Program:
    def __init__(self,program_code,program_name,modules):
        self._program_code = program_code
        self._program_name = program_name
        self._modules = modules

    def get_program_code(self):return self._program_code
    def get_program_name(self):return self._program_name
    def get_modules(self):return self._modules

#Modules data

#Information Systems modules
#=======================================================================
#level 1.1
module_INFO1 = Module('LANP101','Portuguese','INFO','1.1',10,'CS50',False)
module_INFO2 = Module('COSK101','Basic Communication skills','INFO','1.1',10,'CS50',False)
module_INFO3 = Module('BMAN101','Principles of Management','INFO','1.1',20,'CS50',False)
module_INFO4 = Module('ACCT102','Financial Accounting For Business 1A','INFO','1.1',10,'CS50',False)
module_INFO5 = Module('INSY102','Introduction to Computer Science','INFO','1.1',30,'CS50',True,[{'program_code':'ACC','Level':'1.1'},{'program_code':'BM','Level':'1.1'}])
module_INFO6 = Module('INSY103','Principles of Computer Programming','INFO','1.1',20,'CS50',False)
module_INFO7 = Module('INSY104','Computer Organisation and Architecture','INFO','1.1',10,'CS50',False)
#level 1.2
module_INFO9 = Module('BMAN122','Business Communication','INFO','1.2',10,'CS50',False)
module_INFO10 = Module('ACCT123','Financial Accounting For Business 1B','INFO','1.2',10,'CS50',False)
module_INFO11 = Module('INSY121','Computational Mathematics for Information','INFO','1.2',10,'CS50',False)
module_INFO12 = Module('INSY122','Database Systems','INFO','1.2',10,'CS50',False)
module_INFO13 = Module('INSY123','Systems Analysis and Design','INFO','1.2',30,'CS50',False,[{'program_code':'ACC','Level':'1.1'},{'program_code':'BM','Level':'1.1'}])
module_INFO14 = Module('INSY124','Technovation','INFO','1.2',20,'CS50',False)
module_INFO15 = Module('BCOS122','Data Structures and Algorithms','INFO','1.2',10,'CS50',False)
#level 2.1
module_INFO16 = Module('INSY211','Psychology of Computing','INFO','2.1',10,'CS50',False)
module_INFO17 = Module('INSY212','Management Information Systems','INFO','2.1',10,'CS50',False)
module_INFO18 = Module('INSY213','Digital Financial Services','INFO','2.1',10,'CS50',False)
module_INFO19 = Module('INSY214','Visual Programming','INFO','2.1',10,'CS50',False)
module_INFO20 = Module('BCOS211','Web Technologies and Mobile Application','INFO','2.1',30,'CS50',False,[{'program_code':'ACC','Level':'1.1'},{'program_code':'BM','Level':'1.1'}])
module_INFO21 = Module('ASTA217','Research Methods','INFO','2.1',20,'CS50',False)
module_INFO22 = Module('SSGS217','Introduction to Gender Studies','INFO','2.1',10,'CS50',False)
#level 2.2
module_INFO23 = Module('INSY221','E-Business','INFO','2.2',10,'CS50',False)
module_INFO24 = Module('INSY222','ICT Project Management','INFO','2.2',10,'CS50',False)
module_INFO25 = Module('INSY223','Enterprise Team Project','INFO','2.2',10,'CS50',False)
module_INFO26 = Module('BCOS221','Data Communications and Computer Networks','INFO','2.2',10,'CS50',False)
module_INFO27 = Module('BCOS213','Software Engineering','INFO','2.2',30,'CS50',False,[{'program_code':'ACC','Level':'1.1'},{'program_code':'BM','Level':'1.1'}])
module_INFO28 = Module('BCOS223','Object Oriented Methodologies','INFO','2.2',20,'CS50',False)
module_INFO29 = Module('BMAN221','Entrepreneurship Theory and Practice','INFO','2.2',10,'CS50',False)

#Accounting Modules modules
#=======================================================================
#level 1.1
module_ACC01 = Module('HACC101','Intro to Accounts 1','ACC','1.1',20,'HACC45',False)
module_ACC02 = Module('HACC102','Intro to Accounts 2','ACC','1.1',20,'HACC45',False)
module_ACC03 = Module('HACC103','Intro to Accounts 3','ACC','1.1',20,'HACC45',False)
module_ACC04 = Module('HACC104','Intro to Accounts 4','ACC','1.1',20,'HACC45',False)
module_ACC05 = Module('HACC105','Intro to Accounts 5','ACC','1.1',20,'HACC45',False)
module_ACC06 = Module('HACC106','Intro to Accounts 6','ACC','1.1',20,'HACC45',False)
module_ACC07 = Module('HACC107','Intro to Accounts 7','ACC','1.1',20,'HACC45',False)
module_ACC08 = Module('HACC108','Intro to Accounts 8','ACC','1.1',20,'HACC45',False)
#level 1.2
module_ACC09 = Module('HACC121','Tax Accounts 1','ACC','1.2',20,'HACC45',False)
module_ACC010 = Module('HACC122','Tax Accounts 2','ACC','1.2',20,'HACC45',False)
module_ACC011 = Module('HACC123','Tax Accounts 3','ACC','1.2',20,'HACC45',False)
module_ACC012 = Module('HACC124','Tax Accounts 4','ACC','1.2',20,'HACC45',False)
module_ACC013 = Module('HACC125','Tax Accounts 5','ACC','1.2',20,'HACC45',False)
module_ACC014 = Module('HACC126','Tax Accounts 6','ACC','1.2',20,'HACC45',False)
module_ACC015 = Module('HACC127','Tax Accounts 7','ACC','1.2',20,'HACC45',False)
module_ACC016 = Module('HACC128','Tax Accounts 8','ACC','1.2',20,'HACC45',False)
#level 2.1
module_ACC017 = Module('HACC211','Finance Accounts 1','ACC','2.1',20,'HACC45',False)
module_ACC018 = Module('HACC212','Finance Accounts 2','ACC','2.1',20,'HACC45',False)
module_ACC019 = Module('HACC213','Finance Accounts 3','ACC','2.1',20,'HACC45',False)
module_ACC020 = Module('HACC214','Finance Accounts 4','ACC','2.1',20,'HACC45',False)
module_ACC021 = Module('HACC215','Finance Accounts 5','ACC','2.1',20,'HACC45',False)
module_ACC022 = Module('HACC216','Finance Accounts 6','ACC','2.1',20,'HACC45',False)
module_ACC023 = Module('HACC217','Finance Accounts 7','ACC','2.1',20,'HACC45',False)
module_ACC024 = Module('HACC218','Finance Accounts 8','ACC','2.1',20,'HACC45',False)
#level 2.2
module_ACC025 = Module('HACC221','Costing Accounts 1','ACC','2.2',20,'HACC45',False)
module_ACC026 = Module('HACC222','Costing Accounts 2','ACC','2.2',20,'HACC45',False)
module_ACC027 = Module('HACC223','Costing Accounts 3','ACC','2.2',20,'HACC45',False)
module_ACC028 = Module('HACC224','Costing Accounts 4','ACC','2.2',20,'HACC45',False)
module_ACC029 = Module('HACC225','Costing Accounts 5','ACC','2.2',20,'HACC45',False)
module_ACC030 = Module('HACC226','Costing Accounts 6','ACC','2.2',20,'HACC45',False)
module_ACC031 = Module('HACC227','Costing Accounts 7','ACC','2.2',20,'HACC45',False)
module_ACC032 = Module('HACC228','Costing Accounts 8','ACC','2.2',20,'HACC45',False)

#Business Management Modules modules
#=======================================================================
#level 1.1
module_BM01 = Module('BSM111','Introduction to BM 1','BM','1.1',10,'BM20',False)
module_BM02 = Module('BSM112','Introduction to BM 2','BM','1.1',10,'BM20',False)
module_BM03 = Module('BSM113','Introduction to BM 3','BM','1.1',10,'BM20',False)
module_BM04 = Module('BSM114','Introduction to BM 4','BM','1.1',10,'BM20',False)
module_BM05 = Module('BSM115','Introduction to BM 5','BM','1.1',10,'BM20',False)
module_BM06 = Module('BSM116','Introduction to BM 6','BM','1.1',10,'BM20',False)
module_BM07 = Module('BSM117','Introduction to BM 7','BM','1.1',10,'BM20',False)
module_BM08 = Module('BSM118','Introduction to BM 8','BM','1.1',10,'BM20',False)
#level 1.2
module_BM09 = Module('BSM121','Financial BM 1','BM','1.2',10,'BM20',False)
module_BM10 = Module('BSM122','Financial BM 2','BM','1.2',10,'BM20',False)
module_BM11 = Module('BSM123','Financial BM 3','BM','1.2',10,'BM20',False)
module_BM12 = Module('BSM124','Financial BM 4','BM','1.2',10,'BM20',False)
module_BM13 = Module('BSM125','Financial BM 5','BM','1.2',10,'BM20',False)
module_BM14 = Module('BSM126','Financial BM 6','BM','1.2',10,'BM20',False)
module_BM15 = Module('BSM127','Financial BM 7','BM','1.2',10,'BM20',False)
module_BM16 = Module('BSM128','Financial BM 8','BM','1.2',10,'BM20',False)
#level 2.1
module_BM17 = Module('BSM211','Financial 2 BM 1','BM','2.1',10,'BM20',False)
module_BM18 = Module('BSM212','Financial 2 BM 2','BM','2.1',10,'BM20',False)
module_BM19 = Module('BSM213','Financial 2 BM 3','BM','2.1',10,'BM20',False)
module_BM20 = Module('BSM214','Financial 2 BM 4','BM','2.1',10,'BM20',False)
module_BM21 = Module('BSM215','Financial 2 BM 5','BM','2.1',10,'BM20',False)
module_BM22 = Module('BSM216','Financial 2 BM 6','BM','2.1',10,'BM20',False)
module_BM23 = Module('BSM217','Financial 2 BM 7','BM','2.1',10,'BM20',False)
module_BM24 = Module('BSM218','Financial 2 BM 8','BM','2.1',10,'BM20',False)
#level 2.2
module_BM25 = Module('BSM221','Business Management 1','BM','2.2',10,'BM20',False)
module_BM26 = Module('BSM222','Business Management 2','BM','2.2',10,'BM20',False)
module_BM27 = Module('BSM223','Business Management 3','BM','2.2',10,'BM20',False)
module_BM28 = Module('BSM224','Business Management 4','BM','2.2',10,'BM20',False)
module_BM29 = Module('BSM225','Business Management 5','BM','2.2',10,'BM20',False)
module_BM30 = Module('BSM226','Business Management 6','BM','2.2',10,'BM20',False)
module_BM31 = Module('BSM227','Business Management 7','BM','2.2',10,'BM20',False)
module_BM32 = Module('BSM228','Business Management 8','BM','2.2',10,'BM20',False)

#Tourism Modules modules
#=======================================================================
#level 1.1
module_TRSM01 = Module('TOUR111','Introduction to Tourism 1','TRSM','1.1',10,'TRSM50',False)
module_TRSM02 = Module('TOUR112','Introduction to Tourism 2','TRSM','1.1',10,'TRSM50',False)
module_TRSM03 = Module('TOUR113','Introduction to Tourism 3','TRSM','1.1',10,'TRSM50',False)
module_TRSM04 = Module('TOUR114','Introduction to Tourism 4','TRSM','1.1',10,'TRSM50',False)
module_TRSM05 = Module('TOUR115','Introduction to Tourism 5','TRSM','1.1',10,'TRSM50',False)
module_TRSM06 = Module('TOUR116','Introduction to Tourism 6','TRSM','1.1',10,'TRSM50',False)
module_TRSM07 = Module('TOUR117','Introduction to Tourism 7','TRSM','1.1',10,'TRSM50',False)
module_TRSM08 = Module('TOUR118','Introduction to Tourism 8','TRSM','1.1',10,'TRSM50',False)
#level 1.2
module_TRSM09 = Module('TOUR121','Hospitality 1','TRSM','1.2',10,'TRSM50',False)
module_TRSM10 = Module('TOUR122','Hospitality 2','TRSM','1.2',10,'TRSM50',False)
module_TRSM11 = Module('TOUR123','Hospitality 3','TRSM','1.2',10,'TRSM50',False)
module_TRSM12 = Module('TOUR124','Hospitality 4','TRSM','1.2',10,'TRSM50',False)
module_TRSM13 = Module('TOUR125','Hospitality 5','TRSM','1.2',10,'TRSM50',False)
module_TRSM14 = Module('TOUR126','Hospitality 6','TRSM','1.2',10,'TRSM50',False)
module_TRSM15 = Module('TOUR127','Hospitality 7','TRSM','1.2',10,'TRSM50',False)
module_TRSM16 = Module('TOUR128','Hospitality 8','TRSM','1.2',10,'TRSM50',False)
#level 2.1
module_TRSM17 = Module('TOUR211','Tourism and Hosp 1','TRSM','2.1',10,'TRSM50',False)
module_TRSM18 = Module('TOUR212','Tourism and Hosp 2','TRSM','2.1',10,'TRSM50',False)
module_TRSM19 = Module('TOUR213','Tourism and Hosp 3','TRSM','2.1',10,'TRSM50',False)
module_TRSM20 = Module('TOUR214','Tourism and Hosp 4','TRSM','2.1',10,'TRSM50',False)
module_TRSM21 = Module('TOUR215','Tourism and Hosp 5','TRSM','2.1',10,'TRSM50',False)
module_TRSM22 = Module('TOUR216','Tourism and Hosp 6','TRSM','2.1',10,'TRSM50',False)
module_TRSM23 = Module('TOUR217','Tourism and Hosp 7','TRSM','2.1',10,'TRSM50',False)
module_TRSM24 = Module('TOUR218','Tourism and Hosp 8','TRSM','2.1',10,'TRSM50',False)
#level 2.2
module_TRSM25 = Module('TOUR221','Cooking Practice 1','TRSM','2.2',10,'TRSM50',False)
module_TRSM26 = Module('TOUR222','Cooking Practice 2','TRSM','2.2',10,'TRSM50',False)
module_TRSM27 = Module('TOUR223','Cooking Practice 3','TRSM','2.2',10,'TRSM50',False)
module_TRSM28 = Module('TOUR224','Cooking Practice 4','TRSM','2.2',10,'TRSM50',False)
module_TRSM29 = Module('TOUR225','Cooking Practice 5','TRSM','2.2',10,'TRSM50',False)
module_TRSM30 = Module('TOUR226','Cooking Practice 6','TRSM','2.2',10,'TRSM50',False)
module_TRSM31 = Module('TOUR227','Cooking Practice 7','TRSM','2.2',10,'TRSM50',False)
module_TRSM32 = Module('TOUR228','Cooking Practice 8','TRSM','2.2',10,'TRSM50',False)

#Chemical Engineering Modules modules
#=======================================================================
#level 1.1
module_CHM01 = Module('CHEM111','Introduction to Chem Eng 1','CHEM','1.1',8,'CHEM35',False)
module_CHM02 = Module('CHEM112','Introduction to Chem Eng 2','CHEM','1.1',8,'CHEM35',False)
module_CHM03 = Module('CHEM113','Introduction to Chem Eng 3','CHEM','1.1',8,'CHEM35',False)
module_CHM04 = Module('CHEM114','Introduction to Chem Eng 4','CHEM','1.1',8,'CHEM35',False)
module_CHM05 = Module('CHEM115','Introduction to Chem Eng 5','CHEM','1.1',8,'CHEM35',False)
module_CHM06 = Module('CHEM116','Introduction to Chem Eng 6','CHEM','1.1',8,'CHEM35',False)
module_CHM07 = Module('CHEM117','Introduction to Chem Eng 7','CHEM','1.1',8,'CHEM35',False)
module_CHM08 = Module('CHEM118','Introduction to Chem Eng 8','CHEM','1.1',8,'CHEM35',False)
#level 1.2
module_CHM09 = Module('CHEM121','Chemical Engineering P 1','CHEM','1.2',8,'CHEM35',False)
module_CHM10 = Module('CHEM122','Chemical Engineering P 2','CHEM','1.2',8,'CHEM35',False)
module_CHM11 = Module('CHEM123','Chemical Engineering P 3','CHEM','1.2',8,'CHEM35',False)
module_CHM12 = Module('CHEM124','Chemical Engineering P 4','CHEM','1.2',8,'CHEM35',False)
module_CHM13 = Module('CHEM125','Chemical Engineering P 5','CHEM','1.2',8,'CHEM35',False)
module_CHM14 = Module('CHEM126','Chemical Engineering P 6','CHEM','1.2',8,'CHEM35',False)
module_CHM15 = Module('CHEM127','Chemical Engineering P 7','CHEM','1.2',8,'CHEM35',False)
module_CHM16 = Module('CHEM128','Chemical Engineering P 8','CHEM','1.2',8,'CHEM35',False)
#level 2.1
module_CHM17 = Module('CHEM211','Chemical Processing Eng 1','CHEM','2.1',8,'CHEM35',False)
module_CHM18 = Module('CHEM212','Chemical Processing Eng 2','CHEM','2.1',8,'CHEM35',False)
module_CHM19 = Module('CHEM213','Chemical Processing Eng 3','CHEM','2.1',8,'CHEM35',False)
module_CHM20 = Module('CHEM214','Chemical Processing Eng 4','CHEM','2.1',8,'CHEM35',False)
module_CHM21 = Module('CHEM215','Chemical Processing Eng 5','CHEM','2.1',8,'CHEM35',False)
module_CHM22 = Module('CHEM216','Chemical Processing Eng 6','CHEM','2.1',8,'CHEM35',False)
module_CHM23 = Module('CHEM217','Chemical Processing Eng 7','CHEM','2.1',8,'CHEM35',False)
module_CHM24 = Module('CHEM218','Chemical Processing Eng 8','CHEM','2.1',8,'CHEM35',False)
#level 2.2
module_CHM25 = Module('CHEM221','Chemical Practical 1','CHEM','2.2',8,'CHEM35',False)
module_CHM26 = Module('CHEM222','Chemical Practical 2','CHEM','2.2',8,'CHEM35',False)
module_CHM27 = Module('CHEM223','Chemical Practical 3','CHEM','2.2',8,'CHEM35',False)
module_CHM28 = Module('CHEM224','Chemical Practical 4','CHEM','2.2',8,'CHEM35',False)
module_CHM29 = Module('CHEM225','Chemical Practical 5','CHEM','2.2',8,'CHEM35',False)
module_CHM30 = Module('CHEM226','Chemical Practical 6','CHEM','2.2',8,'CHEM35',False)
module_CHM31 = Module('CHEM227','Chemical Practical 7','CHEM','2.2',8,'CHEM35',False)
module_CHM32 = Module('CHEM228','Chemical Practical 8','CHEM','2.2',8,'CHEM35',False)

#Mining Eng Modules modules
#=======================================================================
#level 1.1
module_MNG01 = Module('MNG111','Introduction to Mining 1','MNG','1.1',8,'MNG20',False)
module_MNG02 = Module('MNG112','Introduction to Mining 2','MNG','1.1',8,'MNG20',False)
module_MNG03 = Module('MNG113','Introduction to Mining 3','MNG','1.1',8,'MNG20',False)
module_MNG04 = Module('MNG114','Introduction to Mining 4','MNG','1.1',8,'MNG20',False)
module_MNG05 = Module('MNG115','Introduction to Mining 5','MNG','1.1',8,'MNG20',False)
module_MNG06 = Module('MNG116','Introduction to Mining 6','MNG','1.1',8,'MNG20',False)
module_MNG07 = Module('MNG117','Introduction to Mining 7','MNG','1.1',8,'MNG20',False)
module_MNG08 = Module('MNG118','Introduction to Mining 8','MNG','1.1',8,'MNG20',False)
#level 1.2
module_MNG09 = Module('MNG121','Drilling Engineering 1','MNG','1.2',8,'MNG20',False)
module_MNG10 = Module('MNG122','Drilling Engineering 2','MNG','1.2',8,'MNG20',False)
module_MNG11 = Module('MNG123','Drilling Engineering 3','MNG','1.2',8,'MNG20',False)
module_MNG12 = Module('MNG124','Drilling Engineering 4','MNG','1.2',8,'MNG20',False)
module_MNG13 = Module('MNG125','Drilling Engineering 5','MNG','1.2',8,'MNG20',False)
module_MNG14 = Module('MNG126','Drilling Engineering 6','MNG','1.2',8,'MNG20',False)
module_MNG15 = Module('MNG127','Drilling Engineering 7','MNG','1.2',8,'MNG20',False)
module_MNG16 = Module('MNG128','Drilling Engineering 8','MNG','1.2',8,'MNG20',False)
#level 2.1
module_MNG17 = Module('MNG211','Mining Eng 1','MNG','2.1',8,'MNG20',False)
module_MNG18 = Module('MNG212','Mining Eng 2','MNG','2.1',8,'MNG20',False)
module_MNG19 = Module('MNG213','Mining Eng 3','MNG','2.1',8,'MNG20',False)
module_MNG20 = Module('MNG214','Mining Eng 4','MNG','2.1',8,'MNG20',False)
module_MNG21 = Module('MNG215','Mining Eng 5','MNG','2.1',8,'MNG20',False)
module_MNG22 = Module('MNG216','Mining Eng 6','MNG','2.1',8,'MNG20',False)
module_MNG23 = Module('MNG217','Mining Eng 7','MNG','2.1',8,'MNG20',False)
module_MNG24 = Module('MNG218','Mining Eng 8','MNG','2.1',8,'MNG20',False)
#level 2.2
module_MNG25 = Module('MNG221','Field Engineering 1','MNG','2.2',8,'MNG20',False)
module_MNG26 = Module('MNG222','Field Engineering 2','MNG','2.2',8,'MNG20',False)
module_MNG27 = Module('MNG223','Field Engineering 3','MNG','2.2',8,'MNG20',False)
module_MNG28 = Module('MNG224','Field Engineering 4','MNG','2.2',8,'MNG20',False)
module_MNG29 = Module('MNG225','Field Engineering 5','MNG','2.2',8,'MNG20',False)
module_MNG30 = Module('MNG226','Field Engineering 6','MNG','2.2',8,'MNG20',False)
module_MNG31 = Module('MNG227','Field Engineering 7','MNG','2.2',8,'MNG20',False)
module_MNG32 = Module('MNG228','Field Engineering 8','MNG','2.2',8,'MNG20',False)
#====================================================

#Initialise modules
MODULES = [
module_INFO1,module_INFO2,module_INFO3,module_INFO4,module_INFO5
,module_INFO6,module_INFO7,module_INFO9,module_INFO10
,module_INFO11,module_INFO12,module_INFO13,module_INFO14
,module_INFO15,module_INFO16,module_INFO17,module_INFO18,module_INFO19
,module_INFO20,module_INFO21,module_INFO22,module_INFO23,module_INFO24
,module_INFO25,module_INFO26,module_INFO27,module_INFO28,module_INFO29,
module_ACC01,module_ACC02,module_ACC03,module_ACC04,module_ACC05,module_ACC06
,module_ACC07,module_ACC08,module_ACC09,module_ACC010,module_ACC011,module_ACC012
,module_ACC013,module_ACC014,module_ACC015,module_ACC016,module_ACC017
,module_ACC018,module_ACC019,module_ACC020,module_ACC021,module_ACC022
,module_ACC023,module_ACC024,module_ACC025,module_ACC026,module_ACC027
,module_ACC028,module_ACC029,module_ACC030,module_ACC031,module_ACC032,
module_BM01,module_BM02,module_BM03,module_BM04,module_BM05,module_BM06
,module_BM07,module_BM08,module_BM09,module_BM10,module_BM11,module_BM12
,module_BM13,module_BM14,module_BM15,module_BM16,module_BM17,module_BM18
,module_BM19,module_BM20,module_BM21,module_BM22,module_BM23,module_BM24
,module_BM25,module_BM26,module_BM27,module_BM28,module_BM29,module_BM30
,module_BM31,module_BM32,
module_TRSM01,module_TRSM02,module_TRSM03,module_TRSM04,module_TRSM05
,module_TRSM06,module_TRSM07,module_TRSM08,module_TRSM09,module_TRSM10
,module_TRSM11,module_TRSM12,module_TRSM13,module_TRSM14,module_TRSM15
,module_TRSM16,module_TRSM17,module_TRSM18,module_TRSM19,module_TRSM20
,module_TRSM21,module_TRSM22,module_TRSM23,module_TRSM24,module_TRSM25
,module_TRSM26,module_TRSM27,module_TRSM28,module_TRSM29,module_TRSM30
,module_TRSM31,module_TRSM32,
module_CHM01,module_CHM02,module_CHM03,module_CHM04,module_CHM05
,module_CHM06,module_CHM07,module_CHM08,module_CHM09,module_CHM10
,module_CHM11,module_CHM12,module_CHM13,module_CHM14,module_CHM15
,module_CHM16,module_CHM17,module_CHM18,module_CHM19,module_CHM20
,module_CHM21,module_CHM22,module_CHM23,module_CHM24,module_CHM25
,module_CHM26,module_CHM27,module_CHM28,module_CHM29,module_CHM30
,module_CHM31,module_CHM32,

module_MNG01,module_MNG02,module_MNG03,module_MNG04,module_MNG05
,module_MNG06,module_MNG07,module_MNG08,module_MNG09,module_MNG10
,module_MNG11,module_MNG12,module_MNG13,module_MNG14,module_MNG15
,module_MNG16,module_MNG17,module_MNG18,module_MNG19,module_MNG20
,module_MNG21,module_MNG22,module_MNG23,module_MNG24,module_MNG25
,module_MNG26,module_MNG27,module_MNG28,module_MNG29,module_MNG30
,module_MNG31,module_MNG32

]

program1 = Program('INFO','Information Systems',[module_INFO1,module_INFO2,module_INFO3,module_INFO4,module_INFO5
,module_INFO6,module_INFO7,module_INFO9,module_INFO10
,module_INFO11,module_INFO12,module_INFO13,module_INFO14
,module_INFO15,module_INFO16,module_INFO17,module_INFO18,module_INFO19
,module_INFO20,module_INFO21,module_INFO22,module_INFO23,module_INFO24
,module_INFO25,module_INFO26,module_INFO27,module_INFO28,module_INFO29])

program2 = Program('ACC','Accounting',[module_ACC01,module_ACC02,module_ACC03,module_ACC04,module_ACC05,module_ACC06
,module_ACC07,module_ACC08,module_ACC09,module_ACC010,module_ACC011,module_ACC012
,module_ACC013,module_ACC014,module_ACC015,module_ACC016,module_ACC017
,module_ACC018,module_ACC019,module_ACC020,module_ACC021,module_ACC022
,module_ACC023,module_ACC024,module_ACC025,module_ACC026,module_ACC027
,module_ACC028,module_ACC029,module_ACC030,module_ACC031,module_ACC032])

program3 = Program('BM','Business Management',[module_BM01,module_BM02,module_BM03,module_BM04,module_BM05,module_BM06
,module_BM07,module_BM08,module_BM09,module_BM10,module_BM11,module_BM12
,module_BM13,module_BM14,module_BM15,module_BM16,module_BM17,module_BM18
,module_BM19,module_BM20,module_BM21,module_BM22,module_BM23,module_BM24
,module_BM25,module_BM26,module_BM27,module_BM28,module_BM29,module_BM30
,module_BM31,module_BM32])

program4 = Program('TRSM','Tourism',[module_TRSM01,module_TRSM02,module_TRSM03,module_TRSM04,module_TRSM05
,module_TRSM06,module_TRSM07,module_TRSM08,module_TRSM09,module_TRSM10
,module_TRSM11,module_TRSM12,module_TRSM13,module_TRSM14,module_TRSM15
,module_TRSM16,module_TRSM17,module_TRSM18,module_TRSM19,module_TRSM20
,module_TRSM21,module_TRSM22,module_TRSM23,module_TRSM24,module_TRSM25
,module_TRSM26,module_TRSM27,module_TRSM28,module_TRSM29,module_TRSM30
,module_TRSM31,module_TRSM32])

program5 =Program('CHEM','Chemical Eng',[module_CHM01,module_CHM02,module_CHM03,module_CHM04,module_CHM05
,module_CHM06,module_CHM07,module_CHM08,module_CHM09,module_CHM10
,module_CHM11,module_CHM12,module_CHM13,module_CHM14,module_CHM15
,module_CHM16,module_CHM17,module_CHM18,module_CHM19,module_CHM20
,module_CHM21,module_CHM22,module_CHM23,module_CHM24,module_CHM25
,module_CHM26,module_CHM27,module_CHM28,module_CHM29,module_CHM30
,module_CHM31,module_CHM32,
])

program6 =Program('MNG','Mining Eng',[module_MNG01,module_MNG02,module_MNG03,module_MNG04,module_MNG05
,module_MNG06,module_MNG07,module_MNG08,module_MNG09,module_MNG10
,module_MNG11,module_MNG12,module_MNG13,module_MNG14,module_MNG15
,module_MNG16,module_MNG17,module_MNG18,module_MNG19,module_MNG20
,module_MNG21,module_MNG22,module_MNG23,module_MNG24,module_MNG25
,module_MNG26,module_MNG27,module_MNG28,module_MNG29,module_MNG30
,module_MNG31,module_MNG32])
#Initialise programs
AVAILABLE_PROGRAMS = [program1,program2,program3,program4,program5,program6]