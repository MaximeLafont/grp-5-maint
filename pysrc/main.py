############################### Projet Math-Info : Sujet 5 ###############################
from tools.axis import Axis
from tools.cnds_initiales import Initials
from tools.line_style_form import LineStyle , Color , Form
from tools.phase_diag import PhaseDiag
from tools.fonctions import *
from mdl.systemeProjet import SystemeProjet

cnds = Initials()
col = Color()
frm = Form()
red_solid =  LineStyle(col.red(),frm.get_solid())
cnds.append((5,5),red_solid)
r1 = 0.8
r2 = 0.5
K1 = 50
K2 = 50
alpha = 0.6
beta = 0.4
gamma = 0
delta = 0
xaxis = Axis(0,K1,15j,"Axe x")
yaxis = Axis(0,K2,15j,"Axe y")
taxis = Axis(0,1000,5000,"Axe t")
Projet  = SystemeProjet(r1,r2,K1,K2,alpha,beta,gamma,delta,"Projet")
phases = PhaseDiag(Projet.get_title(),figsize=(9,9))
phases.portrait(Projet , cnds , xaxis , yaxis , taxis,exprtpng=False ,showfield=True)