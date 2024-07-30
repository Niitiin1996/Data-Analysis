import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import math
import statistics

#SSE
def sse(cp,fit_cp):
	sum=0
	for i in range(0,len(cp)-1):
		error=cp[i]-fit_cp[i]
		sum=sum+pow(error,2)
	return sum

#R-SQUARE
def r_square(cp,fit_cp,sse):
	sum=0
	for i in range(0,len(cp)-1):
		error=fit_cp[i]-statistics.mean(cp)
		sum=sum+pow(error,2)
	sst=sum+sse
	return sum/sst

def adjacentR(r2,n,k):
	ar=1-((1-r2)*(n-1)/(n-k-1))
	return ar

def rsme(sse,n):
	rsme=pow(sse/n,1/2)
	return rsme





# The second step Curve fit function

def cfunc1(t, a, b, c, d):
	return a*pow(t,3)+ b*pow(t,2) + c*t +d


#Newton Raphson method
def fun(e,d,Re,x):
	r= -2*np.log10(e/d/3.7+2.51*x/Re)-x
	return(r)


def df(e, d, Re, x):
	return -2*math.pow((e/d/3.7+2.51*x/Re)*math.log(10),-1)*2.51/Re-1

def friction_factor(e, d, Re):
	fg=4
	al=1.2
	tol=1e-5
	while( abs(fun(e,d,Re,fg))>tol):
		fg=fg-al*fun(e,d,Re,fg)/df(e,d,Re,fg)

	return 1/(fg*fg)


# pressure2 is for laminar and turbulent flow
def pressure2(L,De,q=[]):

	v=[]
	for l in q:
		v.append(l*4*7/22/math.pow(De,2))
	vis= 1.81*math.pow(10,-5) #kg/ms
	Re=[]
	f=[] #Friction factor
	p1=[]
	
	for i in v:
		Re.append(1.2*De/vis*i)

	for j in Re:

		if (j<2300):# laminar flow
			c=64/j
			f.append(c)
		else:
			c= friction_factor(e, De, j) #turbulent flow
			f.append(c)
	for k in v:
		p1.append(c*L*math.pow(k,2)/De/2*1.225)
	return p1

#Main Function

#INITIAL FACTORS
col1 = []
i=0
e=0
q=np.linspace(5,25,50) #Flow-rate
# Calculation for Coefficient of Minor losses 
r=0.125 #1. curved radius at inlet (metre)
l=1     #2. Length at inlet (metre)
b=1     #3. bredth at inlet (metre)
l2=1.6  #4. Length at outlet (metre)
b2=2.4  #5. breadth at outlet (metrw)
le=(l+l2)/2 #Equivalent length 
be=(b+b2)/2 #Equivalent breadth
a1=1        # Area of duct inlet cross-section (metre2)
a2=2.4*1.6  # Area of duct outlet cross-section (metre2)
L1=3.25     # 6. Lenght of 1m2 cross-section (metre)
L2=3.75     # 7. Lenght of (2.4*1.6)m2 cross-section (metre)




# 1. For Loss in entry

D=2*l*b/(l+b)
for line in open('data.txt'):
	if '#' not in line:
		values= np.array(line.split(','))
		if(float(values[0])>=(r/D)):
			k1=float (np.array(values[1]))

			break
print('1.)   K1=',k1)



# 2. For Loss in obstructions
#Obstruction Dimension
a=0.5*0.01
#Let the fluid be 90% contracted by vena-contracta i.e. Cc=0.9 
k2=math.pow(a1/((a1-a)*0.9)-1,2)
print('2.)   K2= ',k2)



# 3. Coefficient For loss at outlet

k0=1  #but that is for the velocity at outlet and not the velocity at inlet
k3=math.pow(a1/a2,2)
print('3.)   K3= ',k3)


# 4. Loss in Duct Diffuser
#Kdiffuser= 1- (a1/a5)^2-Cp
# Dimensionless length = N/R1
#Equivalent diameter= 1.265*l^0.6*b^0.6/(a+b)^0.2

De1= 1.265*math.pow(l*b,0.6)/math.pow(l+b,0.2)

DL= L2/De1

# From Graph the value of Cp is calculated 
Cp=0.45
k4= 1- math.pow(a1/a2,2)- Cp
print("4.)   k4= ",k4)

#Minor loss
p0=[]
k=k1+k2+k4+k3
print("Total Loss Coefficient, k=",k)
p0=pressure2(k,De1,q)
print("Pressure Minor Loss.....",'\n',p0)


#5. Friction in ducts 
#5(A) For Friction in straight test section
# change in pressure= 32*L*vis*v/(d^2), where 32*L*vis/d^2 is constant 

De2= 1.265*math.pow(le*be,0.6)/math.pow(le+be,0.2)

p1=[]
p2=[]

p1=pressure2(L1,De1,q)
print("Pressure1.....",'\n',p1)
p2=pressure2(L2,De2,q)
print("Pressure2.....",'\n',p2)

p3=[]
i=0
for i in range(0,len(p1)):
	p3.append(p1[i]+p2[i]+p0[i]+1) # An addition loss of pressure in bolts in ducts
print("Total Pressure Loss",'\n',p3)

#Plotting Graph Pressure vs Flow-Rate
plt.plot(p3, q,color="blue",linewidth=3)
plt.xlabel('Flow-Rate(m^3/s)')
plt.ylabel('Pressure (Pa)')

# Curve Fitting
popt1, pcov1= curve_fit(cfunc1,p3,q)

fit_cp1= cfunc1(np.array(p3),*popt1)

print("Optimal Values of Constants in Equation::  ",*popt1)

# Evaluation of Goodness of Fit
number= len(q)
print('Evaluation of goodness of fit')
sse=sse(q,fit_cp1)
print('SSE =',sse)
r_square=r_square(q,fit_cp1,sse)
print('r-square=',r_square)
ar=adjacentR(r_square,number,1)
print('Adjacent R-SQUARE=',ar)
rsme=rsme(sse,number)
print('RSME=',rsme)

if (r_square>0.65):

	plt.plot(p3, fit_cp1,color="black",linewidth=3)
	plt.show()
else:
	print(" Try Again with equation Assumption")

#T H E   E N D


