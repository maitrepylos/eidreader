SETUP_INFO = dict(
    name='eidreader',
    version='1.0.6',
    install_requires=['requests', 'PyKCS11'],
    scripts=['scripts/eidreader'],
    packages=['eidreader'],
    description="Read data from Belgian eId card via command-line",
    license='BSD-2-Clause',
    author='Luc Saffre',
    url="http://eidreader.lino-framework.org",
    author_email='luc@saffre-rumma.net')

SETUP_INFO.update(long_description="""\

eidreader is a command-line script that reads data from Belgian eID cards and
writes the data to stdout or posts it to a web server. It is designed to be used
together  with a web application.

Not to be mixed up with its deprecated Java predecessor `eidreader
<https://github.com/lsaffre/eidreader>`__ (same project name but
another account).

- The central project homepage is
  http://eidreader.lino-framework.org
- Please report issues to
  https://github.com/lino-framework/eidreader/issues

""")
SETUP_INFO.update(classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 5 - Stable
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Natural Language :: English
Operating System :: OS Independent""".splitlines())
