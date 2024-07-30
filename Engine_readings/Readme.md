## Objective: To read the file 'engine_data.out' and perform the following operations on the data.

1.) Data Visualizer

2.) Compatability Check

3.) Basic Performance Calculation

# Concept: 
The basic concept is to read the file 'engine_data.out' and perform several functions on it. As Sublime doesn't allow you to input the data, It is better to define a function Input(), to input the column numbers . I have taken the example of Columns nos. 1 & 5. To perform a compatibility check, the try and except block: is to be used, as it is used for Python exceptions i.e. it will display the command 'File not recognized. Please provide a valid CONVERGE output file', if it fails to open. The next task will be to calculate the engine's basic performance calculations i.e. 

a) Area under a P-V diagram

There are many ways to complete this task. I have done it by using two of the ways that are best to my knowledge. 

1. The first way is the rectangular strip method. In this method, the area is divided into small rectangular strips and then the area of each strip is then calculated and added.

2. The second way is to use the trapezoidal method, in which the area is divided into trapezoids and then their sum calculates the total area. This method is more accurate than the previous one. There is a function in numpy module named as trapz(y,x) which can be used to calculate the area in this problem.

b) Power output of the engine

Power output for the 4-stroke engine is given as, 

Power = Work done * RPM/2 (Joules)

c) Specific Fuel Consumption

sfc = Area/ Work Done 

# Methodology: 
Let us go task by task in solving this assignment: 

1. The first task is to enter column numbers as input. As sublime doesn't offer input to the user, therefore, instead of using sublimeREPL as it may result in slowing of program building, a separate function is to be used, namely Input().

2. Now coming to the main part, the first operation a program should perform is Compatibility check, i.e. the program should check whether the file is compatible or not. This is done by using the try and except block: as explained above.

3. Now the next part will be to define a string that contains all the names of each of the headings in the data so that the names can be automatically retrieved, and then the input function is called for values of columns. 

4. The next step is to save each column's values under its name i.e. each list should be named after its values. This is done as follows:

 5. The last step will be to plot the pressure vs Volume graph. This is done by two methods first by defining a function called area(y,x) where y-pressure and x- volume, and this function uses the graphical strip method. 

The second method is using trapezoidal method. There is a function in numpy module named as trapz(y,x) which can be used to calculate the area in this problem.

In the end all three factors i.e. Work Done, Power, and Specific fuel consumption are calculated.
