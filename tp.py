#! /usr/local/bin/python3

import sys, subprocess, fileinput, re

def run_return(command, wd=None, shell=False):
    res = subprocess.check_output(command.split(), cwd=wd, encoding='utf8')
    return res.strip()

for entry in fileinput.input():
    if 'nl' in locals(): print()
    print(entry.strip())
    match = re.search('is (/.*)', entry)
    if match:
        target_file, source_file = '/', match.group(1) # ex. /usr/local/bin/python3
        while source_file:
            target_dir = run_return('dirname ' + target_file)
            # print(target_dir)
            source_file = run_return('realpath -s ' + source_file)
            # print(f'source_file = {source_file}')
            if target_file != '/': print('-> ', source_file)
            ls_out = run_return('ls -lF ' + source_file)
            print('ls_out ', ls_out)
            match = re.search(r'(/.*?)(?:@ -> |$)(.*)', ls_out)
            target_file, source_file = match.groups()
    nl = True
