import nltk
from nltk.sem.logic import Expression

read_expr = Expression.fromstring
josue = read_expr('josue')
israel = read_expr('israel')
juan = read_expr('juan')

amigos_josue_israel = read_expr('amigos(josue, israel)')
amigos_josue_Juan = read_expr('no_son_amigos(josue, juan)')
no_amigos_juan_israel = read_expr('tienen_la_misma_edad(juan, israel)')
trabajan_juntos_josue_israel = read_expr('trabajan(josue, israel)')

formulas = [
    amigos_josue_israel,
    amigos_josue_Juan,
    no_amigos_juan_israel,
    trabajan_juntos_josue_israel
]

for formula in formulas:
    print(f"{formula} : {formula}")
