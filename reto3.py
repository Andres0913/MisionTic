def auxi():
    Aux=[]
    Nsucursal,Sistolica,Diastolica=map(int,input().split())
    Aux.append(Nsucursal)
    Aux.append(Sistolica)
    Aux.append(Diastolica)
    return (Aux)

n=0 #n es cantidad de sucursales
while n<1:    
    entrada = input()
    lista = entrada.split(' ')
    n = int(lista[0])
    m = int(lista[1])
Sucursales=[]
Pacientes=[]
for x in range(n):
    valor=int(input())
    if valor!=0:
        Sucursales.append(valor)

Nsucursal=0
Sistolica=0
Diastolica=0
SucursalOriginal=Sucursales.copy()
for x in range(m):
    retorno=auxi()
    Pacientes.insert(x,retorno)

#Entrega de medicamentos  
for x in range(m):
    Sistolic=Pacientes[x][1]
    Diastolic=Pacientes[x][2]
    NumSucursa= Pacientes[x][0]-1
    Cantidad=Sucursales[NumSucursa]
    if Sistolic < 75 and Diastolic<55:
        Sucursales[NumSucursa]=Cantidad-7

    elif Sistolic>=75 and Sistolic< 115 and Diastolic >=55 and Diastolic<75:
        Sucursales[NumSucursa]=Cantidad-0
    elif Sistolic>=115 and Sistolic< 125 and Diastolic >=75 and Diastolic<80:
        Sucursales[NumSucursa]=Cantidad-0
    elif Sistolic>=125 and Sistolic< 135 and Diastolic >=80 and Diastolic<85:
        Sucursales[NumSucursa]=Cantidad-1
    elif Sistolic>=135 and Sistolic< 155 and Diastolic >=85 and Diastolic<95:
        Sucursales[NumSucursa]=Cantidad-7
    elif Sistolic>=155 and Sistolic< 175 and Diastolic >=95 and Diastolic<105:
        Sucursales[NumSucursa]=Cantidad-15
    elif Sistolic>=175 and Diastolic >=105:
        Sucursales[NumSucursa]=Cantidad-30
    elif Sistolic>=135 and Diastolic <85:
        Sucursales[NumSucursa]=Cantidad-15


#Sucursal con menor cantidad
posmenor=0
menor=Sucursales[0]
for x in range(n):
    if Sucursales[x]<menor:
        menor=Sucursales[x]
        posmenor=x
print(f"{posmenor+1} {menor}")

#Sucursal con mayor cantidad
mayor=Sucursales[0]
posmayor=0
for x in range(n):
    if Sucursales[x]>mayor:
        mayor=Sucursales[x]
        posmayor=x
print(f"{posmayor+1} {mayor}")

#Porcentajes
for x in range(n):
    porcentaje=((SucursalOriginal[x]-Sucursales[x])*100)/SucursalOriginal[x]
    print (x+1,end="")
    print(" {:.2f}%".format(porcentaje))