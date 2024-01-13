from setuptools import setup, find_packages

setup(
    name='endpoint',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'endpoint = my_script.endpoint:main',
        ],
    },
)
