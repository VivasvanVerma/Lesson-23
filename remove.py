studentData = {'id1':{'Name':['Sara'], 'Class':['V'], 'Subjects':['English,Maths,Science']}
               , 'id2':{'Name':['David'], 'Class':['V'], 'Subjects':['English,Maths,Science']}
               , 'id3':{'Name':['Sara'], 'Class':['V'], 'Subjects':['English,Maths,Science']}
               , 'id4':{'Name':['Leo'], 'Class':['V'], 'Subjects':['English,Maths,Science']}}

result = {}

for key,value in studentData.items():
    if value not in result.values():
        result[key] = value

print(result)