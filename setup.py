
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

import bsdquota
setup(name='bsdquota',
      version='0.1',
      description=bsdquota.__doc__,
      author=bsdquota.__author__,
      author_email='osborne6@gmail.com',
      url='https://github.com/osborne6/bsdquota',
      license=xmltodict.__license__,
      platforms=['all'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],
      py_modules=['bsdquota'],
      )



