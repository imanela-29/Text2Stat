import requests
from bs4 import BeautifulSoup
import re

def nbr_pages():
    global notre_li
    nbr = []
    url1 = 'http://www.ump.ma/fr/actualite'
    response1 = requests.get(url1)
    if response1.ok:
        soup1 = BeautifulSoup(response1.text, 'lxml')
        uls = soup1.findAll('ul', class_='pagination')
        for ul in uls:
            for li in ul.findAll('li'):
                nbr.append(li)
                index = len(nbr) - 2
                notre_li = nbr[index]
        notre_a = notre_li.find('a')
        nombre = notre_a.text  # nombre de pages existantes qu'on va parcourir
        n = int(nombre)
        return n

def liens(number):
    global les_liens
    url2 = 'http://www.ump.ma/fr/actualite?page=' + number
    response2 = requests.get(url2)

    if response2.ok:
        soup2 = BeautifulSoup(response2.text, 'lxml')
        divs = soup2.findAll('div', class_='caption')
        les_liens = []
        for div in divs:  # on a 9 div dans une page, chaque div représente un article
            a = div.find('a')
            un_lien = a['href']  # pour chaque div des 9 on recupere le href qui est dans a
            les_liens.append(un_lien)  # on les met dans une liste
    return les_liens

def titres(lien):
    url3 = lien
    response3 = requests.get(url3)
    les_h = []
    if response3.ok:
        soup3 = BeautifulSoup(response3.text, 'lxml')
        article = soup3.find('article')  # le contenu est dans la balise article
        h1 = article.find('h1')  # on extrait les titres de chaque article
        les_h.append(h1.text)
    return les_h

def contenu(lien):
    url4 = lien
    response4 = requests.get(url4)
    content = []
    if response4.ok:
        soup4 = BeautifulSoup(response4.text, 'lxml')
        articl = soup4.find('article')  # le contenu est dans la balise article
        les_p = articl.findAll('p')  # on cherche le contenu des p
        for p in les_p:
            content.append(p.text)  # on met le contenu dans lise contenu
    return content

def mainActu():
    nombre_pages = nbr_pages()
    inbr = 1
    print("debut extraction")
    while inbr <= nombre_pages:
        print(inbr)
        istr = str(inbr)
        links = liens(istr)
        for link in links:
            titles = titres(link)
            contenus = contenu(link)
            
            ar_output = open('ar_actu.txt', 'a', encoding='utf-8')
            fr_output = open('fr_actu.txt', 'a', encoding='utf-8')
            
            for h in titles:
                for i in h.split():
                    hh = re.search("[a-z]|[A-Z]|[0-9]", i)
                    if hh:
                        fr_output.write(i+' ')
                    else:
                        ar_output.write(i+' ')
                        
                fr_output.write('\n')
                ar_output.write('\n')
                        
            for c in contenus:
                for j in c.split():
                    cc = re.search("[a-z]|[A-Z]|[0-9]", j)
                    if cc:
                        fr_output.write(j+' ')
                    else:
                        ar_output.write(j+' ')
                
            fr_output.close()
            ar_output.close()

        inbr = inbr + 1

    print("fin extraction")

