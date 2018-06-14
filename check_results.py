# me is this DAT.
# 
# frame is the current frame.
# state is true if the timeline is paused.
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def start():
	return

def create():
	return

def exit():
	return

# Every frame it checks if there are resuts to append to table
def frameStart(frame):
	try:
		inQ = me.parent().fetch('inQ')
		value = inQ.get_nowait()
		op('results').appendRow(value)
	except:
		# nothing new yet
		pass
	return

def frameEnd(frame):
	return

def playState(state):
	return
	