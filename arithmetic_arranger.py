import regex as re

def arithmetic_arranger(problems,solution=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    result=[]
    for item in problems:
        item=item.replace(" ","")
        if re.search("\+",item)!=None:
            number1=item.split("+")[0]
            number2=item.split("+")[1]
            operator="+"
            try:
                resultado=int(number1)+int(number2)
            except:
                return("Error: Numbers must only contain digits.")
                break
            result.append([number1,operator,number2,resultado])
        if re.search("\-",item)!=None:
            number1=item.split("-")[0]
            number2=item.split("-")[1]
            operator="-"
            try:
                resultado=int(number1)-int(number2)
            except:
                return("Error: Numbers must only contain digits.")
            result.append([number1,operator,number2,resultado])
        if re.search("\*",item)!=None:
            return("Error: Operator must be '+' or '-'.")
            break
        if re.search("\/",item)!=None:
            return("Error: Operator must be '+' or '-'.")
            break
    for number in result:
      if len(number[0])>4 or len(number[2])>4:
        return("Error: Numbers cannot be more than four digits.")
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    for a,number in enumerate(result): 
        if a==(len(result)-1):
            greater = len(number[0]) if len(number[0]) > len(number[2]) else len(number[2])
            first_line += " " * (greater - len(number[0]) + 2) + number[0]
            second_line += number[1] + " " * (greater - len(number[2]) + 1) + number[2]
            for i in range(greater + 2) : third_line += "-"
            fourth_line += " "*(greater + 2 - len(str(number[3]))) + str(number[3])
        else:
            greater = len(number[0]) if len(number[0]) > len(number[2]) else len(number[2])
            first_line += " " * (greater - len(number[0]) + 2) + number[0] + " "*4
            second_line += number[1] + " " * (greater - len(number[2]) + 1) + number[2] + " "*4
            for i in range(greater + 2) : third_line += "-"
            third_line += " "*4
            fourth_line += " "*(greater + 2 - len(str(number[3]))) + str(number[3]) + " " * 4
    if solution:
        return first_line + "\n" +second_line+ "\n" + third_line + "\n" + fourth_line
    else:  
        return first_line + "\n" +second_line+ "\n" + third_line
