from distutils.core import setup

setup(
    name='koalamail',
    packages=['koalamail'],  # this must be the same as the name above
    version='0.1.1-alpha',
    description='',
    author='Matt Badger',
    author_email='foss@lighthouseuk.net',
    url='https://github.com/LighthouseUK/koalamail',  # use the URL to the github repo
    download_url='https://github.com/LighthouseUK/koalamail/tarball/0.1.1-alpha',  # I'll explain this in a second
    keywords=['gae', 'lighthouse', 'koala'],  # arbitrary keywords
    classifiers=[],
    requires=['jinja2']
)
