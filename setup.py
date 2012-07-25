import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'gevent',
    'gevent-websocket',
    'gevent-socketio',
    'gunicorn',
    'pyramid_jinja2',
    ]

setup(name='RealTimeChart',
      version='0.0',
      description='RealTimeChart',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Alvaro Aguirre',
      author_email='aaguirre@alma.cl',
      url='http://www.almascience.org',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="realtimechart",
      entry_points = """\
      [paste.app_factory]
      main = realtimechart:main
      """,
      )

