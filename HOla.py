import random
import matplotlib.pyplot as plt

# Se crea el rango de movimientos y la cantidad de iteraciones
opciones = (-0.01, 0.01)
rango = [i*10 for i in range(101)]

# Se generan las 10 series de forma independiente en un diccionario
series = {}
for i in range(10):
    series[i] = [0]

# Para cada serie se itera 100 veces partiendo desde 0
for j in range(100):
    for i in range(10):
        seleccion = random.choice(opciones)
        series[i].append(round(series[i][-1] + seleccion, 4))

# Se genera el grafico adicionando cada serie
for i in range(10):
    plt.plot(rango, series[i], label=str(i+1))
plt.axis([0, 1000, -.5, .5])
plt.title('Caminata aleatoria Binomial en 1 segundo, 10 iteraciones')
plt.legend()
plt.ylabel('Distancia recorrida (m)')
plt.xlabel('Tiempo (ms)')
plt.show()
