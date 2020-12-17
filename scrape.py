import requests as re
from bs4 import BeautifulSoup
import os

ROOT_URL = 'https://sre.google'
TOC_URL  = '/sre-book/table-of-contents/'


def download_links(root_url = ROOT_URL, \
                toc_url = TOC_URL, \
                file_name=None):


    req = re.get(root_url+toc_url)
    soup = BeautifulSoup(req.text, 'html.parser')

    branches = []
    for link in soup.find_all('a'):
        branch = str(link).split('"')[1]
        if branch[:3] in toc_url:
            branches.append(root_url+branch)

    # make subdirectory
    subdir = url_to_path(root_url, toc_url)
    try:
        os.mkdir(subdir)
    except: 
        print(f'Subdirectory {subdir} already exists')

    # configure file_name automatically
    if not file_name:
        file_name = subdir+'/links.txt'

    with open(file_name, 'w+') as f:
        for branch in branches:
            f.write(branch+'\n')


###
### STORE LINKS AS CSV
### Problems with new line in download pages causing http errors!
####
def download_pages(link_path='sre_google/links.txt'):  # generalize later
    with open(link_path, 'r') as f:
        links = f.readlines()
    
    c = 0
    N = 3
    for link in links:
        scrape_to_file(link)
        c += 1
        if c>N:
            break 
    return None 
    
        
def scrape_to_file(url):
    req = re.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    print(soup.find_all('p'))


if __name__=='__main__':
    # download_links()

    # download content from pages to files
    download_pages()





    # def read_links(root_url = ROOT_URL, \
    #                 toc_url = TOC_URL):
    #     return None

    # def get_links(link_path=):
    #     return None

    # def url_to_path(root_url = ROOT_URL, \
    #                 path_url = PATH_URL):
    #     domain = root_url.split('//')[1]
    #     subdir = domain.replace('.', '_')
    #     return subdir