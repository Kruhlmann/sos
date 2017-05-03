import webbrowser

def search(ex):
	template = "{0}: {1}"
	message = template.format(type(ex).__name__, ex.args[0])
	webbrowser.open('http://stackoverflow.com/search?q={0}'.format(message))