"""
Charttable: HTML Tables with bars charts for exploratory data analysis

Copyright 2016, Adrian Martinez Vargas.
Licensed under GPL.
"""
import warnings
import sys
from setuptools.command.test import test as TestCommand
from numpy.distutils.core import Extension


# This is a plug-in for setuptools that will invoke py.test
# when you run python setup.py test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  
        sys.exit(pytest.main(self.test_args))

# define properties for setup
""" 
 Note: using this convention for version 
 major.minor[.build[.revision]]
 with development status at third position as follow: 
    0 for alpha (status)
    1 for beta (status)
    2 for release candidate
    3 for (final) release
"""
version = '0.0.0.1.0'
description = 'Tables with bars charts for exploratory analysis in Ipython Notebooks'
name='charttable'
long_description=open("README.rst").read()
classifiers=[ 
            'Development Status :: 1 - Alpha',
            'Programming Language :: Python',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Topic :: Scientific/Engineering :: Mathematics',
keywords='html tables EDA'
author='Adrian Martinez Vargas'
author_email='adriangeologo@yahoo.es'
url='https://github.com/opengeostat/charttable'
 
        
if __name__ == '__main__':
     
    #Cython code extension
    #-------------------------------------------------------------------
    from distutils.core import setup    # this is the standard setup
    from distutils.extension import Extension as CYExtension
    import numpy
	
    charttable = CYExtension( 'charttable.charttable', 
                            ['cython_code/charttable.pyx'], 
							include_dirs=[numpy.get_include()]) 
                               
                            
    setup(name=name,
          version=version,
          description= description,
          long_description=long_description,
          classifiers=classifiers,
          keywords=keywords, 
          author=author,
          author_email=author_email,
          url=url,
          license='GPL',
          packages=find_packages(exclude=['examples', 'tests']),
          include_package_data=True,
          zip_safe=False,
          tests_require=['pandas>=0.17', 'nose', 'mock'],
          cmdclass={'test': PyTest},   
          install_requires=['pandas'],
          ext_modules = [charttable])

