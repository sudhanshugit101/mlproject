from setuptools import setup, find_packages

from typing import List

HYPHEN = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Reads requirements.txt file and returns a list of requirements."""
    requirements = []
    with open(file_path) as f:
        requirements = f.read().splitlines()

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
            
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    description='My first ML project',
    author='Sudhanshu',
    author_email='sudhanshu.vishnu73@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)