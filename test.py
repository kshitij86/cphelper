import os
import time
from cphelper import cli
from click.testing import CliRunner
from strings import TEST_SUCCESS, CLEANUP_SUCCESS, TEST_FOLDER_NAME

def test_cphelper():
	""" Test the default setup using click testing libraries"""
	
	try:
		# create a runner and test the cli
		# this always creates a folder called "new_folder"
		runner = CliRunner()
		result = runner.invoke(cli, [TEST_FOLDER_NAME])
		# assert result.exit_code == 0
		# assert os.path.isdir("./mako") == True
		print(TEST_SUCCESS)

		# introduce delay to notice changes
		time.sleep(3)

		# code to cleanup the default folder
		# first the folder needs to be emptied
		for i in range(6):
			os.remove(f"./{TEST_FOLDER_NAME}/{i+1}.cpp")
		# as lang is C++, input and output files also exist
		os.remove(f"./{TEST_FOLDER_NAME}/input.txt")
		os.remove(f"./{TEST_FOLDER_NAME}/output.txt")

		#remove the empty directory
		os.rmdir(f"./{TEST_FOLDER_NAME}")

		print(CLEANUP_SUCCESS)
	except Exception as e:
		print(f"fatal error during test: {str(e)}")

if __name__ == '__main__':
	test_cphelper()