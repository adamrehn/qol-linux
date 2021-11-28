#!/usr/bin/env python3
from os.path import abspath, basename, exists, expanduser, join
from pathlib import Path
from subprocess import run
import argparse, urllib.parse


# The default output directory
DEFAULT_OUTPUT_DIR='~/.local/share/applications'

# The default icon to use for directories that do not have a custom icon configured
DEFAULT_ICON = 'org.gnome.Nautilus'

# The template code for generating desktop entries
DESKTOP_ENTRY_TEMPLATE = '''[Desktop Entry]
Name={}
Comment=Open the {} directory
Keywords=folder;manager;explore;disk;filesystem;
Exec=nautilus "{}"
Icon={}
Terminal=false
Type=Application
Categories=GNOME;GTK;Utility;Core;FileManager;
'''


# Parse our command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('dir', help='The path to the directory for which a desktop entry should be created')
parser.add_argument('--outdir', default=DEFAULT_OUTPUT_DIR, help="The output directory to place the generated desktop entry in (defaults to {})".format(DEFAULT_OUTPUT_DIR))
args = parser.parse_args()

# Verify that the target directory exists
target = abspath(args.dir)
if not exists(target):
	raise RuntimeError('the directory "{}" does not exist!'.format(target))

# Determine if a custom icon has been configured for the target directory
# (Command details from here: <https://askubuntu.com/a/1235201>)
icon = DEFAULT_ICON
key = 'metadata::custom-icon: '
info = run(['gio', 'info', target], check=True, capture_output=True, universal_newlines=True).stdout.strip()
lines = [l.strip() for l in info.splitlines()]
for line in lines:
	if line.startswith(key):
		icon = urllib.parse.unquote(line.removeprefix(key)).replace('file://', '')

# Generate the desktop entry
name = basename(target)
outfile = join(expanduser(args.outdir), '{}.desktop'.format(name))
Path(outfile).write_text(DESKTOP_ENTRY_TEMPLATE.format(
	name,
	name,
	target,
	icon
))

# Mark the desktop entry as executable
run(['chmod', '+x', outfile], check=True)

# Inform the user that the entry was created successfully
print('Created desktop entry for "{}" at {}.'.format(target, outfile))
