class Axis:
	def __init__(self,debut,fin,N,label=""):
		self._debut = debut
		self._fin = fin
		self._N = N
		self._label = label

	def set_start(self,debut):
		self._debut = debut

	def get_start(self):
		return self._debut

	def set_end(self,fin):
		self._fin = fin

	def get_end(self):
		return self._fin

	def set_size_subdiv(self,N):
		self._N = N

	def get_size_subdiv(self):
		return self._N

	def set_label(self,label):
		self._label = label

	def get_label(self):
		return self._label

