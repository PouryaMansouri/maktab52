class Indenter:

    def __init__(self):
        self.count = 0
        self.tab = []

    def __enter__(self):
        if self.count != 0:
            self.tab.append("\t")
        self.count += 1
        return self

    def print(self, text):
        print(*self.tab, end="")
        print(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:  # When exception Raised!
            print(f">>> Error: {exc_type=} : {exc_val=}")
        else:
            self.count -= 1
            if self.count != 0:
                self.tab.pop()


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('talk is cheap')
        with indent:
            indent.print('show me the code ')
        indent.print('show me the code ')
    indent.print('Torvalds')

# output is :

"""
hi!
	talk is cheap
		show me the code 
Torvalds



"""
