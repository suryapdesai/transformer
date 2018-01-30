from setuptools import find_packages, setup

setup(
    name="transformer",
    version="",
    description="zapier transformer",
    author="transformer",
    author_email="transformer@zapier.com",
    url="https://github.com/zapier/transformer",
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    install_requires=[
        'arrow==0.7.0',
        'Babel==2.2.0',
        'beautifulsoup4==4.4.1',
        'blinker==1.4',
        'contextlib2==0.5.1',
        'Flask==0.10.1',
        'gunicorn==19.4.5',
        'inflect==0.2.5',
        'itsdangerous==0.24',
        'Jinja2==2.8',
        'Markdown==2.6.5',
        'MarkupSafe==0.23',
        'mock==2.0.0',
        'money==1.2.2',
        'newrelic==2.60.0.46',
        'python-dateutil==2.4.2',
        'raven==5.10.2',
        'pytz==2015.7',
        'six==1.10.0',
        'titlecase==0.8.1',
        'Unidecode==0.04.21',
        'Werkzeug==0.11.3',
        'wheel==0.24.0',
        'phonenumbers==7.2.5',
        'parsedatetime==2.1',
        'simplejson==3.11.1',
    ],
    include_package_data=True,
    packages=find_packages(exclude=['tests', 'tests.*'])
)
