from setuptools import setup, find_packages
from typing import List

def get_requirements(file_name: str) -> List[str]:
    requirements = []
    hypen_dot_e = '-e .'
    with open("requirements.txt") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n", "") for req in requirements]
        if hypen_dot_e in requirements:
            requirements.remove(hypen_dot_e)
    return requirements

setup(
    Name = "Diamond Price Prediction",
    Version = "0.0.1",
    Author = "Raju Gopi",
    Author_Email = "rajugraj29@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()
)