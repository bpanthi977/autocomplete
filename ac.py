import os
import autocomplete as ac
from autocomplete import models



def train_bigtxt():
    """unnecessary helper function for training against
    default corpus data (big.txt)"""

    bigtxtpath = os.path.join(os.path.dirname(__file__), 'bigNepali.txt')
    with open(bigtxtpath, 'r') as bigtxtfile:

        models.train_models(str(bigtxtfile.read()))
        
# train_bigtxt()

ac.load()
ac.run_server()



