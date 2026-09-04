# 🚀 Guerra de meteoritos

Proyecto de repaso de PyGame. Vamos a construir el juego **por partes**, avanzando
de una carpeta a la siguiente. Cada parte tiene un `main.py` con código incompleto
(marcado con `# TODO`) y un `instrucciones.md` con lo que debes lograr.

## Objetivo final: ¿Cómo debe funcionar nuestro juego?

Controlas una nave con las flechas ⬅️➡️ (o A/D) en la parte inferior de la pantalla.
Los meteoritos caen desde arriba en posiciones aleatorias. Si un meteorito te toca,
pierdes. Mientras más tiempo sobrevivas, más sube tu puntaje.

## Instalación

```bash
git clone <URL-de-este-repo>
cd esquiva-meteoritos
python -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
```

## Flujo de trabajo

1. `parte_0_setup/` — ventana, loop principal, reloj (repaso express)
2. `parte_1_movimiento/` — mover al jugador con el teclado
3. `parte_2_obstaculos/` — generar y mover meteoritos con un temporizador
4. `parte_3_colision_puntaje/` — detectar colisiones, mostrar puntaje y game over
5. `solucion_completa/` — el juego completo, por si quieres comparar o te atoras

**¡Manos a la obra!** 👩‍🚀👨‍🚀
