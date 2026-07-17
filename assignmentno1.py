import numpy as np
# 1D array
x=np.array([1,2,3,4,5],dtype=np.int64)
print(x)
print()
#2d array
y=np.array([[1,2,3,4,4],[1,4,6,7,2]],dtype=np.int64)
print(y)
print()
#3d array
z=np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]],dtype=np.int64)
print(z)

#array of zeros
a=np.zeros((2,3))
print("array of zeros",a)
#arraoy of ones
b=np.ones((2,3))
print("Array of ones",b)
#identity matrix
c=np.eye(3)
print("Identity matrix",c)
#arrange the array
d=np.arange(0,10,2)
print("even numbers",d)
#liespace 
e=np.linspace(0,1,5)
print("linespace",e)

#math functions
f=np.array([[1,3,5,7],[4,8,7,9]])
print("shape",f.shape)
print("size",f.size)
g=np.array([[1,2,3,4],[5,6,7,8]])
joon=np.concatenate((f,g))
print("join array",joon)
v_stack=np.vstack((f,g))
h_stack=np.hstack((f,g))
print("vertical stack",v_stack)
print("horizontal stack",h_stack)
print("sorted array",np.sort(f))
print("addition",f+g)
print("substraction",f-g)
print("multiplication",f*g)
print("division",f/g)
print("power",f**2)
print("sqrt",np.sqrt(f))
print("exponential",np.exp(f))
print("first array",f)
print("first element",x[0])
print("last element",x[-1])
print("every second elemetn",x[::2])
print("reversed array",x[::-1])




      

