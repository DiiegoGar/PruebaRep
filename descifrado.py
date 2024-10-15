from collections import Counter

# Frecuencias de letras en español (ordenadas de mayor a menor)
frecuencia_espanol = {
    'e': 16.78, 'a': 11.96, 'o': 8.69, 'l': 8.37, 's': 7.88, 'n': 7.01, 
    'd': 6.87, 'r': 4.94, 'u': 4.80, 'i': 4.15, 't': 3.31, 'c': 2.92, 
    'm': 2.12, 'p': 2.77, 'b': 0.92, 'h': 0.89, 'q': 1.53, 'f': 0.52, 
    'v': 0.39, 'j': 0.30, 'g': 0.73, 'y': 1.54, 'x': 0.06, 'z': 0.15, 
    'k': 0.00, 'w': 0.00
}

# Texto cifrado
mensaje_cifrado = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX 
ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, 
RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE 
AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI 
XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI 
ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE 
RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE 
AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."""

# Función para contar la frecuencia de letras en el mensaje cifrado
def contar_frecuencia(mensaje):
    # Contamos solo las letras (ignoramos espacios, puntuaciones)
    letras = [letra for letra in mensaje if letra.isalpha()]
    contador = Counter(letras)
    total_letras = sum(contador.values())
    
    # Convertimos a porcentaje
    frecuencia = {letra: (contador[letra] / total_letras) * 100 for letra in contador}
    return frecuencia

# Función para ordenar un diccionario por sus valores (de mayor a menor)
def ordenar_por_frecuencia(diccionario):
    return dict(sorted(diccionario.items(), key=lambda item: item[1], reverse=True))

# Función para crear el diccionario de sustitución basándose en las frecuencias
def crear_diccionario_sustitucion(frecuencia_mensaje, frecuencia_espanol):
    letras_mensaje = list(frecuencia_mensaje.keys())
    letras_espanol = list(frecuencia_espanol.keys())
    
    # Creamos un diccionario que mapea las letras del mensaje cifrado con las letras del español
    diccionario_sustitucion = {}
    for i in range(min(len(letras_mensaje), len(letras_espanol))):
        diccionario_sustitucion[letras_mensaje[i]] = letras_espanol[i]
    
    return diccionario_sustitucion

# Función para descifrar el mensaje usando el diccionario de sustitución
def descifrar_mensaje(mensaje, diccionario_sustitucion):
    mensaje_descifrado = ""
    for letra in mensaje:
        if letra in diccionario_sustitucion:
            mensaje_descifrado += diccionario_sustitucion[letra]
        else:
            mensaje_descifrado += letra
    return mensaje_descifrado

# Paso 1: Contar la frecuencia de letras en el mensaje cifrado
frecuencia_mensaje = contar_frecuencia(mensaje_cifrado)

# Paso 2: Ordenar las frecuencias en ambos casos (mensaje cifrado y español)
frecuencia_mensaje_ordenada = ordenar_por_frecuencia(frecuencia_mensaje)
frecuencia_espanol_ordenada = ordenar_por_frecuencia(frecuencia_espanol)

# Paso 3: Crear el diccionario de sustitución
diccionario_sustitucion = crear_diccionario_sustitucion(frecuencia_mensaje_ordenada, frecuencia_espanol_ordenada)

# Paso 4: Descifrar el mensaje
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, diccionario_sustitucion)

# Mostrar el mensaje descifrado
print("Mensaje Descifrado (tentativo):")
print(mensaje_descifrado)

