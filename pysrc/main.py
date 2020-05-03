############################### Projet Math-Info : Sujet 5 ###############################
from tools.axis import Axis
from tools.cnds_initiales import Initials
from tools.line_style_form import LineStyle , Color , Form
from tools.phase_diag import PhaseDiag
from tools.fonctions import *
from mdl.systemeProjet import SystemeProjet
import matplotlib.pyplot as plt
cnds = Initials()
col = Color()
frm = Form()
red_solid =  LineStyle(col.red(),frm.get_solid())
cyan_solid =  LineStyle(col.cyan(),frm.get_solid())
yellow_solid =  LineStyle(col.yellow(),frm.get_solid())
param = ask_parameters()
cnds.append((param[8],param[9]),red_solid)
r1 = param[2]
r2 = param[3]
K1 = param[0]
K2 = param[1]
alpha = param[4] 
beta =  param[5]
gamma =  param[6]
delta = param[7]
xaxis = Axis(0,K1,20j,"Espece 1")
yaxis = Axis(0,K2,20j,"Espèce 2")
taxis = Axis(0,200,10000,"Axe t")
Projet  = SystemeProjet(r1,r2,K1,K2,alpha,beta,gamma,delta,"")
phases = PhaseDiag(Projet.get_title(),figsize=(9,9))
phases.portrait(Projet , cnds , xaxis , yaxis , taxis,exprtpng=False ,showfield=True)