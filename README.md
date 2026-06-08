# CCSE Quiz (Preguntas CCSE)

Este es un sitio web estático interactivo para practicar las preguntas del examen CCSE (Conocimientos Constitucionales y Socioculturales de España).

Funciona de forma completamente local en el navegador, cargando las preguntas desde archivos JSON locales.

## Características

- **Modo Practicar:** Preguntas aleatorias una a una con retroalimentación instantánea.
- **Modo Test:** Simulador de examen oficial con 25 preguntas distribuidas por categorías oficiales (10 de política, 3 de derechos, 2 de geografía, 3 de cultura, y 7 de práctica).
- **Resultados:** Historial de aciertos y revisión de fallos detallada al finalizar el test.

## Ejecución Local

Para ejecutar el proyecto localmente y evitar problemas de CORS al cargar los archivos JSON, inicia el servidor HTTP de Python:

```bash
python server.py [puerto]
```

O si prefieres no usar el script, puedes iniciar el servidor integrado de Python directamente:

```bash
python -m http.server 8080
```

Luego abre en tu navegador:
`http://localhost:8080/index.html`

## Despliegue en GitHub Pages

Este repositorio está preparado para ser alojado de forma gratuita en GitHub Pages:

1. Crea un nuevo repositorio en GitHub.
2. Sube los archivos de este directorio a tu repositorio.
3. Ve a **Settings** (Configuración) > **Pages** de tu repositorio.
4. En la sección **Build and deployment**, selecciona la rama principal (`main` o `master`) y la carpeta `/root`, luego haz clic en **Save**.
5. Tu sitio estará disponible públicamente en la dirección provista por GitHub (por ejemplo, `https://tu-usuario.github.io/ccse/`).
