from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in epiuse_theme/__init__.py
from epiuse_theme import __version__ as version

setup(
	name="epiuse_theme",
	version=version,
	description="EPI-USE Theme",
	author="Christiaan Swart",
	author_email="christiaan.swart@epiuse.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
