from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """This fucntion will return list of requirements"""
    req_lst : List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            
            for line in lines:
                req = line.strip()
                if req and req!='-e .':
                    req_lst.append(req)
    except FileNotFoundError:
        print('Requirements.txt file not found.')
    
    return req_lst

setup(
    name='Network Security',
    version='0.0.1',
    author='Rushikesh',
    author_email='rushi2001bobade@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)