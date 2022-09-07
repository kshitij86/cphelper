import os
import click
from strings import DEFAULT_LANG_EXT, CPP_TEMPLATE, CURR_CONFIG_PROMPT, SUCCESS_MSG, HELP_STRINGS


@click.command()
@click.argument('name')
# @click.option('--name', type=str, default='new_folder', help=HELP_STRINGS["NAME_HELP"])
@click.option('--count', type=int, default=6, help=HELP_STRINGS["COUNT_HELP"])
@click.option('--lang', type=str, default='cpp', help=HELP_STRINGS["LANG_HELP"])
@click.option('--target', type=str, default='.', help=HELP_STRINGS["TARGET_HELP"])
@click.option("--verbose", type=bool, default=False, help=HELP_STRINGS["VERBOSE_HELP"])
def cli(name, count, lang, target, verbose):
    """This creates a folder with count files"""

    # method to print messages only if verbose is set to True
    def console_print(msg):
        if verbose == True:
            click.echo(msg)

    def execute():
        console_print(CURR_CONFIG_PROMPT)
        console_print([name, lang, target, count])

        try:
            if len(name) > 25:
                raise Exception(
                    "contest name too long, needs to be at  25 characters")
            if count > 100:
                raise Exception(
                    "yowza!, that's a lot of files. try again with atmost 100 files")

            # try to create the directory for the files if not exists
            if os.path.isdir(target):
                PATH_DIR = f"{target}/{name}/"
                folder_exists = os.path.isdir(PATH_DIR)
                if folder_exists == False:
                    os.mkdir(path=PATH_DIR)
            else:
                raise Exception(f"directory \"{target}\" not found")

            # create 'count' number of files
            # each file shuld have the predefined template depending on template option
            # works only when language matches default lang
            FILES_PREFIX = f".{lang}"
            for i in range(int(count)):
                file_name = f"{PATH_DIR}{i+1}{FILES_PREFIX}"
                code_file = open(file_name, 'w')
                if lang == DEFAULT_LANG_EXT:
                    code_file.write(CPP_TEMPLATE)

            # create input and output files if lang is C++
            if lang == DEFAULT_LANG_EXT:
                input_file = f"{PATH_DIR}input.txt"
                open(input_file, 'w')
                output_file = f"{PATH_DIR}output.txt"
                open(output_file, 'w')

            console_print(SUCCESS_MSG)
        except Exception as e:
            click.echo(f"fatal error: {str(e)}")
    execute()
