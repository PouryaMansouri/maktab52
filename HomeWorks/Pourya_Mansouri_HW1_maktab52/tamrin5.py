list1=['morning','afternoon','night']
list2=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
tags=[]
for day in list2:
    for time in list1:
        tags.append(day+'-'+time)
print(tags)