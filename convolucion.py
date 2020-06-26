import numpy as np
import matplotlib.pylab as plt



archivo = open('datos.txt','r')
#pedir cuantos datos va a tener x(n)
x=archivo.readline()
x_init=archivo.readline()
#pedir cuantos datos va a tener h(n)
h=archivo.readline()
h_init=archivo.readline()
archivo.close()

x_init = int(x_init)
h_init = int(h_init)

#convierte las strings en nnumeros
flag = 0
flag1 = 0
x_n = []
for var in x:
	if(var != ',') :
		if(var != '\n'):
			if(var == '-'):
				flag = 1
			else:
				if(flag == 1):
					var1 = "-"+var
					x_n.append(int(var1))
					flag = 0
				else:
					x_n.append(int(var))

x_n = list(x_n)
x_fin = (x_init+(len(x_n)-1))
print("x(n) = ",x_n,"inicia en: ",x_init,"termina en:",x_fin)

flag = 0
h_n = []
for var in h:
	if(var != ',') :
		if(var != '\n'):
			if(var == '-'):
				flag = 1
			else:
				if(flag == 1):
					var1 = "-"+var
					h_n.append(int(var1))
					flag = 0
				else:
					h_n.append(int(var))

h_n = list(h_n)
h_fin = (h_init+(len(h_n)-1))
print("h(n) = ",h_n,"inicia en: ",h_init,"termina en:",h_fin)

#Aqui invierte h(n) para volverlo h(-k)
h_x=[]

i=h_init
while(i <= h_fin):
	h_x.append(i)
	i+=1

x_x=[]

i=x_init
while(i <= x_fin):
	x_x.append(i)
	i+=1

h_kInvert = h_n

h_kInvert.reverse()

print("h(k) invertido = ",h_kInvert)	
h_x.reverse()
num_h = len(h_x)
i=0
while(i<num_h):
	h_x[i] = h_x[i]*(-1)
	i+=1
print("\n")

plt.figure(1)
plt.bar(x_x,x_n)
plt.suptitle('x(k)')
plt.figure(2)
plt.bar(h_x,h_kInvert)
plt.suptitle('h(k) Invertida')


y_n = []
n=-10
n_fin=10

#Aqui se mutliplica cada h(n-k) con x(k)
while(n <= n_fin):
	i = 0
	h_k = h_x.copy()
	y = 0
	while(i < len(h_k)):
		h_k[i] = h_k[i] + n
		i += 1
	print("h(",n,"- k) = ",h_k)
	#se suman los resultados de cada n
	flag_z = 0
	for x in x_x:
		for h in h_k:
			if(x == h):
				n_x = x_x.index(x)
				n_h = h_k.index(h)
				y += (x_n[n_x]*h_kInvert[n_h])
				flag_z+=1
	if(flag_z==0):
		y_n.append(0)
	else:
		y_n.append(y)
	n+=1
print("\ny(n) va de -10 a 10")
print("y(n) = ",y_n)
y_N = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

plt.figure(3)
plt.bar(y_N,y_n)
plt.suptitle("y(n)")
plt.show()
print("Oprima cualquier tecla para salir")
input()


