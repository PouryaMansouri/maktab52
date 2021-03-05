students_list = [
'AmirHassan',
'Sajjad',
'Mehdi',
'Hamid',
"Rooh'o'lah",
'Sina',
'Mohammad',
'Hamed',
'Masoud'
]
# for name in students_list:
#     print("Hello",name)

print(*map(lambda x:f'Hello {x}', students_list), sep='\n')