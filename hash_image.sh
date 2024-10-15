#!/bin/bash

# Archivo de imagen
IMAGE="imagen22.jpg"

# Generar el hash MD5
HASH=$(md5sum "$IMAGE" | awk '{print $1}')

# Crear una copia de la imagen y añadir el hash al final
cp "$IMAGE" "${IMAGE%.jpg}_hashed.jpg"
echo "$HASH" >> "${IMAGE%.jpg}_hashed.jpg"

echo "Hash MD5 añadido a la imagen."

# Verificación
head -c -33 "${IMAGE%.jpg}_hashed.jpg" > temp_image.jpg
CALCULATED_HASH=$(md5sum temp_image.jpg | awk '{print $1}')

if [ "$HASH" == "$CALCULATED_HASH" ]; then
    echo "La imagen es auténtica y no ha sido modificada."
else
    echo "La imagen ha sido modificada o no es auténtica."
fi

# Elimina el archivo temporal
rm temp_image.jpg

