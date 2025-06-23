from setuptools import setup, find_packages

setup(
    name='concat_pdf',
    version='0.1.0',
    description='A tool to concatenate PDF files',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
    ],
    entry_points={
        'console_scripts': [
            'concat-pdf=main:main',
        ],
    },
    python_requires='>=3.7',
)
