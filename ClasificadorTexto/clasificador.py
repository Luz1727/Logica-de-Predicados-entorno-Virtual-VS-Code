# Importamos las librerías necesarias
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Datos de entrenamiento: Comentarios en español con sus respectivas etiquetas (1 = positivo, 0 = negativo)
comentarios = [
    "Este producto es excelente, me encantó.",  # Positivo
    "La calidad es muy buena, lo recomiendo totalmente.",  # Positivo
    "Muy mal, llegó roto y no funciona.",  # Negativo
    "No me gustó, esperaba algo mejor.",  # Negativo
    "Estoy muy satisfecho con la compra, superó mis expectativas.",  # Positivo
    "Horrible, no lo compren, es un fraude.",  # Negativo
    "Buen precio y funciona bien, lo compraría de nuevo.",  # Positivo
    "No sirve para nada, dinero tirado a la basura.",  # Negativo
    "Pésimo, no lo recomiendo para nada.",  # Negativo
    "Increíble producto, calidad insuperable.",  # Positivo
    "Terrible experiencia, nunca compraré aquí otra vez.",  # Negativo
]

# Etiquetas de los comentarios (1 = positivo, 0 = negativo)
etiquetas = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]

# Creamos el modelo con un vectorizador TF-IDF y el clasificador Naive Bayes
modelo = make_pipeline(TfidfVectorizer(stop_words=None), MultinomialNB())

# Entrenamos el modelo con los datos de entrenamiento
modelo.fit(comentarios, etiquetas)

# Comentarios nuevos para clasificar
nuevos_comentarios = [
    "Es un buen producto, la calidad es increíble.",
    "Pésimo, no cumplió mis expectativas.",
    "Excelente, lo recomiendo totalmente."
]

# Predicción de las categorías de los nuevos comentarios
predicciones = modelo.predict(nuevos_comentarios)

# Mostramos los resultados
for i, comentario in enumerate(nuevos_comentarios):
    categoria = "Positivo" if predicciones[i] == 1 else "Negativo"
    print(f'"{comentario}" → Clasificación: {categoria}')
