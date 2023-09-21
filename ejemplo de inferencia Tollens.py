# Definimos una función que implementa el modus tollens
def modus_tollens(P, Q, q):
  # Si P implica Q y Q es falso, entonces P es falso
  if P and not q:
    return not P
  else:
    return None

# Definimos una premisa P: si es martes
P = "si es martes"
# Definimos una conclusión Q: hay clase
Q = "hay clase"
# Definimos un hecho q: no hay clase
q = False

# Aplicamos la función modus_tollens con los argumentos P, Q y q
resultado = modus_tollens(P, Q, q)

# Imprimimos el resultado
print(resultado)