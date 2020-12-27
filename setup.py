from setuptools import setup, find_packages

setup(
    name='microsms_sdk',
    author='ivall',
    author_email='ivallpl@gmail.com',
    install_requires=['requests', 'hashlib'],
    version='1.0',
    description='Simple microsms api wrapper in python.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ivall/microsms-sdk-python",
    packages=find_packages()
)
