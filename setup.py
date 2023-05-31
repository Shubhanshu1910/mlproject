from setuptools import find_packages,setup
from typing import List

HYPEN_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
    requirement = []
    with open(file_path) as file:
        requirement = file.readlines()
        requirement = [res.replace("\n",' ') for res in requirement]
        if HYPEN_DOT in requirement:
            requirement.remove(HYPEN_DOT)
        
    return requirement
        
setup(
    name='mlproject',
    version = '0.0.0.1',
    author="Harsh",
    author_email = "shubhanshum154@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)