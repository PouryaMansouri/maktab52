with Indenter() as indent: 
    indent.print('hi!') 
    with indent:
        indent.print('talk is cheap') 
        with indent:
            indent.print('show me the code ') 
    indent.print('Torvalds')




# output is :

"""
hi!
	talk is cheap
		show me the code 
Torvalds



"""
