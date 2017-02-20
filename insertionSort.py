input=[9,2]
for i in range(1,len(input)):
  value=input[i]
  j=i
  while (j>0 and input[j-1]>value):
    input[j]=input[j-1]
    j=j-1
    
  input[j]=value

print(input)
