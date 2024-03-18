import numpy as np
data = list(range(20,100,5))
print(data)

Q1 = np.quantile(data,0.25)
Q2 = np.quantile(data,0.50)
Q3 = np.quantile(data,0.75)

print("Quartile 1",Q1)
print("Quartile 2",Q2)
print("Quartil3 3",Q3)

def quartile(a,b):
    print("THIS IS THE QUARTILE OF THE DATA :")
    return (a-b)/2
def IQR(a,b):
    print("THIS IS THE IQR OF THE DATA :")
    return a-b
print(quartile(Q3,Q1))
print(IQR(Q3,Q1))
