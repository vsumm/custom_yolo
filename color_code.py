with open('output_test.txt','r') as file:
    data = file.readlines()

for a in range(len(data)):
    if 'person' in data[a] and 'tv' in data[a]:
        data[a] = data[a].replace('\n','') + ' status : Low\n'
    else:
        data[a] = data[a] + ' status : High'

with open('outputs.txt','w') as file:
    file.writelines(data)