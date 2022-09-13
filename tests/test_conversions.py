
from utils import conversions

def test_fahrToKelv():
    '''
    make sure freezing is calculated correctly
    '''
    assert conversions.fahrToKelv(32) == 273.15, 'incorrect freezing point!'