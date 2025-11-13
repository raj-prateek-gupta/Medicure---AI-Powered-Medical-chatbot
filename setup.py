from setuptools import find_packages, setup
from typing import List

def install_requirements()->List[str]:
    """
    Reads and returns the list of dependencies from requirements.txt
    """
    try:

      with open('requirements.txt','r') as file:
         requirements = file.readlines()
         requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#') and not req.startswith("-e")]
         return requirements
      
    except:
       raise FileNotFoundError("requirements.txt not found")
       
setup(

    name='Medicure-AI Powered medical chatbot',
    version='0.0.1',
    description="AI powered chatbot to answer the peoples query",
    author='Prateek Raj Gupta',
    author_email='Prateekgupta11.40@gmail.com',
    packages = find_packages(),
    install_requires=install_requirements()
)