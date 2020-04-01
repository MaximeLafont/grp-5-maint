import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from tools.field import Field
class PhaseDiag:
	def __init__(self, title="Portrait des phases", figsize=(10, 6)):
		self._title = title
		self._figsize = figsize

	def __str__(self):
		return self._title

	def get_title(self):
		return self._title

	def get_figsize(self):
		return self._figsize

	def portrait(self, modl, cndszr, xaxis, yaxis, taxis, exprtpng=False, showfield=True):

		fig, phases = plt.subplots(figsize=self.get_figsize())

		plt.xlim(xaxis.get_start(), xaxis.get_end()) 

		plt.ylim(yaxis.get_start(), yaxis.get_end())

		phases.grid(True) 

		phases.set_title(self.get_title()) 

		phases.set(xlabel=xaxis.get_label(),ylabel=yaxis.get_label())

		tdisc = np.linspace(taxis.get_start(), taxis.get_end(),taxis.get_size_subdiv())
		
		cndszero = cndszr.get_cnds() 

		for cnd in cndszero:
			cnd0 = cnd.get_cords()
			trj = odeint(modl.get_rhs(), cnd0, tdisc) 
			phases.plot(trj[:, 0], trj[:, 1], cnd.get_style())
			
		if showfield:
			field = Field() 
			field.plot(modl, xaxis, yaxis)

		plt.show()

		if exprtpng:
			figname = self.get_title() + ".png" 
			figname = figname.replace(" ", "_") 
			fig.savefig(figname)
