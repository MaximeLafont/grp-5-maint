from tools.line_style_form import LineStyle
class Initial:
	def __init__(self,coord,parametre = {"color" : "b", "form" : "-"}):
		self._coord = coord
		self._param = parametre


	def set_cords(self,x,y):
		self._coord = (x,y)

	def get_cords(self):
		return self._coord

	def get_style(self):
		return self._param["color"] + self._param["form"]


	def set_param(self,couleur,forme):
		self._param["color"] = couleur
		self._param["form"] = forme

	def get_param(self):
		return self._param

class Initials:

	def __init__(self,liste = []):
		self._liste = liste

	def get_cnds(self):
		return self._liste 

	def set_cnds(self,liste):
		self._liste = liste


	def generateur_cnds(self,lx,ly,param = LineStyle("b","-")):
		couleur = param.get_couleur()
		forme = param.get_forme()
		liste = []
		for u in lx:
			for v in ly:
				liste.append(Initial((u,v),{"color" : couleur, "form" : forme}))
		return liste


	def append(self,coord,param = LineStyle("b","-")):
		couleur = param.get_couleur()
		forme = param.get_forme()
		self._liste.append(Initial(coord,{"color" : couleur, "form" : forme}))










