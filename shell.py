import os
import atexit
import readline
import rlcompleter

historyPath = (".projectcmdhistory")
os.environ['PYTHONINSPECT'] = 'True'


def save_history(historyPath=historyPath):
	import readline
	readline.write_history_file(historyPath)


if os.path.exists(historyPath):
	readline.read_history_file(historyPath)

atexit.register(save_history)
del os, atexit, readline, rlcompleter, save_history, historyPath
