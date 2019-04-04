import sys
from setuptools import setup, Extension

if sys.version_info < (3,):
    type = 'py2'
else:
    type = 'py3'

module1 = Extension('unicodedataplus',
                    sources = ['./unicodedataplus/' + type + '/unicodedata.c',
                               './unicodedataplus/unicodectype.c'],
                    include_dirs = ['./unicodedataplus/' + type, './unicodedataplus/'],
)

setup (name = "unicodedataplus",
       version = "12.0.0",
       description = "Unicodedata with extensions for additional properties.",
       ext_modules = [module1],
       author="Ben Yang",
       author_email="benayang@gmail.com",
       download_url="http://github.com/iwsfutcmd/unicodedataplus",
       license="Apache License 2.0",
       platforms=['any'],
       url="http://github.com/iwsfutcmd/unicodedataplus",
       test_suite="tests",
)
