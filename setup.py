from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='kartik',
    author_email='kartik61003@gmail.com',
    install_requires=[
        'langchain',
        'langchain_community',
        'openai',
        'pandas',
        'dotenv',
        'PyPDF2',
        'streamlit'
    ],
    packages=find_packages()
)