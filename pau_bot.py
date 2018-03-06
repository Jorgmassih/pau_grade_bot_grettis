import datetime

def login(user):
    if user.isdigit():
        if int(l[0:4]) >= 1962 and len(l)==8 and datetime.datetime.now().year >= int(l[0:4]):
            return "aquivaelcodigosiguiente"
        else:
            return ("Matrícula invalida")
    else:
        return ("Ingrese una matricula valida")
