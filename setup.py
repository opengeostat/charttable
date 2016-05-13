"""
Charttable: HTML Tables with bars charts for exploratory data analysis

Copyright 2016, Adrian Martinez Vargas.
Licensed under GPL.
"""


from distutils.core import setup


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
            'License :: OSI Approved :: GPL License',
            'Topic :: Scientific/Engineering :: Mathematics']
keywords='html tables EDA'
author='Adrian Martinez Vargas'
author_email='adriangeologo@yahoo.es'
url='https://github.com/opengeostat/charttable'
 
                            
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
      packages=['charttable'],)

