#!/usr/bin/python3

import os
import sys
from subprocess import Popen, PIPE


def gits_add_func(args):
    """
    Function that adds files as passed
    to the gits add command.
    Performs operation as similar to git
    add command
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("add")
        file_names_list = args.file_names
        total_files = len(file_names_list)
        if total_files == 0:
            #do nothing
            pass
        else:
            for i in range(0, total_files):
                subprocess_command.append(file_names_list[i])
            process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()

    except Exception as e:
        print("ERROR: gits add command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
