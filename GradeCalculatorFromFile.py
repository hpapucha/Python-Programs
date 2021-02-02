#Reading information from .txt file and calculating grade points
#txt example bellow the code

#Prompting user to type name and setting counting varibles
desired_first_name = input("Input first name:")
desired_last_name = input("Input last name:")
total_credit_hours = 0
total_grade_points = 0.0


fin = open("grade-records.txt", "r")
line = fin.readline( )
while line != "":
    fields = line.split(",")
    last_name = fields[1].strip( )
    first_name = fields[2].strip( )
    credit_hours = fields[6].strip( )
    grade_points = fields[7].strip( )

#If the inputed name is the same with the .txt file field start
#a calculation loop for every field that corresponds.
    if desired_first_name == first_name and desired_last_name == last_name:

        if grade_points == "A":
            total_grade_points = credit_hours * 4
        elif grade_points == "B":
            total_grade_points = credit_hours * 3
        elif grade_points == "C":
            total_grade_points = credit_hours * 2
        elif grade_points == "D":
            total_grade_points = credit_hours * 1
        else:
            credit_hours = 0
    line = fin.readline( )


#Update the variables which count total credit hours and grades
total_credit_hours = total_credit_hours + credit_hours
total_grade_points = total_grade_points + grade_points
fin.close()  

#Calculating gpa with the formula
GPA = total_grade_points / total_credit_hours
print(f"GPA for {desired_first_name} {desired_last_name} is {round(gpa, 2)}.")


#txt example
stud_id,last_name,first_name,course_number,course_name,prof_name,credit_hours,grade
148383847,Hoffman,Raymond,ART104,Creating Art,Taylor,4,B
148383847,Hoffman,Raymond,CHM127,Quantitative Analysis,Shippley,4,A
148383847,Hoffman,Raymond,HST219,World History II,Black,4,B
148383847,Hoffman,Raymond,MAT140,Discrete Math I,Flick,4,C
148383847,Hoffman,Raymond,REL332,Feminist Ethics,Santos,4,A
184376436,Ferret,Nancy,BIO215,Ecology,Chu,4,B
195428395,Murphy,Thomas,MAT150,Calculus I,Rogers,4,B
195428395,Murphy,Thomas,BIO225,General Biology,Chu,4,A
201928737,Cirello,Brian,ART323,Japanese Art,Nagoro,2,A
201928737,Cirello,Brian,CHM131,General Chemistry I,Marcus,4,C
201928737,Cirello,Brian,CHM210,Physical Chemistry I,Shippley,4,F
201928737,Cirello,Brian,ENG220,Reading Poetry,Carmen,3,B
201928737,Cirello,Brian,HST214,Eastern Europe to 1699,Black,4,B
201928737,Cirello,Brian,SPA101,Basic Spanish I,Sanchez,4,D
415938372,Murphy,Eileen,MAT130,College Algebra,Serre,3,A
415938372,Murphy,Eileen,MAT140,Discrete Math I,Murphy,4,A
415938372,Murphy,Eileen,PE160,Volleyball,Perillo,2,A
415938372,Murphy,Eileen,PHY150,General Physics I,Garvey,4,B
593837233,Ramirez,Juanita,POL251,Politics of the USSR,Diamond,3,A
593837233,Ramirez,Juanita,WOM210,Values and Gender,Santos,3,B
   




    
    
    
    
    
