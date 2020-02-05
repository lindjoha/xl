import setuptools

setuptools.setup(
	name = "xl",
	packages = ["xl"],
	version = "0.0.1",
	install_requires = ["pandas", "xlrd"],
	entry_points = {"console_scripts" : ["xl=xl:main"]}
)