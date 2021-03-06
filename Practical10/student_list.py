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
        print('Name:', self.first_name, f'{self.last_name:15}', 'Programme:', self.programme)

# example 0
studentA = Student('San', 'ZHANG', 'BMI')
studentA.info()

# example 1 This example can show the ability to exclude unknown programme name and rasie a ValueError.
# studentB = Student('Si', 'LI', 'ECE')