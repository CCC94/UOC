# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:30:35 2022

@author: Carlos
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def getdata(url):
    r = requests.get(url)
    return r.text


def html_code(url):
  
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # return html code
    return(soup)


def get_page(soup):
    data_str = ""
    for item in soup.find_all("li", class_="selected"):
        res= data_str + item.get_text()
        print(res)
        return (res)

def iterate_pages (url):
    url1 = url
    pages = [url]
    count = 1
    while count == int(get_page(html_code(url))):
        count += 1
        
        url = url1 + f'pagina-{count}.htm'
        pages.append(url)
    return pages
        
    

def property_data(soup):
    

    data_str = ""
    for item in soup.find_all("a", class_="item-link"):
        result_1 = data_str + item.get_text()
        yield(result_1)
        
def price_data(soup):
    
    data_str = ""
    for item in soup.find_all("span", class_="item-price h2-simulated"):
        result_2 = data_str + item.get_text()
        result_2= re.sub('\D', '', result_2)
        result_2 = int(result_2)
        yield(result_2)

def num_hab(soup):
    data_str = ""
    for item in soup.find_all("div", class_="item-detail-char"):
        result_3 = data_str + item.get_text()
        if (' hab.') in result_3:
            result_3 = result_3.split(' hab.')[0]
            result_3 = int(result_3.strip())
        else:
            result_3 = 'no_data'
        yield(result_3)

def m2(soup):
    data_str = ""
    for item in soup.find_all("div", class_="item-detail-char"):
        result = data_str + item.get_text()
        if (' m²') in result:
            result_4 = result.split(' m')[0]
            if (' hab.') in result_4:
                result_4 = result_4.split(' hab.')[1]
            
            result_4 = float(result_4.strip())
        else:
            result_4 = 'no_data'
        yield(result_4)

def planta(soup):
    data_str = ""
    for item in soup.find_all("div", class_="item-detail-char"):
        result = data_str + item.get_text()
        if ('Planta') in result:
            result_5 = result.split('Planta')[1]
            result_5 = re.split('[^0-9]', result_5.strip())[0]
        elif ('treplanta') in result:
            result_5 = 'entreplanta'
            
            #result_5 = int(result_5.strip())
        else:
            result_5 = 'no_data'
        yield(result_5)

def ascensor(soup):
    data_str = ""
    for item in soup.find_all("div", class_="item-detail-char"):
        result = data_str + item.get_text()
        if ('ascensor') in result:
            if ('con ascensor') in result:
                result_6 = 1
            elif ('sin ascensor') in result:
                result_6 = 0
            else:
                result_6 = 'no_data'
            
            #result_5 = int(result_5.strip())
        else:
            result_6 = 'no_data'
        yield(result_6)    

def descripcion(soup):
    data_str = ""
    for item in soup.find_all("p", class_="ellipsis"):
        result = data_str + item.get_text()
        yield(result)


def gen_dict(sample1):
    dic = {}      
    count1=0
    for i, j, k, l, q, w, e  in zip(property_data(sample1), 
                          price_data(sample1), num_hab(sample1), 
                          m2(sample1), planta(sample1), ascensor(sample1),
                          descripcion(sample1)):
        count1 += 1
        dic[f'propiedad_{count1}']={'propiedad':i, 'precio':j, 'num_hab':k, 'm2':l,
                                    'planta':q, 'ascensor': w, 'descripcion': e,
                                    'time_of_download': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        
    return(dic)


if __name__ == "__main__":

    df_alquiler_barcelona = pd.DataFrame(columns=['propiedad','precio','num_hab','m2',\
                                                  'planta','ascensor','descripcion',\
                                                      'time_of_download'])   
    
    url = 'https://www.idealista.com/alquiler-viviendas/barcelona-barcelona/'
    pages = iterate_pages(url)
    for page in pages:
        sample = html_code(page)
        dic = gen_dict(sample)
        for keys, values in dic.items():
            df_alquiler_barcelona =  df_alquiler_barcelona.append(values, ignore_index = True)
            
    df_alquiler_barcelona.to_csv('alquiler_idealista_barcelona', index=False)
    
        