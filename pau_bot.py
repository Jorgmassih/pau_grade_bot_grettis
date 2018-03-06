import datetime

def login(user):
    if user.isdigit():
        if int(l[0:4]) >= 1962 and len(l)==8 and datetime.datetime.now().year >= int(l[0:4]):
            return "aquivaelcodigosiguiente"
        else:
            return ("Matrícula invalida")
    else:
        return ("Ingrese una matricula valida")
def files_manager(exercises='result', u_exercise='fofi'):
    with open(exercises + '.csv') as csvfile:
        c_exercise = []
        channel = csvfile.readlines()
        for line in channel:
            if line[0].isnumeric(): c_exercise.append(line.split(","))
        print(c_exercise)

    with open(u_exercise + '.csv') as csvfile:
        user_exercise = []
        channel = csvfile.readlines()
        for line in channel:
            if line[0].isnumeric(): user_exercise.append(line.split(","))
        print(user_exercise)

    test = True
    for element in c_exercise:
        for element_2 in user_exercise:
            if element[3] == 'https://www.codewars.com/kata/' + element_2[2]:
                test = False
                if datetime.datetime.strptime(element_2[4][0:8], '%m/%d/%y') <= datetime.datetime.strptime(element[1], '%m/%d/%y'): print(True)
                else: print(False)
        if test == True: print("no hecho")
print(files_manager())
