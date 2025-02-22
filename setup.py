from setuptools import setup, find_packages

setup(
    name ='catlibrary',
    version='1.2',
    packages=find_packages(),
    description='Libreria para obtener gatos',
    long_description='Hola',
    long_description_content_type='text',
    author='Samuel',
    author_email='prueba@gmail.com',
    url='probando',
    requires=['requests'],
)