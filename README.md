# WatchExec

#### Purpose
A command needs to be run whenever its source files change. This small script
uses `inotifywatch` to run a specified command, or list of commands, whenever
that happens.

#### Prerequisites
Install the ```inotify-tools``` package. It contains ```inotifywatch```.

#### Example
```bash
# Regenerate PDF when latex changes:
./watchexec.py "pdflatex -halt-on-errors %f > /dev/null"

# Compile and test when the files in src change:
./watchexec.py -p ./src make "make test"
```

#### Usage
```
usage: watchexec.py [-h] [-p PATH] [-o] [-d] [commands [commands ...]]

Run command whenever files in the path change.

positional arguments:
  commands              Specify the command(s) to run on the changed file. Use
                        %f to refer to the file inside the command. (default:
                        ['echo %f'])

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Directory or file to watch. (default: .)
  -o, --once            Run the task only on the first change. Then exit.
                        (default: False)
  -d, --debug           Show debug info. (default: False)
```
