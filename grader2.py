#studentInfo
#name = Aiman Nawar Chowdhury
#Version: 03 Oct, 2022.
#Learning objective:
#Defining and using named constants, use of Branching and Looping.

#F1
min_Gp = 0
max_Gp = 4.3

#F2
Grd1 = "F"
Grd2 = "D"
Grd3 = "D+"
Grd4 = "C-"
Grd5 = "C"
Grd6 = "C+"
Grd7 = "B-"
Grd8 = "B"
Grd9 = "B+"
Grd10 = "A-"
Grd11 = "A"
Grd12 = "A+"

#F3
print("*\aTerm GPA CAN ONLY RANGE FROM 0 TO 4.3!*")
print()
print()
TGPA = float(input("Enter Term GPA: "))
while((TGPA < min_Gp)or(TGPA > max_Gp)):
    TGPA = float(input("Enter Term GPA: "))
#F4
if((TGPA >= 0) and (TGPA < 0.85)):
    TLG = Grd1
if((TGPA >= 0.85) and (TGPA <1.15)):
    TLG = Grd2
if((TGPA >= 1.15) and (TGPA <1.50)):
    TLG = Grd3
if((TGPA >= 1.50) and (TGPA <1.85)):
    TLG = Grd4
if((TGPA >= 1.85) and (TGPA <2.15)):
    TLG = Grd5
if((TGPA >= 2.15) and (TGPA <2.50)):
    TLG = Grd6
if((TGPA >= 2.50) and (TGPA <2.85)):
    TLG = Grd7
if((TGPA >= 2.85) and (TGPA <3.15)):
    TLG = Grd8
if((TGPA >= 3.15) and (TGPA <3.50)):
    TLG = Grd9
if((TGPA >= 3.50) and (TGPA <3.85)):
    TLG = Grd10
if((TGPA >= 3.85) and (TGPA <4.06)):
    TLG = Grd11
if(TGPA >= 4.06):
    TLG = Grd12
#F5
print(("%s" %"Term GPA: "), end = "")
print(("%0.1f" %TGPA) + "\t", end = "")
print(("%s" %"Term Letter: "), end = "")
print(("%s" %TLG))



    

