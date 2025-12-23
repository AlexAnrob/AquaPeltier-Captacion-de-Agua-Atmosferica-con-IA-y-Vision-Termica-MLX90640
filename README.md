<p align="center">
  <img src="https://github.com/AlexAnrob/Dispositivo-que-capta-agua-de-la-atmosfera-con-celdas-peltier-/blob/main/Logo.png" alt="Logo AquaPeltier" width="200"/>
</p>

<h1 align="center">AquaPeltier: Captación de Agua Atmosférica con IA y Visión Térmica MLX90640</h1>

Este repositorio presenta el desarrollo de un dispositivo experimental diseñado para **captar agua del aire de la atmósfera** mediante el uso de **celdas Peltier**. El sistema combina hardware de bajo costo con algoritmos de inteligencia artificial para registrar, analizar y clasificar el comportamiento del dispositivo en condiciones reales.

---

## 🌊 Funcionalidades principales
- Captación de agua atmosférica utilizando celdas Peltier.  
- Registro de datos ambientales mediante sensores integrados.  
- Clasificación automática con una red neuronal:  
  - **1** → cuando se detecta goteo de agua.  
  - **0** → cuando no se detecta goteo de agua.  
- Imágenes térmicas de las celdas Peltier, capturadas con una cámara **MLX90640** conectada a una **Raspberry Pi 3**.  
- Conjunto de datos térmicos generado a partir de estas imágenes, disponible para entrenamiento y validación de modelos.  
- Algoritmo de estimación de sensación térmica promedio en las zonas caliente y fría de la celda Peltier.  
- Código de captura de imágenes térmicas con la cámara MLX90640 para reproducibilidad y extensión del dataset.  

---

## 🎯 Objetivo
Explorar soluciones tecnológicas para la **obtención de agua potable a partir de la humedad ambiental**, integrando hardware accesible con algoritmos de **machine learning** y visión computacional.  

---

## 📂 Estructura del repositorio
- **/src** → Código fuente del sistema de adquisición y clasificación.  
- **/data** → Conjunto de datos registrados por los sensores y las imágenes térmicas.  
- **/models** → Implementación y entrenamiento de la red neuronal.  
- **/thermal** → Algoritmos para estimar la sensación térmica promedio en zonas caliente y fría.  
- **/capture** → Código para la captura de imágenes térmicas con MLX90640 y Raspberry Pi 3.  
- **/docs** → Documentación técnica y resultados experimentales.  

---

## 🚀 Futuro del proyecto
- Optimizar la eficiencia energética del sistema de captación.  
- Ampliar la base de datos de imágenes térmicas para mejorar la robustez del modelo.  
- Explorar nuevas arquitecturas de redes neuronales para mejorar la precisión en la detección de goteo.  
- Integrar visualizaciones avanzadas de los mapas térmicos de las celdas Peltier.  

---

## 👥 Authors
- [alexis.angeles0160@gmail.com]  
- [yair.gutierrez@uaem.edu.mx]  
- [oubram@uaem.mx]  
- [roy.lopez@uaem.edu.mx]  
