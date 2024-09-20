# Implementación de RSA y ElGamal en Python

Este repositorio presenta la implementación de dos algoritmos criptográficos: RSA y ElGamal. Ambos algoritmos se utilizan para cifrar y descifrar mensajes de texto. Además, el algoritmo ElGamal incluye una funcionalidad de firma digital para asegurar la autenticidad de los mensajes.

## Algoritmos Implementados

### 1. RSA:
RSA es un algoritmo de clave pública basado en la factorización de grandes números primos. Este proyecto incluye las siguientes funciones:
- **Generación de claves públicas y privadas**.
- **Cifrado y descifrado** de mensajes utilizando representación ASCII.
  
**Archivo**: `RSA.py`

### 2. ElGamal:
ElGamal es un algoritmo de cifrado basado en la aritmética modular y la dificultad del logaritmo discreto. Este proyecto incluye:
- **Generación de claves públicas y privadas**.
- **Cifrado y descifrado** de mensajes en formato ASCII.
- **Firma digital** para garantizar la integridad del mensaje.
  
**Archivo**: `elgamal.py`

## Archivos Incluidos
- **`RSA.py`**: Implementación del algoritmo RSA con generación de claves y operaciones de cifrado y descifrado.
- **`elgamal.py`**: Implementación del algoritmo ElGamal, incluyendo generación de claves, cifrado, descifrado y firma digital.

## Ejecución

### RSA:
1. Para ejecutar el script de RSA:
   ```bash
   python3 RSA.py
