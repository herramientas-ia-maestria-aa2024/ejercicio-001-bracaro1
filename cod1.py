file=open('/home/vboxuser/Descargas/informacion.txt')
line=file.readline()
while (line!=''):
    datos=line.split(';')
    print (datos[0],'\t\t',datos[1],'\t',datos[2],'\t',datos[3],end='\n')
    line=file.readline()
