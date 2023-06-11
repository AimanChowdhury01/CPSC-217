#studentInfo
name = "Aiman Nawar Chowdhury, "
ID = "UCID: 30174339"
print("%s" %(name+ID))
print("%s" %("Mini-pre-A1"))
print("""Version: 20-Sep, 2022.
Learning objective:
Creating a complete Python program from the ground up with the use of common operators, variables,
getting input, displaying output, and formatting that output using escape codes & format specifiers.""")
print()
print()
#heading
heading = "TERM GRADE CALCULATOR"
print("%85s" %heading)
#Taking assignment inputs
print()
print()
print("Enter grades for your assignments:")
print()
print("\a*Grades for assignments can only accept numbers ranging from 0 to 4!*")
print()
a1 = float(input("What grade did you recieve in assignment 1?: "))
a2 = float(input("What grade did you recieve in assignment 2?: "))
a3 = float(input("What grade did you recieve in assignment 3?: "))


#Done taking input for assignments


#Taking inputs for exams
print()
print()
print("Enter your examination grades:")
print()
print("\a*Grades for examinations can only accept numbers ranging from 0 to 4.3!*")
mid = float(input("What grade did you recieve in your Midterm examination?: "))
final = float(input("What grade did you recieve in your Final examination?  : "))
#Done taking inputs



#back-end
wghtAssgn = float(a1)*0.15+ float(a2)*0.15+ float(a3)*0.20
wghtExam = float(mid)*0.20+ float(final)*0.30
termGPA = float(wghtAssgn) + float(wghtExam)

#final-output
print()
print()
print()
print("Original & weighted grade points, term grade point")
print()
print(("%28s" %"Assignments:\t") , end = "")
print("%0.1f" %a1 +"\t", end ="")
print("%0.1f" %a2 +"\t", end ="")
print("%0.1f" %a3 +"\t", end ="")
print()
print(("%28s" %"Examinations:\t" ), end = "")
print("%0.1f" %mid +"\t", end ="")
print("%0.1f" %final +"\t", end ="")
print()
print("%28s" %"Weighted Assignment/exams:\t" , end = "")
print("%0.1f" %wghtAssgn +"\t", end ="")
print("%0.1f" %wghtExam + "\t", end ="")
print()
print("%28s" %"Term grade point:\t", end ="")
print("%0.1f" %termGPA +"\t", end ="")
