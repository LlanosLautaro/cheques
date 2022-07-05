import pandas as pd
from datetime import datetime
dt = datetime.now()

df = pd.read_csv("cheques.csv")

df['FechaPago'] = pd.to_datetime(df['FechaPago'], format="%d/%m/%Y")

UserDni = int(input("Ingrese su DNI: "))
insertarTipo = input("Ingrese el tipo de cheque (EMITIDO o DEPOSITADO): ").upper()

FiltroFino = input("¿Desea filtrar por estado del cheque y un rango de fecha de emision? (SI/NO): ").upper()

if FiltroFino == "SI":
  FechaMin = input("Ingrese una fecha de pago minima dd/mm/aa: ")
  FechaMinima = datetime.strptime(FechaMin, '%d/%m/%Y')
  
  FechaMax = input("Ingrese una fecha de pago maxima dd/mm/aa: ")
  FechaMaxima = datetime.strptime(FechaMax, '%d/%m/%Y')
  
  insertarEstado = input("Ingrese el estado del cheque (PENDIENTE, RECHZADO o APROBADO): ").upper()
  
  datos = df[(df["DNI"] == (UserDni)) & (df["Tipo"].str.contains(insertarTipo)) & (df["Estado"].str.contains(insertarEstado)) & (df["FechaPago"].isin(pd.date_range(FechaMinima , FechaMaxima)))]
  
elif FiltroFino == "NO":
   datos = df[(df["DNI"] == (UserDni)) & (df["Tipo"].str.contains(insertarTipo))]

salida = input("Ingrese el formato de visualizacion de datos(PANTALLA o CSV): ").upper()
if salida == 'PANTALLA':
  print(datos)
elif salida =='CSV':
  datos.to_csv(f'{UserDni}-{dt}.csv')
  print("Archivo csv creado con exito")

#filas = len(df.index)
#df.drop(df.index[[filas-1]],inplace = True)

  
#datos[df.duplicated(keep=False)]
