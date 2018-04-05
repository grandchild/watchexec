#!/usr/bin/env python3
import argparse
import subprocess as proc
import os.path as path
import os
import re


DEFAULT_IGNORE_DIRS = [".git", ".svn"]


parser = argparse.ArgumentParser(
	description="Run command whenever files in the path change.",
	formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("commands", nargs="*", default=["echo %f"],
					help="Specify the command(s) to run on the changed file. Use %%f to refer to the file inside the command.")
parser.add_argument("-p", "--path", default=".", type=str, help="Directory or file to watch.")
parser.add_argument("-o", "--once", default=False, action="store_true", help="Run the task only on the first change. Then exit.")
parser.add_argument("-i", "--initial", default=False, action="store_true", help="Run the task once initially, regardless whether there are any changes.")
parser.add_argument("-I", "--ignore-dirs", default=DEFAULT_IGNORE_DIRS, nargs="*", metavar="DIR", help="List of directories which are not watched.")
parser.add_argument("-d", "--debug", default=False, action="store_true", help="Show debug info.")
args = parser.parse_args()


cmd = "; ".join([c.replace("%f", "${filename}") for c in args.commands])
notify_cmd = "inotifywait --quiet --recursive {excludes} --event close_write,moved_to,create {dir} | while read -r directory events filename; do {cmd}; done".format(
	excludes = "--exclude '" + ("|".join([re.escape(d) for d in args.ignore_dirs])) + "'" if args.ignore_dirs else "",
	dir = path.abspath(path.join(".", args.path)) if not args.path.startswith("/") else args.path,
	cmd = cmd)

if args.debug:
	print(notify_cmd)
try:
	if args.initial:
		os.system(cmd)
	if args.once:
		proc.run(notify_cmd, shell=True)
	else:
		while True:
			proc.run(notify_cmd, shell=True)
except KeyboardInterrupt:
	print()
