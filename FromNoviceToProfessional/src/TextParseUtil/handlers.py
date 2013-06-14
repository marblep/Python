'''
Created on 2013-6-13

@author: Administrator
'''
class Handler:
    """
    An object that handles method calls from the Parser.

    The Parser will call the start() and end() methods at the
    beginning of each block, with the proper block name as a
    parameter. The sub() method will be used in regular expression
    substitution. When called with a name such as 'emphasis', it will
    return a proper substitution function.
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method): return method(*args)
    def start(self, name):
        return self.callback('start_', name)
    def end(self, name):
        return self.callback('end_', name)
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)
            return result
        return substitution

class HTMLRenderer(Handler):
    """
    A specific handler used for rendering HTML.

    The methods in HTMLRenderer are accessed from the superclass
    Handler's start(), end(), and sub() methods. They implement basic
    markup as used in HTML documents.
    """
    def start_document(self):
        return '<html>\n<head>\n<title>...</title>\n</head>\n<body>\n'
    def end_document(self):
        return '</body>\n</html>'
    def start_paragraph(self):
        return '\n<p>\n'
    def end_paragraph(self):
        return '\n</p>'
    def start_heading(self):
        return '<h2>\n'
    def end_heading(self):
        return '</h2>\n'
    def start_list(self):
        return '<ul>'
    def end_list(self):
        return '</ul>'
    def start_listitem(self):
        return '<li>'
    def end_listitem(self):
        return '</li>'
    def start_title(self):
        return '<h1>\n'
    def end_title(self):
        return '</h1>\n'
    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)
    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
    def feed(self, data):
        return data
    
    

if __name__ == "__main__":    
    import re
    from toblocks import blocks

    input_filename = r'E:\eclipse-java-juno-SR1-win32\workspace\FromNoviceToProfessional\src\test_input.txt'
    inputfile = open(input_filename)
    
    handler = HTMLRenderer()
    markup = handler.start('document') 
    title = True
    for block in blocks(inputfile):
        block = re.sub(r'\*(.+?)\*', handler.sub('emphasis'), block)
        if title:
            markup += handler.start('title')
            markup += block
            markup += handler.end('title')
            title = False
        else:
            markup += handler.start('paragraph')
            markup += block
            markup += handler.end('paragraph')
    markup += handler.end('document') 
    
    html = open(input_filename + '_handler_output.html', 'w')
    html.write(markup)
    html.close()
    
    
    
    
    
