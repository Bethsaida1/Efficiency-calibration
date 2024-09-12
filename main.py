import numpy as np
import matplotlib.pyplot as plt
from numpy._core.fromnumeric import size

colores = ["orange", "red", "blue", "green", "purple"]
distancias = ["5,8cm", "20cm", "50cm", "100cm", "150cm"]
for i in range(len(distancias)):
  titulo = distancias[i]
  data = np.loadtxt(titulo)
  X = np.log(data[:, 0]) #ln(energía)
  Y = np.log(data[:, 2]) #ln(eficiencia)

  e = data[:, 0]
  DELTAe = data[:, 1]
  x_err = DELTAe / e

  eff = data[:, 2]
  DELTAeff = data[:, 3]
  y_err = DELTAeff / eff

  coef = np.polyfit(X, Y, 4)
  polinomio = np.poly1d(coef)

  x_ajustado = np.linspace(X.min(), X.max(), 100)
  y_ajustado = polinomio(x_ajustado)
  
  # Mostrar los resultados
  print(titulo)
  for n in range(len(coef)): 
    print(f"a{n} = {coef[ len(coef)-1-i ]}")

#Caso individual  
# Mostrar los resultados
#for i in range(len(coef)): 
#  print(f"a{i} = {coef[ len(coef)-1-i ]}")

# Valores ajustados/predecidos
#Y_pred = polinomio(X)

# Calcular chi cuadrado reducido
#p = len(coef)
#N = len(Y)
#grados_de_libertad = N - p
#chi_cuadrado = np.sum( ( (Y - Y_pred) / y_err )** 2 )
#chi_cuadrado_reducido = chi_cuadrado / grados_de_libertad
#print(f"χr² = {chi_cuadrado_reducido}")


  # Graficar los puntos y la recta ajustada
  plt.scatter(X, Y, color=colores[i], label=distancias[i], s=10)
  plt.plot(x_ajustado, y_ajustado, color='black', linewidth=0.5) #linestyle= "--"
  #plt.errorbar(X, Y, yerr=y_err, xerr=x_err, fmt=" ", color="black",     label="Error")
plt.xlabel('ln(Energy(keV))')
plt.ylabel('ln(Efficiency)')
plt.title("Efficiency calibration")
plt.legend()
plt.show()