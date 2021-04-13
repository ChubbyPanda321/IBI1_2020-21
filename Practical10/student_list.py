class Student(object):
    def __init__(self, first_name:str, last_name:str, programme:str):
        self.first_name = first_name
        self.last_name = last_name
        programme_list = ['BMI','BMS']
        if programme in programme_list:
            self.programme = programme
        else:
            raise ValueError('Our institute does not have a programme called %s.'%programme)
    def info(self):
        print(self.first_name, self.last_name, self.programme)

studentA = Student('San', 'ZHANG', 'BMI')
studentA.info()