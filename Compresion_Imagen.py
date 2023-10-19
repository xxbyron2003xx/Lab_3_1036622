from PIL import Image

# Abrir una imagen
imagen_original = Image.open('imagen_original')

# Guardar la imagen en formato PNG (compresión sin pérdida)
imagen_original.save('imagen_comprimida.png', 'PNG')

# También puedes especificar opciones adicionales, como la compresión sin filtro
imagen_original.save('imagen_comprimida_con_filtro.png', 'PNG', optimize=False)

# Guardar con opciones adicionales, como la compresión sin filtro y sin paleta
imagen_original.save('imagen_comprimida_sin_filtro_sin_paleta.png', 'PNG', optimize=False, bits=8)
