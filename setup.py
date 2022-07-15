from setuptools import setup

setup(
	name="cphelper",
	version='0.0',
	py_modules=['cphelper'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		cphelper=cphelper:cli
	''',
)