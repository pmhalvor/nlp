import requests as re
from bs4 import BeautifulSoup
import os

ROOT_URL = 'https://sre.google'
TOC_URL  = '/sre-book/table-of-contents/'


def url_to_path(root_url = ROOT_URL):
    domain = root_url.split('//')[1]
    subdir = domain.replace('.', '_')
    return subdir

def download_links(root_url = ROOT_URL, \
                toc_url = TOC_URL, \
                filename=None):


    req = re.get(root_url+toc_url)
    soup = BeautifulSoup(req.text, 'html.parser')

    branches = []
    for link in soup.find_all('a'):
        branch = str(link).split('"')[1]
        if branch[:3] in toc_url:
            branches.append(root_url+branch)

    # make subdirectory
    subdir = url_to_path(root_url)
    try:
        os.mkdir(subdir)
    except: 
        print(f'Subdirectory {subdir} already exists')
        return None

    # configure filename automatically
    if not filename:
        filename = subdir+'/links.txt'

    with open(filename, 'w+') as f:
        for branch in branches:
            f.write(branch+',')

def download_pages(dir_path='sre_google/', filename='links.txt'):  # generalize later
    with open(dir_path+filename, 'r') as f:
        lines = f.readline()
    
    # currently seperated by commas
    links = lines.split(',')
    
    for link in links[:-2]:   # skips last empty line and bibliography
        branch = link.split('/')[-2]
        print('\n\n', branch) 
        text = get_page_as_text(link)
        append_text_to_file(text, dir_path+branch+'.txt') 
    return None 
        
def get_page_as_text(url, print_content=False):
    req = re.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    bottom = soup.text.split('Bibliography')[1]
    page = bottom.split('Previous')[0]
    content = page.replace('\n\n\n\n', '')
    content = content.replace('â', '')
    if print_content:
        print(content)
    return content

def append_text_to_file(text='', filename=''):
    with open(filename, 'a+') as f:
        f.write(text)
    return text

if __name__=='__main__':
    # download links of chapters
    # download_links()

    # download content from pages to files
    download_pages()

