zonas = int(input())
cant_ant_insta=0
rango_anti= 36900

tipo_a = 0
tipo_b = 0
tipo_c = 0
tipo_d = 0
tipo_e = 0
total_antenas= 0

for i in range(zonas):
    area=float(input())
    cantidad=int(input())
    type=str(input())
    if type == "a":
        tipo = 44600
    elif type == "b":
        tipo = 51800
    elif type == "c":
        tipo = 9600
    elif type == "d":
        tipo = 15300
    elif type== "e":
        tipo = 13900
    else:
        tipo = 0

    if(cantidad < 1 or area < cantidad*rango_anti):
        antenas = 0
    else:
        antenas= (area-(cantidad*rango_anti))/tipo
        if antenas % 1 > 0:
            antenas = (antenas//1) + 1
    
    if type == "a":
        tipo_a += antenas
    elif type == "b":
        tipo_b += antenas
    elif type == "c":
        tipo_c += antenas
    elif type == "d":
        tipo_d += antenas
    else:
        tipo_e += antenas

    total_antenas+= antenas
#Total de antenas 
print(int(total_antenas))
#Porcentaje por tipo de antenas
if(tipo_a == 0):
    print("a 0.00%")
else:
    result=(100/(total_antenas/tipo_a))
    result = round(result, 2)
    if((result % 1)/10!=0):
        print("a ","{}%".format(result))
    else:
        print("a {}0%".format(result))
if(tipo_b == 0):
    print("b 0.00%")
else:
    result=(100/(total_antenas/tipo_b))
    result = round(result, 2)
    if((result % 1)/10!=0):
        print("b ","{}%".format(result))
    else:
        print("b {}0%".format(result))
if(tipo_c == 0):
    print("c 0.00%")
else:
    result=(100/(total_antenas/tipo_c))
    result = round(result, 2)
    if((result % 1)/10!=0):
        print("c ","{}%".format(result))
    else:
        print("c {}0%".format(result))
if(tipo_d == 0):
    print("d 0.00%")
else:
    result=(100/(total_antenas/tipo_d))
    result = round(result, 2)
    if((result % 1)/10!=0):
        print("d ","{}%".format(result))
    else:
        print("d {}0%".format(result))
if(tipo_e == 0):
    print("e 0.00%")
else:
    result=(100/(total_antenas/tipo_e))
    result = round(result, 2)
    if((result % 1)/10!=0):
        print("e ","{}%".format(result))
    else:
        print("e {}0%".format(result))


