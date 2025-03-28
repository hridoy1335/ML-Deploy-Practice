from setuptools import setup, find_packages
from typing import List

HIPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    It removes any '-e .' entry from the list.
    """
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n', '') for req in requirement]
        if HIPEN_E_DOT in requirement:
            requirement.remove(HIPEN_E_DOT)
    return requirement
setup(
    name='ML-Deployment-Project',
    version='0.0.1',
    author='HRIDOY KHAN',
    author_email='rkhridoyinfo@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)