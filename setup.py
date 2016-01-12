__author__ = 'zhaoyifei'

from setuptools import setup, find_packages
setup(
      name="dwh",
      version="0.10",
      description="datawarehouse etl",
      author="zhaoyifei",
      url="http://www.zlycare.com",
      license="LGPL",
      packages=find_packages(),
      py_modules=['etl'],
      data_files=[('config', ['config.ini'])],

      )
