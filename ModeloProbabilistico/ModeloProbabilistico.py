from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



# Datos de ejemplo (horas de estudio, durmió bien: 1 sí, 0 no)
# X son las características
X = [
    [2, 0],  # poco estudio, no durmió
    [4, 1],  # regular estudio, sí durmió
    [6, 1],  # buen estudio, sí durmió
    [1, 0],
    [3, 1],
    [5, 0],
    [7, 1],
    [8, 1]
]

# y es la etiqueta: 1 = aprobó, 0 = no aprobó
y = [0, 1, 1, 0, 0, 1, 1, 1]

# Dividimos los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Creamos el modelo Naive Bayes
modelo = GaussianNB()

# Entrenamos el modelo
modelo.fit(X_train, y_train)

# Hacemos predicciones
y_pred = modelo.predict(X_test)

# Mostramos resultados
print("Predicciones:", y_pred)
print("Valores reales:", y_test)
print("Precisión del modelo:", accuracy_score(y_test, y_pred))

# Probamos una nueva predicción
nuevo_estudiante = [[5, 1]]  # 5 horas de estudio y sí durmió
prediccion = modelo.predict(nuevo_estudiante)
print("¿El nuevo estudiante aprueba?", "Sí" if prediccion[0] == 1 else "No")
