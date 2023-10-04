# Tarea para diseño de equipos

import math

#Problema

propiedades_fluidos = {
    "Cp":{
        "H2O":0.99,
        "Aceite":0.629,
        "unit":"BTU/(lb*°F)"
        },
    "SG":{
        "H2O":0.95,
        "Aceite":0.755,
        "unit":"0"
        },
    "k":{
        "H2O":0.365,
        "Aceite":0.065,
        "unit":"0"
        },
    "mu":{
        "H2O":0.365,
        "Aceite":0.065,
        "unit":"0"
        },
    "Rd":{
        "H2O":0.365,
        "Aceite":0.065,
        "unit":"0"
        },
    "Pop":{
        "H2O":0.365,
        "Aceite":0.065,
        "unit":"0"
        }
    }
temps = {
    "T2":150,
    "T1":250,
    "t1":67,
    "t2":115}
Flujos = {"H2O":0,
          "Aceite":500000
          }
Q = Flujos["Aceite"]*propiedades_fluidos["Cp"]["Aceite"]*(temps["T1"]-temps["T2"])
print(Q)

Flujos["H2O"] = Q/(propiedades_fluidos["Cp"]["H2O"]*(temps["t2"]-temps["t1"]))
print(Flujos["H2O"])
##            |
##   _________v
##->|          |->
##   |----------
##   V
   
# Calculamos la temperatura media logaritmica
# Contracorriente
dTML = ((temps["T1"]-temps["t2"])-(temps["T2"]-temps["t1"]))/(math.log((temps["T1"]-temps["t2"])/(temps["T2"]-temps["t1"])))
print(dTML)
