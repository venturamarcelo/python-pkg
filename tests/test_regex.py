from utils import regex

def test_findFileName():
    '''
    make sure file name is captured by regex
    '''
    assert regex.betweenFSlashAndComma('Large text with path/to/first/file.txt , command then other things') == 'path/to/first/file.txt', 'no file name captured by regex.'