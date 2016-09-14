#!/usr/bin/env python

from distutils.core import setup

setup(name='aiooss',
      version='0.1',
      description='Asyncio-based client for Aliyun OSS',
      author='Rocky Feng',
      author_email='folowing@gmail.com',
      url='https://github.com/folowing/aio-oss',
      packages=[
          'aiooss',
      ],
      requires=['aiohttp'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
      ],
      )
