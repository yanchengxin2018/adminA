from setuptools import setup, find_packages

setup(
    name='adminA',
    version='2024.6.29.17',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
)
