# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 19:03:47 2018

@author: bolto_000
"""

import os
import requests
from bs4 import BeautifulSoup

main_url = "https://pokemondb.net/pokedex/national/"

page = requests.get(main_url)
soup = BeautifulSoup(page.content, 'html.parser')
pokemon = [x.text for x in soup.find_all('a')]



for pk in pokemon:
    pk_lower = pk.lower()
    
    #get the image
    image_url = 'https://img.pokemondb.net/artwork/{}.jpg'.format(pk_lower)
    img_data = requests.get(image_url).content
    os.mkdir('data/imgs')
    outfile = os.path.join('data', 'imgs', '{}.jpg'.format(pk))

    with open(outfile, 'wb') as handler:
        handler.write(img_data)
        
        

# Link to metadata (before cleaning): https://www.kaggle.com/rounakbanik/pokemon/version/1