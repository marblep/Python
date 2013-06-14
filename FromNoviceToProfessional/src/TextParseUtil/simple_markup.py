'''
Created on 2013-6-10

@author: Administrator
'''

import re
from toblocks import blocks

def SimpleMarkup(input_filename):
    inputfile = open(input_filename)
    
    markup = '<html>\n<head>\n<title>...</title>\n</head>\n<body>\n'
    title = True
    for block in blocks(inputfile):
        block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
        if title:
            markup += ('<h1>' + '\n' + block + '\n' + '<h1>' + '\n')
            title = False
        else:
            markup += ('<p>' + '\n' + block + '\n' + '<p>' + '\n')
    markup += '</body>\n</html>'
    
    html = open(input_filename + '_output.html', 'w')
    html.write(markup)
    html.close()
    
    
if __name__ == "__main__":
    SimpleMarkup(r'E:\eclipse-java-juno-SR1-win32\workspace\FromNoviceToProfessional\src\test_input.txt')
