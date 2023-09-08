from setuptools import setup, find_packages

dependencies = [

]


setup(
    name='symbolipy',
    version='1.0.1',
    packages=find_packages(),
    url='https://github.com/pmotakef/symbolipy',
    license='BSD 2-Clause "Simplified"',
    author='Pouya Motakef',
    author_email='p.motakef@gmail.com',
    description='Present mathematical equality and inequality in symbol format.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=dependencies,
)
