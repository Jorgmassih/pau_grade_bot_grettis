import datetime
import os.path

def login(id):
    if id.isdigit() and int(id[0:4]) >= 1962 and len(id)==8 and datetime.datetime.now().year >= int(id[0:4]):
        return True
    else: return False

def files_manager(id):
    with open('codewars.csv') as csvfile:
        c_exercise = []
        channel = csvfile.readlines()
        for line in channel:
            if line[0].isnumeric(): c_exercise.append(line.split(","))
        # print(c_exercise)

    with open('exercises.csv') as csvfile:
        user_exercise = []
        channel = csvfile.readlines()
        for line in channel:
            if line[0].isnumeric(): user_exercise.append(line.split(","))
        # print(user_exercise)

    test = False


    for element in c_exercise:
        for element_2 in user_exercise:
            if element[3] == 'https://www.codewars.com/kata/' + element_2[2]:
                test = True
                if datetime.datetime.strptime(element_2[4][0:8], '%m/%d/%y') <= datetime.datetime.strptime(element[1], '%m/%d/%y'):
                    status = "{},{},{},{},{}".format(element[0], element_2[2], True, element_2[4][:8], False)
                    print(status)
                    print_in_csv(id, status)
                else:
                    status = "{},{},{},{},{}".format(element[0], element_2[2], True, element_2[4][:8], True)
                    print(status)
                    print_in_csv(id, status)

        if test == False:
            status = "{},{},{},{},{}".format(element[0], element[3][30:], False, 'None', 'None')
            print(status)
            print_in_csv(id, status)
    return ""

def print_in_csv(id, text):
    with open('processed.csv', "a+") as generatedcsv:
        return generatedcsv.write(text + "\n")

def found_file_test(id_test):
  file = id_test + '.csv'
  if os.path.exists(file): return True
  else: return False

def summary(id):
    with open('processed.csv') as csvfile:
        list = []
        channel = csvfile.readlines()
        for line in channel:
            list.append(line.split(","))

    count = 0
    elements = 0
    for element in list:
        elements+=1
        if element[4][:4] == "True": count+=1

    print("""
StudentId: {}
TotalExcercises: {}        
TotalCompleted: {}
TotalLate: {}
TotalMissing: {}
    """.format(id, 37, len(list), count, 37-len(list)))


option = input("""Seleccione una opcion:
1. Login
2. Exit
""")

while True:
    if option == "1":
        while True:
            input_ = input("Ingrese su matricula: ")
            if login(input_) == True:
                break
            else:
                print("Matricula incorrecta, inserte un ID válido.\n")

        while True:
            option_2 = input("""
Seleccione una funcion
1. Codewars
2. Summary
3. Back
            """)
            if option_2 == "1":
                print(files_manager(input_))

            if option_2 == "2": summary(input_)

            if option_2 == "3": break


    if option == "2": break
