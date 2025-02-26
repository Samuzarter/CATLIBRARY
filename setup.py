from setuptools import setup, find_packages

setup(
    name ='catlibrary',
    version='1.3',
    packages=find_packages(),
    description='Libreria para obtener gatos',
    long_description='Hola',
    long_description_content_type='text',
    author='Samuel Quiroz Rincón',
    author_email='samuelquirozrincon1@gmail.com',
    url='https://github.com/Samuzarter/CATLIBRARY.git',
    install_requires=['requests','python-decouple','python-dotenv']
)