import matplotlib.pyplot as plt
from numpy import trapz
import math


#For calculation of area using rectangular strip method
def area (y, x):
	a=0.0

	#Graphical Strip Method

	for i in range(0,len(x)-1):
		
		b=y[i]
		l=x[i+1]-x[i]
		a=a+b*l

	return (a)



#Function to be used to input the values of columns
def Input():
	col_1=1
	col_2=5
	return col_1,col_2

#If file doesnot open , FILE ISN'T RECOGANIZED i.e. Compatibility Test
try:
    with open('engine_data.out') as file:
        read_data = file.read()
except:
   print('File not recognized. Please provide a valid CONVERGE output file')
   exit()

#String containing headings of the Columns.
str=['crank_angle','pressure','Max_pre','Min_pre','Mean_Temp','Max_Temp','Min_Temp','Volume','Mass','Density','Integrated_HR','HR_Rate','C_P','C_V','Gamma','Kyn_Visc','Dyn_Visc']
p=1
col1=[]
col2=[]
column1, column2=Input() #Input of no. of columns to be taken as INPUT

for line in open('engine_data.out'):
	if '#' not in line:
		
		col1.append(float(line.split()[column1-1]))
		col2.append(float(line.split()[column2-1]))
plt.plot(col2,col1)

#For automatic label information....
plt.ylabel(str[column2-1])
plt.xlabel(str[column1-1])
plt.show()


crank_angle=[]
pressure=[]
Max_pre=[]
Min_pre=[]
Mean_Temp=[]
Max_Temp=[]
Min_Temp=[]
Volume=[]
Mass=[]
Density=[]
Integrated_HR=[]
HR_Rate=[]
C_P=[]
C_V=[]
Gamma=[]
Kyn_Visc=[]
Dyn_Visc=[]

#To save each file with the name of the column...
for line in open('engine_data.out'):
	if '#' not in line:
		crank_angle.append(float(line.split()[0]))
		pressure.append(float(line.split()[1]))
		Max_pre.append(float(line.split()[2]))
		Min_pre.append(float(line.split()[3]))
		Mean_Temp.append(float(line.split()[4]))
		Max_Temp.append(float(line.split()[5]))
		Min_Temp.append(float(line.split()[6]))
		Volume.append(float(line.split()[7]))
		Mass.append(float(line.split()[8]))
		Density.append(float(line.split()[9]))
		Integrated_HR.append(float(line.split()[10]))
		HR_Rate.append(float(line.split()[11]))
		C_P.append(float(line.split()[12]))
		C_V.append(float(line.split()[13]))
		Gamma.append(float(line.split()[14]))
		Kyn_Visc.append(float(line.split()[15]))
		Dyn_Visc.append(float(line.split()[16]))
		

plt.plot(Volume,pressure)
plt.xlabel('Volume')
plt.ylabel('Pressure')
plt.show()
area=abs(area(pressure,Volume))
print('Work Done using graphical strip method',area*pow(10,6),'J')

area=abs(trapz(pressure,Volume))


print('Work Done using Trapezoidal method',area*pow(10,6),'J')
N=1500/60  #rps
power=area*N*pow(10,3)/2 #for four stroke engine
print('The power output of the engine', power,'KW')

mass=20
sfc=float(20/abs(area)/math.pow(10,9))
print('The specific fuel consumption =', sfc*3600,'kg/W.hr')