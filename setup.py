from setuptools import setup, find_packages

setup(
    name="streaming",
    version="1.0.5",  
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "requests",
    ],
    package_data={
        '': ['*.txt', '*.rst'],
        'streaming': ['*.xml'],
    },
    include_package_data=True,
)
