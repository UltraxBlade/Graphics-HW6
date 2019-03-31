from Graphics import *
from matrix import *
from display import *

homeTest=False

def parse(filename,edges,polys,transform,img,color):
    f=open(filename,"r")
    script=f.read().split("\n")
    f.close()
    i=0
    while i<len(script):
        if script[i]=="line":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            addEdge(edges,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])
            i+=1
        elif script[i]=="triangle":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            addPoly(polys,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7],coords[8])
            i+=1
        elif script[i]=="ident":
            transform=I(4)
        elif script[i]=="apply":
            edges=multMatrix(transform,edges)
            polys=multMatrix(transform,polys)
        elif script[i]=="quit":
            return
        elif script[i]=="move":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            transform=multMatrix(translate(coords[0],coords[1],coords[2]),transform)
            i+=1
        elif script[i]=="scale":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=float(coords[k])
            transform=multMatrix(scale(coords[0],coords[1],coords[2]),transform)
            i+=1
        elif script[i]=="rotate":
            coords=script[i+1].split(" ")
            transform=multMatrix(rotate(coords[0],float(coords[1])),transform)
            i+=1
        elif script[i]=="save":
            clear(img)
            drawLines(img,edges,color)
            drawPolys(img,polys,color)
            if homeTest:
                save_ppm(img,script[i+1])
            else:
                save_extension(img,script[i+1])
            i+=1
        elif script[i]=="circle":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            circle(edges,coords[0],coords[1],coords[2],coords[3])
            i+=1
        elif script[i]=="hermite":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            hermite(edges,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7])
            i+=1
        elif script[i]=="bezier":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            bezier(edges,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7])
            i+=1
        elif script[i]=="box":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            box(polys,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])
            i+=1
        elif script[i]=="sphere":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            sphere(polys,coords[0],coords[1],coords[2],coords[3])
            i+=1
        elif script[i]=="torus":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            torus(polys,coords[0],coords[1],coords[2],coords[3],coords[4])
            i+=1
        elif script[i]=="clear":
            edges[0]=[]
            edges[1]=[]
            edges[2]=[]
            edges[3]=[]
            polys[0]=[]
            polys[1]=[]
            polys[2]=[]
            polys[3]=[]
        elif script[i]=="display" and not homeTest:
            clear(img)
            drawLines(img,edges,color)
            drawPolys(img,polys,color)
            display(img)
        i+=1

img=generate(501,501)
edges=[[],[],[],[]]
polys=[[],[],[],[]]
transform=I(4)
parse("script",edges,polys,transform,img,[0,0,0])
