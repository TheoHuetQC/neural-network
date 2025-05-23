import numpy as np
import matplotlib.pyplot as plt
from layer import Layer

class MLP :
    def __init__(self, perceptron_by_layer = [2,3,1]) :
        self.perceptron_by_layer = perceptron_by_layer
        self.layers = [Layer(perceptron_by_layer[i], perceptron_by_layer[i + 1])
                       for i in range(len(perceptron_by_layer) - 1)]
    
    def forward(self, output) : #on parcours les couches
        for layer in self.layers :
            output = layer.forward(output) # on avance a la couche d apres
        return output
    
    def backward(self, d_input) :
        for layer in reversed(self.layers) :
            d_input = layer.backward(d_input)

    def train(self, inputs, z_true, epochs) :
        losses = [] #pour sauvegarder la perte moyenne par époque
        for epoch in range(epochs) :
            loss_epoch = 0
            for i in range(len(inputs)) :
                # prediction
                z_pred = self.forward(inputs[i])
                # regarde la difference de sortie
                d_out = (z_pred - z_true[i])
                # ajustement des parametres en revenant en arrière
                self.backward(d_out)
                #calculs de la perte moyenne
                loss_epoch += self.binary_cross_entropy(z_true[i], z_pred)
            losses.append(loss_epoch / len(inputs))

            if epoch % 10 == 0 or epoch == epochs - 1 : #pour ne pas afficher a chaque pas de temps
                print(f"Epoch {epoch+1}/{epochs} - Loss: {losses[-1]:.4f}")
        #on pourrait return losses si besoin

    def binary_cross_entropy(self, z_true, z_pred) : # Calculer la perte (coût) Pour un problème de classification binaire 
        epsilon = 1e-8  # éviter log(0)
        return -np.mean(z_true * np.log(z_pred + epsilon) + (1 - z_true) * np.log(1 - z_pred + epsilon))

    def predict(self, inputs): #donne des valeurs entre 0 et 1
        z_pred = self.forward(inputs)
        return z_pred
    
    def predict_label(self, input): # donne soit 1 soit 0
        return int(self.forward(input) > 0.5)