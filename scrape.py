import requests
from bs4 import BeautifulSoup
import os
import re


ROOT_URL = 'https://sre.google'
TOC_URL  = '/sre-book/table-of-contents/'


def url_to_path(root_url = ROOT_URL):
    domain = root_url.split('//')[1]
    subdir = domain.replace('.', '_')
    return subdir

def download_links(root_url = ROOT_URL, \
                toc_url = TOC_URL, \
                filename=None):


    req = requests.get(root_url+toc_url)
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

def download_pages(dir_path='sre_google/', filename='link.txt'):  # generalize later
    ## TO ACTIVATE ALL PAGES AGAIN; CHANGE filename='links.txt'
    
    with open(dir_path+filename, 'r') as f:
        lines = f.readline()
    
    # currently seperated by commas
    links = lines.split(',')
    
    for link in links[:-2]:   # skips last empty line and bibliography
        branch = link.split('/')[-2]
        print('\n\n', branch) 
        text = get_page_as_text(link)
        write_text_to_file(text, dir_path+branch+'.txt') 
    return None 
        
def get_page_as_text(url, print_page=False, bold_titles=True):
    # TODO: regex selection titles ('\n\n<some string>\n) to make bold ('\n\n**<string>**\n')
    req = requests.get(url)
    req.encoding = 'utf-8'                      # TODO: might not be necessary?
    soup = BeautifulSoup(req.content)           # to get rid of html tags

    # small site specific alterations to text
    bottom = soup.text.split('Bibliography')[1] # get rid of nav bar links
    page = bottom.split('Previous')[0]          # get rid of footer
    page = page.replace('\n\n\n\n', '')         # cut unnecessary whitespaces
    page = page.replace("’", "'")               # replace erroneous apostrophe
    
    # get titles from soup 
    print(soup.find_all('h1'))


    if print_page:
        print(page)

    if bold_titles:
        regex = r"\n\n([^\.]+)\n"    # everytime '\n\n<string>\n occurs w/o a period . 
        matches = re.findall(regex, page)
        for m in matches:
            m = m.strip('\n')
            page = page.replace(m, f'# {m}') # replaces with markdown title

    return page

def write_text_to_file(text='', filename=''):
    with open(filename, 'w+') as f:
        f.write(text)
    return text

if __name__=='__main__':
    # download links of chapters
    # download_links()

    # download content from pages to files
    download_pages()

