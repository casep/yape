from setuptools import setup

setup(name='yape',
      version='2.0',
      description='Yet another pbuttons tool',
      url='https://github.com/murrayo/yape',
      author='Fabian',
      author_email='fab@intersystems.com',
      license='MIT',
      packages=['yape'],
      entry_points = {
        'console_scripts': ['yape=yape.command_line:main','yape-profile=yape.command_line:main_profile'],
      },
      install_requires=[
        'altgraph>=0.10.2','py-dateutil>=2.2',
      'bdist-mpkg>=0.5.0',
      'certifi>=2017.7.27.1',
      'cffi>=1.10.0',
      'chardet>=3.0.4',
      'idna>=2.5',
      'bokeh>=0.12.6',
      'macholib>=1.5.1',
      'matplotlib>=2.0.2',
      'pandas>=0.20.3',
      'modulegraph>=0.10.4',
      'numpy>=1.13.1',
      'py2app>=0.7.3',
      'pycparser>=2.18',
      'pyparsing>=2.0.1',
      'python-dateutil>=1.5',
      'pytz>=2013.7',
      'requests>=2.18.3',
      'six>=1.4.1',
      'urllib3>=1.22',
      'zope.interface>=4.1.1'],
      zip_safe=False)