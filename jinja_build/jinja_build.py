#!/usr/bin/env python

import sys, datetime, os
try:
    from jinja2 import Template
    from jinja2 import FileSystemLoader
    from jinja2.environment import Environment
except ImportError:
    print("Uh-oh! Looks like you don't have jinja2 installed!", file=sys.stderr)
    print("Go to http://jinja.pocoo.org/ and install it please!", file=sys.stderr)
    sys.exit(1)

def usage():
    print("jinga_build.py file.html repo_directory <templateDirectories>")
    print("\nBuilds a file specified by 'file.html', dumping to STDOUT the resulting HTML.\n")
    print("<templateDirectories> is one or more directories for templates to be housed,")
    print("separated by commas.\n")
    print("'repo_directory' is the path to the repo containing the site builder.")

if len(sys.argv) < 2 or len(sys.argv) > 4:
    usage()
    sys.exit()

filename = sys.argv[1]
templateFile = open(filename, 'r')
rawTemplate = templateFile.readlines()
templateFile.close()

strTemplate = "".join(rawTemplate)

env = Environment()
if len(sys.argv) == 4:
    p = sys.argv[3].split(',')
    env.loader = FileSystemLoader(p)
else:
    env.loader = FileSystemLoader(".")

builder = {
            'date' : '%s' % datetime.datetime.now(),
       }

template = env.from_string(strTemplate)
rendered = template.render(builder=builder)

print(rendered)

