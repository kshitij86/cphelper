import os
import time
from cphelper import cli
from click.testing import CliRunner
from strings import TEST_SUCCESS, CLEANUP_SUCCESS

def test_cphelper():
	""" Test the default setup using click testing libraries"""
	
	# create a runner and test the cli
	# this always creates a folder called "new_folder"
	runner = CliRunner()
	result = runner.invoke(cli)
	assert result.exit_code == 0
	assert os.path.isdir("./new_folder") == True
	print(TEST_SUCCESS)

	# introduce delay to notice changes
	time.sleep(3)

	# code to cleanup the default folder
	# first the folder needs to be emptied
	for i in range(6):
		os.remove(f"./new_folder/{i+1}.cpp")
	# as lang is C++, input and output files also exist
	os.remove(f"./new_folder/input.txt")
	os.remove(f"./new_folder/output.txt")

	#remove the empty directory
	os.rmdir("./new_folder")

	print(CLEANUP_SUCCESS)



test_cphelper()