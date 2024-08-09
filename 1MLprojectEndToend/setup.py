from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #whenever we try to read new lines, as specified in requirements.txt \n also gets added. We will try to replace it with blank
        requirements=[req.replace("\n","") for req in requirements]  #also -e . in requirements.txt will automatically trigger setup.py
        #but while running this code '-e .' should not come here, it should directly connect to setup.py, we will create a constant for that and make a condition on that
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
name='mlproject',
version='0.0.1',
author='Rohit',
author_email='rmandhyan54@gmail.com',
packages = find_packages(),
# install_requires=['pandas','numpy','seabron'] we'll require 100's of packages in a project, its not feasible to write all of them here. So see next line for the soltion
install_requires = get_requirements('requirements.txt') #now we have to create and define function get_requirements 
)