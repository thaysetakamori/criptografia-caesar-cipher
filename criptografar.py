def criptografar(str, num):
    resultado = ""
    
    for letra in str:
        if letra.isalpha():
            deslocamento = num % 26
            
            if letra.isupper():
                inicio = ord('A')
            else:
                inicio = ord('a')
           
            nova_letra = chr(inicio + (ord(letra) - inicio + deslocamento) % 26)
            resultado += nova_letra
        else:
            resultado += letra
    
    return resultado

print(criptografar("Caesar Cipher", 2))