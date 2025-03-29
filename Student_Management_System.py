class StudentManagement:
    def __init__(self):
        self.student_details={}
        self.counter=1
    def add_student(self,sid,name,course,marks):
        if sid in [detail['sid'] for detail in self.student_details.values()]:
             print(f'Duplicate sid: {sid}')
             return None

        if course not in [detail['course'] for detail in self.student_details.values()]:
            self.student_details[self.counter]={
                'sid':sid,
                'name':name,
                'course':course,
                'marks':marks,
            }
            self.counter+=1
        else:
            print(f'Duplicate Course: {course}')

    def fetch_student(self,sid):
        for key,value in self.student_details.items():
            if value['sid'] ==sid:
                print(value)
                break
        else:
            print(f'No Student found with id: {sid}')
    
    def update_student(self,sid,name,course,marks):
        for key,value in self.student_details.items():
            if value['sid'] == sid :
                value['name']=name
                value['course']=course
                value['marks']=marks
                print(f'Successfully updated student record with id : {sid}')
                break
        else:
            print(f'No Student found with id: {sid}')
    
    def delete_student(self,sid):
        for key,value in self.student_details.items():
            if value['sid'] == sid :
                self.student_details.pop(key)
                print(f'Successfully deleted student record with id : {sid}')
                break
        else:
            print(f'No Student found with id: {sid}')

    def highest_marks_student(self):
         maxmarks=max([detail['marks'] for detail in self.student_details.values()])
         for key,value in self.student_details.items():
             if value['marks']==maxmarks:
                 print(value)

    def lowest_marks_student(self):
         minmarks=min([detail['marks'] for detail in self.student_details.values()])
         for key,value in self.student_details.items():
             if value['marks']==minmarks:
                 print(value)
    def fetch_all_students(self):
        print(list(self.student_details.values()))

            
                


s1=StudentManagement()   
s1.add_student(12,'ram','CSE',900)     
s1.add_student(14,'sita','ECE',800) 
s1.add_student(34,'radha','CE',200) 
s1.add_student(64,'sam','ME',100) 
s1.add_student(78,'sam','ME',999) 

s1.fetch_student(34)
s1.update_student(34,'Radha','EEE',500)
s1.fetch_student(34)
s1.delete_student(34)
s1.fetch_student(34)
s1.highest_marks_student()
s1.lowest_marks_student()

s1.add_student(12,'abc','CSE',600)     
s1.add_student(72,'abc','CSE',600)   
s1.fetch_all_students()  







        