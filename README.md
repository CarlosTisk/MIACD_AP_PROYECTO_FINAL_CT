# Proyecto Final - MIACD AP

Este repositorio contiene el cuaderno final del proyecto de la asignatura **MIACD AP**.  
Se incluyen dos formatos para facilitar tanto la lectura como la ejecución del contenido.

---

## 📂 Archivos incluidos
- **MIACD_AP_PROYECTO_FINAL.ipynb** → Cuaderno en formato Jupyter Notebook.  
  Diseñado para ejecutarse en **Google Colab**, ya que incluye integración con Google Drive.  

- **MIACD_AP_PROYECTO_FINAL.md** → Versión en Markdown, pensada para lectura directa en GitHub sin necesidad de ejecutar el código.  

- **requirements.txt** → Lista de librerías necesarias en caso de que alguien quiera ejecutar el proyecto fuera de Colab.  

---

## ▶️ Cómo ejecutar el cuaderno

### Google Colab (único método soportado oficialmente)
1. Abre el archivo `.ipynb` en Google Colab usando este enlace:

   [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USUARIO/REPO/blob/main/MIACD_AP_PROYECTO_FINAL.ipynb)

2. Asegúrate de **conceder permisos de acceso a tu Google Drive** cuando el cuaderno lo solicite.  
   Esto es necesario para leer y escribir archivos durante la ejecución.  

---

## 📁 Datos, modelos y resultados

Durante la ejecución, el notebook entrenará modelos y generará resultados, los cuales se guardarán en **Google Drive del usuario que lo ejecute**.  

> ⚠️ Importante:  
> - **Los modelos preentrenados no se incluyen en este repositorio**.  
> - Cada usuario debe entrenar sus propios modelos siguiendo las instrucciones del notebook.  
> - Se recomienda crear en tu Drive una carpeta con la siguiente estructura:
>
> ```
> /MIACD_AP_PROYECTO_FINAL/
>     ├── modelos/      # Para guardar modelos entrenados
>     ├── resultados/   # Para gráficos, métricas, reportes
>     └── datos/        # Conjunto de datos de entrada
> ```
>
> De este modo podrás organizar de manera clara tu ejecución del proyecto.  

---

## 📦 Requisitos
En Google Colab no es necesario instalar nada adicional: todas las librerías ya están disponibles.  

Si deseas ejecutar el cuaderno en otro entorno, instala las dependencias con:

```bash
pip install -r requirements.txt
