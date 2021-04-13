def grade_calc(name:str, code_grade, presentation_grade, final_grade):
    '''
    This function calculates the IBI students grade.
    '''
    grade = 0.4*code_grade + 0.3*presentation_grade + 0.3*final_grade
    return name, grade

# example 0
name_grade_tuple = grade_calc('ZHANG San', 100, 95, 100)
print(name_grade_tuple)

# example 1
# name, grade = grade_calc('ZHANG San', 100, 95, 100)
# print(name, grade)