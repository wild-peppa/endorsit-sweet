from setuptools import setup, find_packages

setup(
    name="endorsit-sdk",
    version="0.0.1",
    description='endorsit-sdk',
    packages=find_packages(exclude=["migrations"]),
    namespace_packages=['endorsit'],
    keywords=('endorsit-sdk'),
    install_requires=[],
    zip_safe=False,
)