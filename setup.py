import sys
from setuptools import setup, Extension

with open("README.md") as f:
    long_description = f.read()

module_sources = ["./unicodedataplus/unicodedata.c", "./unicodedataplus/unicodectype.c"]

is_pypy = hasattr(sys, "pypy_version_info")
if is_pypy:
    module_sources.append("./unicodedataplus/pypy_ctype.c")
main_module = Extension(
    "unicodedataplus",
    sources=module_sources,
    include_dirs=["./unicodedataplus/"],
)

setup(
    name="unicodedataplus",
    version="14.0.0",
    description="Unicodedata with extensions for additional properties.",
    ext_modules=[main_module],
    author="Ben Yang",
    author_email="benayang@gmail.com",
    download_url="http://github.com/iwsfutcmd/unicodedataplus",
    license="Apache License 2.0",
    platforms=["any"],
    url="http://github.com/iwsfutcmd/unicodedataplus",
    test_suite="tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
