# Abre el archivo en modo lectura y binario (rb)
with open('forms.py', 'rb') as f:
    content = f.read()

# Elimina los bytes nulos del contenido
content = content.replace(b'\x00', b'')
print(content)

# Vuelve a escribir el archivo con los bytes nulos eliminados
with open('forms.py', 'wb') as f:
    f.write(content)
    print('corrio')
