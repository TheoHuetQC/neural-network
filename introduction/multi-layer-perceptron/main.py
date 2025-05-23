import numpy as np
import matplotlib.pyplot as plt
from mlp import MLP
from utils import generate_data, plot_classification, accuracy, mlp_networkx_view

############################### paramètres ###############################

# constante de numérisation :
Nt = 100 #nombre de prediction
Nx = 100 #nombre d'entrée

# constante du probleme
g = lambda x: np.exp(x)/4  # frontière de séparation
input_size = 2 # 2 car (x,y)
hide_layer_size1 = 3
hide_layer_size2 = 4
hide_layer_size3 = 8
output_size = 1 # 1 car on veut savoir au dessus ou en dessous de g

############################### Main ###############################

# creer notre reseau de neuronne simple (MLP)
mlp = MLP([input_size, hide_layer_size1,hide_layer_size2, output_size])

# initialisation des points aléatoires et du bon résultat a comparer avec nos prédictions 
x, y, inputs, z_true = generate_data(Nx, g) # on veut regarder si le point (x,y) est au dessus de (x,g(x))

# entraine notre perceptron
mlp.train(inputs, z_true, Nt)

# Prédictions finales
z_pred = np.array([mlp.forward(inputs[i]) for i in range(Nx)]) # donne des valeurs entre 0 et 1
z_pred_int =  np.array([mlp.predict_label(inputs[i]) for i in range(Nx)]) # donne soit 1 soit 0

# precision de notre perceptron
print(f"Précision : {accuracy(z_true, z_pred_int) * 100:.2f}%")

# Affichage des résultats finaux
plot_classification(x, y, z_pred, g, title="Prédictions du perceptron (bleu = au dessus, rouge = en dessous)")

mlp_networkx_view(mlp)
