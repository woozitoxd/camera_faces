# camera_faces

Proyecto en Python para detección de rostros en video en vivo usando OpenCV.

## Dependencias

- Python 3.7+ (preferible 3.10+)
- OpenCV (cv2)

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

Contenido de `requirements.txt`:

```
opencv-python
```

## Uso

1. Conecta una cámara (integrada o USB).
2. Ejecuta:

```bash
python detectFaces.py
```

3. Aparecerá una ventana llamada `Deteccion de Caras`.
4. Presiona `q` para salir.

## El codigo:

- Carga el clasificador Haar Cascade frontal desde `cv2.data.haarcascades`.
- Abre la cámara con `cv2.VideoCapture(0)`.
- Captura frame a frame, convierte a escala de grises, y aplica `detectMultiScale`.
- Dibuja un rectángulo azul alrededor de cada cara detectada.
- Finaliza liberando recursos (`cap.release()` y `cv2.destroyAllWindows()`).

## Proyecto tomado de "Programando con Mica" influencer