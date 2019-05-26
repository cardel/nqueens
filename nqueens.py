# -*- coding: utf-8 -*- 
import numpy as np
import random as rnd
import math

#La solución es un arreglo y la función de fitnees es que tanto se cruzan las reinas.
def obtenerFitness(poblacion):
	
	fitness = np.array([])
	
	#Contar el numero de veces que las reinas se interceptan
	for individuo in poblacion:
		
		#Contadores
		coincidenciasFila = 0
		coincidenciasDiagIzq = 0
		coincidenciasDiagDer = 0		
		for pos in range(0, individuo.shape[0]):
			
			filaActual = individuo[pos]
			#Contar coincidencias en la fila
			for posC in range(0, individuo.shape[0]):
				if pos != posC:
					if individuo[pos] == individuo[posC]:
						coincidenciasFila += 1
			
			
			#Contar diagonales izquierda inferior
			colIzq = individuo[pos]+1
			for i in range(pos+1, individuo.shape[0]):
				if individuo[i] == colIzq:
					coincidenciasDiagIzq += 1
				
				colIzq += 1
				
			#Contar diagnonales derecha inf
			codDer = individuo[pos]-1
			for i in range(pos-1,-1, -1):
				if individuo[i] == codDer:
					coincidenciasDiagDer += 1
				
				codDer -= 1					
		
		#Ajustamos
		total = coincidenciasDiagDer + coincidenciasDiagIzq + coincidenciasFila
		fitness = np.append(fitness, total)


	return fitness
	
def algoritmo(n, max_it, num_indv):
	mejor_individuo = 0
	
	#Supongo un tablero n por n
	poblacion = np.random.randint(n, size=(num_indv,n))
	
	for i in range(0, max_it):
		fitness = obtenerFitness(poblacion)
		
	
		#Aplicamos selección por ruleta
		ruleta = np.max(fitness) - fitness
		ruleta = ruleta.astype(float)
		
		ruleta = ruleta/(np.sum(ruleta)+1)
		indiceR = np.argsort(ruleta)
		ruleta = np.sort(ruleta)
		
		#Genero la suma incremental
		for i in range(1,ruleta.shape[0]):
			ruleta[i] = ruleta[i-1]+ruleta[i]
		
		
		
		mejor_individuo = poblacion[indiceR[0]]
		fitnessMejor = fitness[indiceR[0]]

		#Rehacemos población con el cruce
		poblacionNueva = np.array([])
		for j in range(0, num_indv):
			
			aleatorio1 = rnd.random()
			aleatorio2 = rnd.random()
			pos1 = 0
			pos2 = 0
			for k in range(0, ruleta.shape[0]):
				if ruleta[k] >= aleatorio1:
					pos1 = k
		
				if ruleta[k] >= aleatorio2:
					pos2 = k
			
			#Realizamos el cruce
			slice1 = int(math.ceil(n/2))
			slice2 = n


			nuevoIndividuo = np.append(poblacion[indiceR[pos1]][0:slice1],poblacion[indiceR[pos2]][slice1:slice2])
			poblacionNueva= np.append(poblacionNueva, nuevoIndividuo)
		poblacion = poblacionNueva.reshape(num_indv,n)
	
	return mejor_individuo, fitnessMejor


n = 4
max_it = 200
num_ind = 200
solucion = algoritmo(n,max_it,num_ind)
print(solucion)

