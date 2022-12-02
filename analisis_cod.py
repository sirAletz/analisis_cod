import subprocess
import pandas as pd
import colorama
colorama.init()

class bcolors:
    OK = "\033[92m" #GREEN
    WARNING = "\033[93m" #YELLOW
    FAIL = "\033[91m" #RED
    RESET = "\033[0m" #RESET COLOR
    TITLE = "\033[94m" #TITULOS
    LINE = "\033[95m"
    

conexion='open 10.192.2.130'
bin1='bin'
ins="QUOTE RCMD CALL PGM(SEGURIDAD/COPYCOD) PARM('"
simbol="')"
obtener='GET /QSYS.LIB/SEGURIDAD.LIB/SAL_COD.FILE C:\TELSHARE\COMPCOD\COPYCOD.csv'
salir='quit'

usr=input("Ingresa tu usr de QAS: ")
psw=input("Ingresa tu psw de QAS: ")
Folio=input("Ingresa el No del Folio en QAS: ")
f=open(r"C:\TELSHARE\COMPCOD\CMDFTP.txt","w")
f.truncate(0)
f.write(conexion + "\n")
f.write(usr + '\n')
f.write(psw + '\n')
f.write(ins + Folio + simbol + '\n')
f.write(obtener + '\n')
f.write(salir)
f.close()

subprocess.run('C:\TELSHARE\COMPCOD\Run_ftp.bat', shell=True)

print(bcolors.OK + "proceso existoso!!\n" + bcolors.RESET)

getmenu=input("Que menu deseas comparar?\n")
getmgraf=input("Que menu deseas comparar?\n")

frame1=pd.Cov = pd.read_csv(r'C:\TELSHARE\COMPCOD\COPYCOD.csv','r',names=["COD1"])
frame2=pd.read_excel('C:\TELSHARE\COMPCOD\Inventario_de_codigos 2018_11.xlsx')
df_dataframe2 = frame2[frame2.MENU.isin([getmenu,getmgraf])] #& (frame2.MENU == getmgraf)]
frame3=pd.read_excel('C:\TELSHARE\COMPCOD\Cod_esp.xlsx')

bandera='0'
for busca in frame1.values:
    if busca in df_dataframe2.values and busca in frame3.values:
       print(busca + " Código pertenece a menu y REQUIERE AUTORIZACIÓN")
       bandera='1'
    elif busca in df_dataframe2.values and not busca in frame3.values:
       print(busca + " Código pertenece a menu y no especial")
    else:
        print(busca + "Codigo no pertenece a menu")

input("presiona enter para continuar")
if bandera=='1':
   subprocess.Popen(r'C:\TELSHARE\COMPCOD\MENUS_VS_FIRMA _EN_CARPETA_2015.xls', shell=True)


