import sys
from setuptools import setup, Extension

# if sys.version_info < (3,):
#     type = 'py2'
# else:
type = 'py3' # Python 2 support has been removed

with open("README.md") as f:
       long_description = f.read()

main_module = Extension('unicodedataplus',
                    sources = ['./unicodedataplus/' + type + '/unicodedata.c',
                               './unicodedataplus/unicodectype.c'],
                    include_dirs = ['./unicodedataplus/' + type, './unicodedataplus/'],
)

setup (name = "unicodedataplus",
       version = "14.0.0",
       description = "Unicodedata with extensions for additional properties.",
       ext_modules = [main_module],
       author="Ben Yang",
       author_email="benayang@gmail.com",
       download_url="http://github.com/iwsfutcmd/unicodedataplus",
       license="Apache License 2.0",
       platforms=['any'],
       url="http://github.com/iwsfutcmd/unicodedataplus",
       test_suite="tests",
       long_description=long_description,
       long_description_content_type="text/markdown",
)
