#!/bin/bash

# Ruta de la plantilla Nginx dentro del proyecto
TEMPLATE="${NGINX_TEMPLATE_PATH:-./nginx_templates/crystalitservice.com}"

# Solicita el dominio
read -p "👉 Ingresa el nuevo dominio (ej: empresa1.com): " dominio
dominio_www="www.${dominio}"
archivo="/etc/nginx/sites-available/${dominio}"

# Verifica que la plantilla exista
if [ ! -f "$TEMPLATE" ]; then
  echo "❌ No se encontró la plantilla base en: $TEMPLATE"
  exit 1
fi

# Copiar la plantilla al archivo destino
cp "$TEMPLATE" "$archivo"

# Reemplazar dominios en el archivo
sed -i "s/www\.crystalitservice\.com/${dominio_www}/g" "$archivo"
sed -i "s/crystalitservice\.com/${dominio}/g" "$archivo"

# Crear enlace simbólico en sites-enabled (si no existe)
if [ ! -L /etc/nginx/sites-enabled/${dominio} ]; then
  ln -s "$archivo" /etc/nginx/sites-enabled/
fi

# Verificar la configuración de Nginx
echo "🔍 Verificando configuración de Nginx..."
nginx -t
if [ $? -ne 0 ]; then
  echo "❌ Error en la configuración Nginx. Corrige antes de continuar."
  exit 1
fi

# Recargar Nginx
echo "🔄 Recargando Nginx..."
systemctl reload nginx

# Ejecutar Certbot para HTTPS
echo "🔒 Solicitando certificado SSL para $dominio y $dominio_www..."
certbot --nginx -d "$dominio" -d "$dominio_www"

echo "✅ Listo. El dominio https://${dominio_www} está configurado correctamente."

