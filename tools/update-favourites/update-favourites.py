#!/usr/bin/env python3
from subprocess import run
import argparse, json


# Captures the output of a command
def capture(command):
	return run(command, check=True, capture_output=True, universal_newlines=True).stdout


# Parse the supplied command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--add', nargs='*', default=[], help='Add an entry to the favourites list')
parser.add_argument('--remove', nargs='*', default=[], help='Remove an entry from the favourites list')
args = parser.parse_args()

# Retrieve the existing list of favourite applications
favourites = capture(['gsettings', 'get', 'org.gnome.shell', 'favorite-apps'])
favourites = json.loads(favourites.replace("'", '"'))

# Append any new entries that aren't already in the list
for newEntry in args.add:
	if newEntry not in favourites:
		favourites.append(newEntry)

# Filter out any entries that need to be removed
favourites = list([f for f in favourites if f not in args.remove])

# Save the updated list
command = ['gsettings', 'set', 'org.gnome.shell', 'favorite-apps', str(favourites)]
print(' '.join(command), flush=True)
run(command, check=True)
