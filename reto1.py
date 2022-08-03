
ante_anti = 36900
a = 44600
b = 51800
c = 9600
d = 15300
e = 13900

area = float(input())
ant_inst= int(input())
ant_new= input()

if ant_inst<0:
    print("error en los datos")
else:
    print()

alcance_total= ant_inst*ante_anti

if area<alcance_total:
  print("0")
elif area>alcance_total:
  if ant_new == "a":
    print(round((area-alcance_total)/a))
  elif ant_new == "b":
    print(round((area-alcance_total)/b))
  elif ant_new == "c":
    print(round((area-alcance_total)/c)) 
  elif ant_new == "d":
    print(round((area-alcance_total)/d))
  elif ant_new == "e":
    print(round((area-alcance_total)/e))   