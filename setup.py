from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    It removes any empty lines and comments.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    # Clean up the list
    requirements = [req.replace('\n', '') for req in requirements]

    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements


setup(  
    name='end-to-endmlproject',
    version='0.0.1',
    author='Vedant',
    author_email='vedxntshirgaonkar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)