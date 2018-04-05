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
usage: watchexec.py [-h] [-p PATH] [-o] [-i] [-I [DIR [DIR ...]]] [-d]
                    [commands [commands ...]]

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
  -i, --initial         Run the task once initially, regardless whether there
                        are any changes. (default: False)
  -I [DIR [DIR ...]], --ignore-dirs [DIR [DIR ...]]
                        List of directories which are not watched. (default:
                        ['.git', '.svn'])
  -d, --debug           Show debug info. (default: False)
```

#### License

[<img src='https://img.shields.io/badge/license-CC0-blue.svg'/>](https://creativecommons.org/publicdomain/zero/1.0)

This is free software, and to the extent possible under law, all copyright and related or neighboring rights to this work are waived.
You may use this code, or parts of it, freely and *without* attribution for any purpose.
