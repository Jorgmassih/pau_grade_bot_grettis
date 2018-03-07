import datetime

def login(user):
    if user.isdigit():
        if int(l[0:4]) >= 1962 and len(l)==8 and datetime.datetime.now().year >= int(l[0:4]):
            return "aquivaelcodigosiguiente"
        else:
            return ("Matrícula invalida")
    else:
        return ("Ingrese una matricula valida")

def print_in_csv(id, text):
    with open(id + "_summary" + ".csv", "a+") as generatedcsv:
        return generatedcsv.write(text + "\n")


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

    test = False
    id = "2016-5459"
    for element in c_exercise:
        for element_2 in user_exercise:
            if element[3] == 'https://www.codewars.com/kata/' + element_2[2]:
                test = True
                if datetime.datetime.strptime(element_2[4][0:8], '%m/%d/%y') <= datetime.datetime.strptime(element[1], '%m/%d/%y'):
                    status = "{},{},{},{},{}".format(element[0], element_2[2], True, element_2[4][:8], True)
                    print(status)
                    print_in_csv(id, status)
                else:
                    status = "{},{},{},{},{}".format(element[0], element_2[2], True, element_2[4][:8], False)
                    print(status)
                    print_in_csv(id, status)

        if test == False:
            status = "{},{},{},{},{}".format(element[0], element[3][30:], False, 'None', 'None')
            print(status)
            print_in_csv(id, status)
    return ""


print(files_manager())
