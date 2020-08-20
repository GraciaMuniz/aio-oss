from setuptools import setup, find_packages


setup(
    name='aiooss',
    version='0.6',
    description='Asyncio-based client for Aliyun OSS',
    author='Rocky Feng',
    author_email='folowing@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['aiohttp>=3.6.2'],
    zip_safe=False,
)
