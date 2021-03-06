#!/usr/bin/env python3

import sys
import json
import os.path
from os import path
import time
from datetime import datetime
# the below imports are quicknote .py files
import memory as mem
import helper_func as hf
import note


# Color Definitions
BOLD = '\033[1m'
ITALIC = '\033[3m'
RESET = '\033[0m'


"""
Returns access to the .quicknote_cache file, the .archive_notes and .notes directories
"""
def background_info():
	files = []
	# this file holds any miscellaneous information that Quick Note needs –– at the moment, just the current file
	data_file = path.expanduser('~/.quicknote/.background/data_file.json')
	# this directory holds available notes
	notes = path.expanduser('~/.quicknote/.notes')
	# this holds the name of the current note, as taken from data_file
	current_note = note.get_current_note(data_file)
	# this directory holds archived notes
	archive_notes = path.expanduser('~/.quicknote/.archive_notes')
	
	files.append(data_file)
	files.append(current_note)
	files.append(hf.read_directory(notes))
	files.append(hf.read_directory(archive_notes))
	return files


"""
Prints the user's version of Quick Note
"""
def get_version():
	print(BOLD + 'Quick Note v.1.0.6' + RESET) 
	print('If you would like to update, type \'remember --update')


"""
Prompts the user to update Quick Note
every month
"""


"""
Given the data_file, updates the user's
version of Quick Note
"""
def update_quick_note():
	print(datetime.now())
	# Save last date of update in data_file
	# Ask the user to update every month
	# they should be able to update on their own as well
	# make a send_update_message func to ask for update
	# make install.py add the data of install to the data_file
	# make a get_current_time func or something
	# or a func to write date_time to data_file


"""
Prints some help/usage information
"""
def get_help():
	get_version()
	print('\n', end='')
	print(BOLD + 'GENERAL' + RESET + '\n')
	print('\'Notes\' are files where we store your thoughts')
	print('\'Memories\' are the individual entries in each note\n')
	print(BOLD + 'MEMORIES' + RESET + '\n')
	print('If you would like to' + BOLD + ' add' + RESET + ' a memory, type \'remember' + ITALIC + ' your_memory' + RESET + '\'')
	print('If you would like to' + BOLD + ' view' + RESET + ' current memories, type \'remember --list\'')
	print('If you would like to' + BOLD + ' clear' + RESET + ' your current memories, type \'remember --clear\'')	
	print('If you would like to' + BOLD + ' remove' + RESET + ' a particular memory, type \'remember --remove' + ITALIC + ' row_number' + RESET + '\'')
	print('If you would like to' + BOLD + ' remove' + RESET + ' the last memory entered on a note, type \'remember --remove\'')
	print('If you would like to' + BOLD + ' move' + RESET + ' a memory to another note, type \'remember --move' + ITALIC + ' row_number other_note_name' + RESET + '\'')
	print('If you would like to' + BOLD + ' copy' + RESET + ' a memory to another note, type \'remember --copy' + ITALIC + ' row_number other_note_name' + RESET + '\'\n')
	print(BOLD + 'NOTES' + RESET + '\n')
	print('If you would like to' + BOLD + ' add' + RESET + ' a note, type \'remember --add-note' + ITALIC + ' note_name' + RESET + '\'')
	print('If you would like to' + BOLD + ' view' + RESET + ' current notes, type \'remember --list-notes\'')
	print('If you would like to' + BOLD + ' view' + RESET + ' the current note, type \'remember --current-note\'')
	print('If you would like to' + BOLD + ' change' + RESET + ' the current note, type \'remember --change-note' + ITALIC + ' note_name' + RESET + '\'')
	print('If you would like to' + BOLD + ' rename' + RESET + ' a note, type \'remember --rename-note' + ITALIC + ' note_to_rename' + RESET + ' / ' + ITALIC + 'new_name' + RESET + '\'')
	print('If you would like to' + BOLD + ' remove' + RESET + ' a particular note, type \'remember --remove-note' + ITALIC + ' note_name' + RESET + '\'')
	print('If you would like to' + BOLD + ' remove' + RESET + ' the current note, type \'remember --remove-note')
	print('If you would like to' + BOLD + ' clear' + RESET + ' your current notes, type \'remember --clear-notes\'')	
	print('If you would like to' + BOLD + ' import' + RESET + ' a note, type \'remember --import-note' + ITALIC + ' file_to_import' + RESET + ' / ' + ITALIC + 'note_name' + RESET + '\'')
	print('If you would like to' + BOLD + ' export' + RESET + ' a note, type \'remember --export-note' + ITALIC + ' note_to_export' + RESET + ' / ' + ITALIC + 'new_file_name' + RESET + '\'\n')
	print(BOLD + 'ARCHIVE' + RESET)
	print(ITALIC + 'Archived notes do not receive the same functionality as regular notes. To rename, remove, export, etc. archived notes, please unarchive them first.' + RESET + '\n')
	print('If you would like to' + BOLD + ' archive' + RESET + ' a particular memory, type \'remember --archive' + ITALIC + ' row_number' + RESET + '\'')
	print('If you would like to' + BOLD + ' archive' + RESET + ' the last memory entered on a note, type \'remember --archive\'')
	print('If you would like to' + BOLD + ' archive' + RESET + ' a particular note, type \'remember --archive-note' + ITALIC + ' note_name' + RESET + '\'')
	print('If you would like to' + BOLD + ' archive' + RESET + ' the current note, type \'remember --archive-note\'')
	print('If you would like to' + BOLD + ' unarchive' + RESET + ' a particular note, type \'remember --unarchive-note' + ITALIC + ' note_name' + RESET + '\'')
	print('If you would like to' + BOLD + ' view' + RESET + ' your archived notes, type \'remember --list-archived-notes\'')
	print('If you would like to' + BOLD + ' clear' + RESET + ' your archived notes, type \'remember --clear-archived-notes\'')	
	
	
	

"""
Prints some random info about Quick Note
"""
def info():
	print(BOLD + 'Quick Note' + RESET + ' is an open-source note-taking software designed for personal use')
	print('If you need help, type \'remember --help\'\n')
	print(BOLD + 'Quick Note' + RESET + ' uses the GNU General Public License v3, so you can edit, distribute, and otherwise meddle with any of the source code.')
	print('The only thing you can\'t do is take this software and make it closed-source and try to sell it. ' + BOLD + 'Quick Note' + RESET + ' was designed to be free for everyone, forever.')
	# print a random quote??


"""
Handles command line arguments and redirects to appropriate
helper functions. Should be further decomposed
"""
def main():
	# send_update_message()
	args = sys.argv[1:]
	files = background_info()

	data_file = files[0]
	current_note = files[1].strip('\n')
	notes = files[2]
	archive_notes = files[3]

	last_slash_index = current_note.rfind('/')	
	current_note_name = current_note[last_slash_index + 2:] 
	
	if len(args) == 0:
		info()
		return
	command = args[0]
	if len(args) == 1:
		if command == '--list':
			mem.list_memories(current_note, current_note_name)
		elif command == '--update':
			update_quick_note(data_file)
		elif command == '--clear':
			mem.clear_memories(current_note)
		elif command == '--help':
			get_help()
		elif command == '--version':
			get_version()
		elif command == '--list-notes':
			note.list_notes(notes) 
		elif command == '--current-note':
			print(current_note_name)
		elif command == '--clear-notes':
			note.clear_notes(notes, current_note_name, data_file)
		elif command == '--clear-archived-notes':
			note.clear_archive_notes(archive_notes)
		elif command == '--remove-note':
			note.remove_note(current_note_name, current_note_name, data_file)
		# this is for archiving the current note
		elif command == '--archive-note':
			note.archive_note(current_note_name, current_note_name, data_file)
		elif command == '--list-archived-notes':
			note.list_archive_notes(archive_notes)
		else:
			mem.add_memory(current_note, args)
	elif len(args) >= 1:
		if command == '--remove':
			mem.remove_memory(current_note, args[1])
		elif command == '--archive':
			mem.archive_memory(current_note, args[1])
		elif command == '--add-note':
			note.add_note(args[1:])
		elif command == '--change-note':
			note.change_note(args[1:], current_note, data_file)
		elif command == '--rename-note':
			note.rename_note(args[1:], current_note, data_file)
		# this is for removing any note
		elif command == '--remove-note':
			note.remove_note(args[1:], current_note_name, data_file)
		# this is for archiving any note
		elif command == '--archive-note':
			note.archive_note(args[1:], current_note_name, data_file)	
		elif command == '--unarchive-note':
			note.un_archive_note(args[1:])
		elif command == '--import-note':
			note.import_note(args[1:])
		elif command == '--export-note':
			note.export_note(args[1:])
		elif command == '--move-memory':
			mem.move_memory(current_note, args[1], args[2:])
		elif command == '--copy-memory':
			mem.copy_memory(current_note, args[1], args[2:])
		else:
			mem.add_memory(current_note, args)


if __name__ == '__main__':
	main()	

