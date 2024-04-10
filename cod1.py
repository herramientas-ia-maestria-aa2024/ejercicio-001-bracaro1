arc=open('/home/vboxuser/Descargas/informacion.txt')
li=arc.readlines()
for linea in li:
  print (linea)

file=open('C:/Users/byron.acaro/Downloads/informacion.txt')
line=file.readline()
name_colum=line.split(';')
print(name_colum[0],name_colum[1],name_colum[2],name_colum[3],sep='\t')
while (line!=''):
    datos=line.split(';')
    print (datos[0],datos[1],datos[2],datos[3],sep='\t')
    line=file.readline()
