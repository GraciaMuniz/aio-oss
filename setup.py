from setuptools import setup, find_packages


setup(
    name='aiooss',
    version='0.1',
    description='Asyncio-based client for Aliyun OSS',
    author='Rocky Feng',
    author_email='folowing@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
