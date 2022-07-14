import os
import click
from strings import DEFAULT_LANG, CODE_TEMPLATES, CURR_CONFIG, SUCCESS_MSG


@click.command()
@click.option('--name', type=str, default='new_folder', 
	help="The name of the directory, preferably the name of the contest.")
@click.option('--count', type=int, default=6, 
	help="The number of files to be created, defaults to 6.")
@click.option('--lang', type=str, default='cpp', 
	help="The programming language used, same for all files, defaults to C++. Only the extension needs to provided.")
@click.option('--target', type=str, default='.', 
	help="The directory where the create the folder, defaults to pwd.")
@click.option("--template", type=bool, default=True, 
	help="This populates each file with the default C++ template. Does not work if language is other than C++")
@click.option("--verbose", type=bool, default=False,
	help="This will make cphelper print messages to the console")
def cli(name, count, lang, target, template, verbose):
	"""This creates a folder with count files"""

	# method to print messages only if verbose is set to True
	def console_print(msg):
		if verbose == True:
			click.echo(msg)

	def execute():
		console_print(CURR_CONFIG)
		console_print([name, lang, target, count])


		# try to create the directory for the files if not exists
		PATH_DIR = f"{target}/{name}/"
		folder_exists = os.path.isdir(PATH_DIR)
		if folder_exists == False:
			os.mkdir(path=PATH_DIR)


		# create 'count' number of files
		# each file shuld have the predefined template depending on template option
		# works only when language matches default lang
		FILES_PREFIX = f".{lang}"
		template_file = open(CODE_TEMPLATES, 'r')
		cpp_template = template_file.read()
		for i in range(int(count)):
			file_name = PATH_DIR + f"{i+1}" + FILES_PREFIX
			code_file = open(file_name, 'w')
			if lang == DEFAULT_LANG:
				code_file.write(cpp_template)

		# create input and output files if lang is C++
		if lang == DEFAULT_LANG:
			input_file = f"{PATH_DIR}input.txt"
			open(input_file, 'w')
			output_file = f"{PATH_DIR}output.txt"
			open(output_file, 'w')


		console_print(SUCCESS_MSG)
	execute()