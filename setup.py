from setuptools import find_packages,setup
from typing import List

HYPEN = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
        This will return list of req
    """
    req=[]
    with open('requirements.txt') as file_obj:
        req=file_obj.readlines()
        req = [r.replace("\n","") for r in req]

        if HYPEN in req:
            req.remove(HYPEN)
    return req

setup(
    name='mlproject',
    version='0.0.1',
    author='Madhu',
    author_email='madhusudhanaraghu02@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)