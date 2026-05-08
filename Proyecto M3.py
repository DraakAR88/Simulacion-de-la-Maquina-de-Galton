import random
import matplotlib.pyplot as plt

def simular_galton(num_canicas, niveles):
    """
    Simula la caída de canicas en una máquina de Galton.
    Retorna una lista con la posición final de cada canica.
    """
    resultados_finales = []
    
    for _ in range(num_canicas):
        posicion = 0
        # 12 niveles: la canica decide ir a la izquierda (-1) o derecha (+1)
        for _ in range(niveles):
            # random.choice([-1, 1]) representa 50% izq, 50% der
            posicion += random.choice([-1, 1])
        resultados_finales.append(posicion)
        
    return resultados_finales

def graficar_histograma(datos, niveles):
    """
    Grafica el histograma de los resultados de la simulación.
    """
    # Configuramos el histograma
    # Los contenedores van desde -niveles hasta +niveles
    plt.figure(figsize=(10, 6))
    
    # Creamos un histograma centrado en los números de ranuras
    plt.hist(datos, bins=range(-niveles, niveles + 2), align='left', 
             color='skyblue', edgecolor='black', rwidth=0.8)
    
    # Etiquetas y título
    plt.title(f'Simulación Máquina de Galton\n({len(datos)} canicas, {niveles} niveles)', fontsize=14)
    plt.xlabel('Posición Final del Contenedor (Desviación del centro)', fontsize=12)
    plt.ylabel('Cantidad de Canicas', fontsize=12)
    plt.grid(axis='y', alpha=0.5)
    
    # Mostramos el gráfico
    plt.show()

# --- Parámetros ---
NUM_CANICAS = 3000
NIVELES = 12

# --- Ejecución ---
# 1. Simular
posiciones = simular_galton(NUM_CANICAS, NIVELES)

# 2. Graficar
graficar_histograma(posiciones, NIVELES)