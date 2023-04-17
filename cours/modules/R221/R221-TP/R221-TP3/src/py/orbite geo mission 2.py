import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G

# Base du programme GPT4 23/3/2023
# Adaptation Philippe PUJAS 16/4/2023

# Mission 2 : Lancement avec mise en orbite GTO depuis une altitude donnée

# Constantes
M_earth = 5.972e24  # Masse de la Terre en kg
R_earth = 6371e3    # Rayon de la Terre en m
G_const = G         # Constante gravitationnelle en m^3 kg^-1 s^-2

# Fonctions
def v_circulaire(r, M=M_earth, G=G_const):
    """Retourne la vitesse tangentielle pour une orbite circulaire de rayon r donné."""
    # programmez ici la formule de Kepler 
    mu = M*G

    delta = np.sqrt((mu/r))

    # return 7788.4
    return delta

def v_elliptique(r,a, M=M_earth, G=G_const):
    """Retourne la vitesse tangentielle pour une orbite elliptique à une distance r donnée connaissant le 1/2 grand axe a."""
    # programmez ici la formule de Kepler 
    mu = M*G
    b = (2/r) - (1/a)

    delta = np.sqrt(mu * b)

    return delta

def a_elliptique(r,v, M=M_earth, G=G_const):
    """Retourne le demi-grand axe si la vitesse vaut v à une distance r donnée d'une orbite initialement elliptique."""
    # programmez ici la formule déduite de la loi de Kepler 

    mu = M*G
    v_square_times_r = (v**2)*r
    two_mu = 2*mu
    bottom_part = v_square_times_r - two_mu
    a = (mu * r) / bottom_part
    print(a, -a, True if round(-a) == 6571000 else False)
    return -a

    #return 6571000

def e_ellipse(r_per,a):
    """Retourne l'excentricité d'une ellipse de périapse r_per et de demi-grand axe a."""
    excentricity = 1 - (r_per / a)
    return excentricity

def plot_orbite(a, e, color, label):
    """Dessine une orbite elliptique de demi-grand axe a et d'excentricité e, en utilisant les coordonnées polaires."""
    theta = np.linspace(0, 2 * np.pi, 1000)
    r = a * (1 - e**2) / (1 + e * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y, color=color, label=label)

# Paramètres de l'orbite GEO
h_geo = 35.786e6  # altitude de l'orbite géostationnaire en m
r_geo = R_earth + h_geo  # Rayon de l'orbite géostationnaire en m = apogée GTO

# Paramètre de l'orbite à la fin du lancement
# Ajoutez une saisie clavier de l'altitude h_lan
h_lancement = 200e3  # Le lanceur dépose le satellite à cette altitude en m
r_lancement = R_earth + h_lancement  # rayon au point de largage en m

# Vous programmerez cette vitesse en utilisant la loi de Kepler
# vitesse tangentielle à la séparation
v_lancement = v_circulaire(r_lancement) # Utilisez la fonction une fois celle-ci programmée
v_lancement += 2456.49   # Surplus de vitesse pour avoir une orbite GTO depuis h=200km



# Programmer la formule qui donne le 1/2 grand-axe en fonction de la vitesse au périgée
a_lancement=a_elliptique(r_lancement, v_lancement) # Utilisez la fonction une fois celle-ci programmée



# on suppose que le périapse est le point de largage
r_per_lancement = r_lancement

# Calculer ici l'apoapse en fonction de a_lancement et du périapse
r_apo_lancement = 2*a_lancement-r_per_lancement

# Ce morceau s'assure que le périapse est plus petit que l'apoapse et sinon les permute
if r_per_lancement > r_apo_lancement:
    r_per_lancement,r_apo_lancement = r_apo_lancement, r_per_lancement
    
# Programmer l'excentricité de l'ellipse en fonction de r_per_lancement et de a_lancement
e_lancement = e_ellipse(r_per_lancement,a_lancement)


# Affichage des orbites et de la Terre
plt.figure()
plt.gca().set_aspect('equal', adjustable='box')

terre = plt.Circle(( 0 , 0), R_earth, fill=True, color='blue' , label='Terre')
plt.subplot().add_patch(terre)
plot_orbite(a_lancement,e_lancement, color='red', label='Orbite de lancement')  # lorsqu'on connait la vitesse du lanceur à la fin de la propulsion
plot_orbite(r_geo, 0, color='green', label='Orbite géostationnaire')



plt.legend()
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Mission 2 : Orbite GTO")
plt.grid()
plt.show()
