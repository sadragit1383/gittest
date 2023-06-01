class Course:
    def __init__(self,code_course,start_course,end_course,grade_course,cost_course,teacher):
        self.__code_course=code_course
        self.__start_course=start_course
        self.__end_course=end_course
        self.__grade_course=grade_course
        self.__cost_course=self._separate_thousands(cost_course)
        self.__teacher=teacher
        self.list_day=[]
        self.__all_cousrse=[]
        self.__all_cousrse.append(self)

#------------------------------------------------------#fun add day in list day with control the user----------------------------------------------------------------------------------------------
    def _add_day(self):
        member=int(input('Enter member days: '))
        for mem in range(member):
            days=input(f'Enter days{mem+1}:')
            self.list_day.append(days)
    def _add_day1(self):
        self._add_day()
    def add_day(self):
        self._add_day()
    
    def show_all_course(self):
        for course in self.__all_cousrse:
            print(course)
   
#--------------------------------------------for separate zero for price----------------------------------------------------------------------------------------------------------
    def _separate_thousands(self,number):
        number_str = str(number)
        result = ""
        for i in range(len(number_str)-1, -1, -1):
            result = number_str[i] + result
            if (len(number_str)-i) % 3 == 0 and i > 0:
                result = ',' + result
        return result
#------------------------------------------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        return f'code course:{self.__code_course}\tstart_course:{self.__start_course}\tend_course;{self.__end_course}\tgrade course:{self.__grade_course}\tteacher:{self.__teacher}cost_course:{self.__cost_course}'
# ------------------------------------------------------------------------------------------------------------------------------------------------------
   
#------------------------------------------------------------------------------------------------------------------------------------------------------
    def _show_info(self):
        print(f'code course:{self.__code_course}\tstart_course:{self.__start_course}\tend_course:{self.__end_course}\tgrade course:{self.__grade_course}\tteacher:{self.__teacher}\tcost course:{self.__cost_course}')
#----------------------------------------------------------show all information with days--------------------------------------------------------------------------------------------
    # def show_info(self):
        
    #     self._show_info()
    #     print(100*'-')

############################################################################################################################

class Python(Course):
    def __init__(self, code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)
        # self.show_info()

class Java(Course):
    def __init__(self, code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)
        # self.show_info()


class Php(Course):
    def __init__(self, code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)
        # self.show_info()
############################################################################################################################
class Basic_python(Python):
    def __init__(self, code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)
class Advance_python(Python):
    def __init__(self, code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)
#------------------------------------------------------------------------------------------------------------------------------------------------------
class Basic_java(Java):
    def __init__(self, code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)
class Advance_java(Java):
    def __init__(self, code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)
#------------------------------------------------------------------------------------------------------------------------------------------------------
class Basic_php(Php):
    def __init__(self, code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)
class Advance_php(Php):
    def __init__(self, code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
class educational_institutions(Course):
    def __init__(self,name_edc ,code_course, start_course, end_course, grade_course, cost_course, teacher):
        super().__init__(code_course, start_course, end_course, grade_course, cost_course, teacher)
        self.__name_edc=name_edc
        self.__course_educational_institutions=[]
        
    def _add_course(self, *new_courses):
        for course in new_courses:
            self.__course_educational_institutions.append(course)

    def show_course(self):
        self._show_all_days()
        for course in self.__course_educational_institutions:
            print(course)
            
    def _show_all_days(self):
        print("All days:")
        for course in self.__course_educational_institutions:
            for day in course.list_day:
                print(day, end=' ')
            print() # add a newline after printing the days of each course
        

   


        
    
    
############################################################################################################################
# ایجاد یک شی از کلاس educational_institutions
educational_institutions1 = educational_institutions('name_edc', 11, '1400', '1401', 'basic', 200000, 'ali')

# اضافه کردن دوره‌ها به مؤسسه آموزشی
basic_java1 = Basic_java(11, '1401', '1402', 'basic', 200000, 'ali')
basic_java1.add_day()
advance_java1 = Advance_java(11, '1400', '1401', 'basic', 200000, 'ali')
advance_java1.add_day()
basic_php1 = Basic_php(11, '1400', '1401', 'basic', 200000, 'ali')
basic_php1.add_day()
advance_php1 = Advance_php(11, '1400', '1401', 'basic', 200000, 'ali')
basic_python1 = Basic_python(11, '1400', '1401', 'basic', 200000, 'ali')
advance_php1 = Advance_php(11, '1400', '1401', 'basic', 200000, 'ali')
advance_php1 = Advance_php(11, '1400', '1401', 'basic', 200000, 'ali')
basic_python1 = Basic_python(11, '1400', '1401', 'basic', 200000, 'ali')
advance_php1 = Advance_php(11, '1400', '1401', 'basic', 200000, 'ali')
basic_python1 = Basic_python(11, '1400', '1401', 'basic', 200000, 'ali')
basic_python1.add_day()
advance_python1 = Advance_python(11, '1400', '1401', 'basic', 200000, 'ali')
advance_python1.add_day()

educational_institutions1.add_course(basic_java1, advance_java1, basic_php1, advance_php1, basic_python1, advance_python1)

# نمایش تمام روزهای تمام دوره‌های مؤسسه آموزشی
educational_institutions1.show_course()
# educational_institutions1.show_all_days()
