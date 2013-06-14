'''
Created on 2013-6-9

@author: Administrator
'''

def lines(_file):
    for line in _file:
        yield line
    yield '\n'
    
def blocks(_file):
    block = []
    for line in lines(_file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
    
if __name__ == "__main__":
    thefile = open(r'E:\eclipse-java-juno-SR1-win32\workspace\FromNoviceToProfessional\src\test_input.txt')
    
    for block in blocks(thefile):
        print block
        print "==================="
        
        
        
        
        