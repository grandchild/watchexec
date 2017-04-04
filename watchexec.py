#!/usr/bin/env python3
import argparse
import subprocess as proc
import os.path as path


parser = argparse.ArgumentParser(
	description="Run command whenever files in the path change.",
	formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("commands", nargs="*", default=["echo %f"],
					help="Specify the command(s) to run on the changed file. Use %%f to refer to the file inside the command.")
parser.add_argument("-p", "--path", default=".", type=str, help="Directory or file to watch.")
parser.add_argument("-o", "--once", default=False, action="store_true", help="Run the task only on the first change. Then exit.")
parser.add_argument("-d", "--debug", default=False, action="store_true", help="Show debug info.")
args = parser.parse_args()



notify_cmd = "inotifywait --quiet --recursive --event close_write,moved_to,create {dir} | while read -r directory events filename; do {cmd}; done".format(
	dir = path.abspath(path.join(".", args.path)) if not args.path.startswith("/") else args.path,
	cmd = "; ".join([c.replace("%f", "${filename}") for c in args.commands]))

if args.debug:
	print(notify_cmd)
try:
	if args.once:
		proc.run(notify_cmd, shell=True)
	else:
		while True:
			proc.run(notify_cmd, shell=True)
except KeyboardInterrupt:
	print()
