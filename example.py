import sos

try:
	4 / 0
except Exception as e:
	sos.search(e)
