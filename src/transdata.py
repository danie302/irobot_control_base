import numpy as np 
import math

with open('map.txt', 'r') as f:
    m = f.readlines()
    mapa = m[0].split(')')[0].split('(')[1].split(",")
    for i in range(len(mapa)):
        mapa[i] = int(mapa[i])
    mapa = tuple(mapa)

width= 192
height=192
datayes=[100, 0]
setdata=set(datayes)

print ("numero de datos en data", len(mapa))

move=0
maparev= mapa[::-1] 
mapp=np.empty((width,height))
mappreverse=np.empty((width,height))
mappdown=np.empty((width,height))

for i in range (height):
    for y in range (width):
        mapp[i,y]=mapa[move]
        mappreverse[i,y]=maparev[move]
        move=move+1

inicio=len(mapa)-1
np.savetxt("transdata192.txt",mapp,fmt="%s")
np.savetxt("transdatarev192.txt",mappreverse,fmt="%s")

move=0
for i in range (height): #para eliminar las filas que solo tienen -1
    print("move",move)
    setmapp=set(mappreverse[move,:])
    if len(setdata.intersection(setmapp)) > 0:
        move=move+1
        print("fila BUENA",mappreverse[move,:])
        print("fila buena, next")
    else: #eliminar fila
        print("elimino la fila de move",move)
        print("fila eliminada",mappreverse[move,:])
        mappreverse= np.delete(mappreverse,move,axis=0)
move=0
for i in range (width): #para eliminar las columna que solo tienen -1
    print("move",move,"lenmapp",len(mappreverse))
    setmapp=set(mappreverse[:,move])
    print("condicion",len(setdata.intersection(setmapp)))
    if len(setdata.intersection(setmapp)) > 0:
        move=move+1
        print("columna BUENA",mappreverse[move,:])
        print("columna buena, next")
    else: #eliminar columna
        print("elimino la columna de move",move)
        mappreverse= np.delete(mappreverse,move,axis=1)


np.savetxt("newtransdatarev192.txt",mappreverse,fmt="%s")

newheight=len(mappreverse[:,1])
newwidth=len(mappreverse[1,:])

# Eliminar espacios vacios en el mapa
for i in range (newheight):
    for y in range (newwidth):
        if ((y>0 and y<newwidth-1) and mappreverse[i,y]==-1 and (mappreverse[i,y-1]==0 or mappreverse[i,y+1]==0)):
            mappreverse[i,y]=0
        print("i ",i,"y ",y,"newwidth ",newwidth,"newheight ",newheight)
        if ((y>0 and y<(newwidth-4)) and mappreverse[i,y]==-1 and mappreverse[i,y+1]==-1 and (mappreverse[i,y+2]==0 or mappreverse[i,y-1]==0)):
            mappreverse[i,y]=0
robotStart = 0
# Posicion inicial del robot 4x4
for i in range (newheight):
    if(robotStart != 0):
        break
    for y in range (newwidth):
        if ((y>0 and y<newwidth-4) and mappreverse[i,y]==0 and (mappreverse[i,y+1]==0 and mappreverse[i,y+2]==0 and mappreverse[i,y+3]==0)):
            if((i>0 and i<newheight-4) and mappreverse[i,y]==0 and (mappreverse[i+1,y]==0 and mappreverse[i+2,y]==0 and mappreverse[i+3,y]==0)):
                robotStart = (i,y)
                for x in range(0,4):
                    for h in range(0,4):
                        mappreverse[i+x,y+h]=20
        if(robotStart  != 0):
            break
                
# Meta 13,10
for x in range(13,17):
    for h in range(10,14):
        mappreverse[x,h]=40

print robotStart
np.savetxt("transdatacut192.txt",mappreverse,fmt="%s")
