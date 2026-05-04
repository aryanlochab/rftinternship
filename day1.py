#original data
data = [10, None, 20, 10, "", 30, None, 40]

#lets remove none and "" empty strings
for item in data[:]:
    if item is None or item == "":
        data.remove(item)

# I am converting list to set to remove duplicated values
data = set(data)

#Lets return the clean list. 
print(data)
