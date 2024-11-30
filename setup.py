from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT='-e .'# We dont want -e to come under get_requirement as the function will treat it as string and there is no package as '-e .'

def get_requirements(file_path:str)->List[str]:  # Define function with input as file_path in string format and '->' denotes the output which is list of strings
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) # This will remove the '-e .' as we dont need it and there is no such package
    return requirements

setup(
    name='ML_generic',
    version='0.0.1',
    author='Shivam',
    author_email='shivambisht0770@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # This assumes get_requirements is properly defined
)