# Definimos una función que implementa el modus ponens
def modus_ponens(P, Q, p):
  # Si P implica Q y P es verdadero, entonces Q es verdadero
  if P and p:
    return Q
  else:
    return None

# Definimos una premisa P: si llueve
P = "si llueve"
# Definimos una conclusión Q: el suelo está mojado
Q = "el suelo está mojado"
# Definimos un hecho p: llueve
p = True

# Aplicamos la función modus_ponens con los argumentos P, Q y p
resultado = modus_ponens(P, Q, p)

# Imprimimos el resultado
print(resultado)