class Color :
	def __init__(self) :
		self._colors = {"blue": "b", "red": "r", "black": "k","cyan" : "c","green": "g","magenta": "m","yellow" : "y"}

	def blue(self) :
		return self._colors["blue"]

	def red(self) :
		return self._colors["red"]

	def black(self) :
		return self._colors["black"]

	def cyan(self) :
		return self._colors["cyan"]

	def green(self) :
		return self._colors["green"]

	def magenta(self) :
		return self._colors["magenta"]

	def yellow(self) :
		return self._colors["yellow"]

class Form :
	def __init__(self):
		self._form = {"solid line" : "-", "dashed line" : "--", "dash-dot line" : "-.", "dotted line" : ":"}

	def get_solid(self):
		return self._form["solid line"]

	def get_dashed(self):
		return self._form["dashed line"]

	def get_dash_dot(self):
		return self._form["dash-dot line"]

	def get_dotted(self):
		return self._form["dotted line"]

class LineStyle:
	def __init__(self,couleur,forme = "-"):
		self._couleur = couleur
		self._forme = forme

	def get_style(self):
		return self._couleur + self._forme

	def get_couleur(self):
		return self._couleur

	def get_forme(self):
		return self._forme

	def set_couleur(self,couleur):
		self._couleur = couleur

	def set_forme(self,forme):
		self._forme = forme












