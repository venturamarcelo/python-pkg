import re

def betweenFSlashAndComma(text):
    '''
    return a string between the forward slash '/' and a comma ',' 
    '''
    regexp = re.compile(r'(\/.*[^\/])+\,')
    m = regexp.search(text)
    r = m.group().rstrip('\,')

    return r