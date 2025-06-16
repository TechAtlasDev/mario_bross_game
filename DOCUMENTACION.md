# Documentación Detallada del Juego tipo Mario Bros

## 1. Visión General del Proyecto

### Objetivo

El objetivo de este proyecto es crear un juego de plataformas 2D simple, inspirado en clásicos como Mario Bros, utilizando Python y la librería Pygame. Sirve como un excelente caso de estudio para aprender sobre:

*   Programación Orientada a Objetos (POO).
*   Manejo de un bucle de juego (Game Loop).
*   Física básica para videojuegos (gravedad, salto, colisiones).
*   Manejo de entrada de usuario (teclado).
*   Inteligencia Artificial (IA) simple para enemigos.
*   Estructura y organización de un proyecto de software.

### Estructura de Carpetas

El proyecto está organizado en módulos para separar responsabilidades, lo que lo hace más fácil de entender y mantener.

```
/mario_bross
├── core/           # Lógica central del juego (bucle principal, configuración).
│   ├── game.py     # Contiene la clase Game con el bucle principal.
│   └── runner.py   # Configura y lanza una partida (crea el nivel).
├── entidades/      # Todas las cosas que se mueven y tienen "vida".
│   ├── entidad.py  # La clase base para todos los personajes y enemigos.
│   ├── personaje.py# La clase para el jugador.
│   └── enemigos.py # La clase para los enemigos.
├── estructuras/    # Objetos estáticos del nivel (suelo, plataformas).
│   └── piso.py     # Clase para crear plataformas y el suelo.
├── pantallas/      # Gestiona las escenas o niveles del juego.
│   └── escena1.py  # Clase que contiene y gestiona todo en un nivel.
├── utils/          # Herramientas y configuraciones.
│   └── config.py   # Parámetros como FPS, tamaño de pantalla, etc.
└── main.py         # El punto de entrada que inicia todo el juego.
```

---

## 2. El Corazón del Juego: Flujo de Ejecución

El juego cobra vida siguiendo una secuencia clara:

1.  **`main.py`**: Es el primer archivo que se ejecuta. Su única misión es llamar a la función `run_game()` del módulo `runner.py`.

2.  **`core/runner.py`**: Actúa como el "director de orquesta" de una partida. Aquí es donde:
    *   Se crea una instancia de `Game`.
    *   Se crea una instancia de `Pantalla` (nuestro nivel).
    *   Se crean el `Personaje`, los `Enemigos` y las `Estructuras` (plataformas).
    *   Se añaden todos estos objetos a la `Pantalla`.
    *   Finalmente, se le dice al objeto `Game` que empiece a correr con el nivel que hemos preparado: `game.run(pantalla)`.

3.  **`core/game.py`**: Aquí reside el **bucle principal del juego (Game Loop)**. Este bucle se ejecuta continuamente (por defecto, 60 veces por segundo) y es responsable de mantener el juego vivo. En cada "tick" o fotograma, realiza 3 tareas clave en orden:
    *   **Manejar Eventos**: Revisa si el jugador ha pulsado alguna tecla o si ha cerrado la ventana.
    *   **Actualizar Estado**: Llama a `pantalla.update()`, que a su vez actualiza la posición y estado de todos los personajes y enemigos según la física y la IA.
    *   **Dibujar en Pantalla (Renderizar)**: Llama a `pantalla.draw()`, que limpia la pantalla y dibuja todo en sus nuevas posiciones.

---

## 3. La Base de Todo: La Clase `Entidad`

La clase `Entidad` (`entidades/entidad.py`) es la pieza más importante de nuestro diseño. Es una **clase base** que define qué es una "cosa" en nuestro juego. Tanto el `Personaje` como el `Enemigo` heredan de ella.

### Atributos Clave

*   `self.rect`: Un objeto `pygame.Rect` que almacena la posición (`x`, `y`) y el tamaño (`ancho`, `alto`). Es fundamental para el dibujado y la detección de colisiones.
*   `self.vel_x` y `self.vel_y`: La velocidad actual de la entidad en los ejes X e Y.
*   `self.gravedad`: Una fuerza constante que tira de la entidad hacia abajo en cada fotograma, simulando la gravedad.
*   `self.fuerza_salto`: La velocidad negativa que se aplica a `vel_y` para hacer que la entidad salte.
*   `self.en_suelo`: Un booleano que nos dice si la entidad está tocando el suelo. Es crucial para saber si puede saltar.

### Métodos Principales

*   `update()`: Aquí se aplica la física básica. En cada llamada, la velocidad vertical (`vel_y`) se incrementa por la `gravedad`, haciendo que la entidad acelere hacia abajo.
*   `saltar()`: Si `en_suelo` es `True`, aplica la `fuerza_salto` para iniciar un salto.
*   `cambiar_direccion()`: Invierte la velocidad de movimiento, usado por los enemigos para rebotar.
*   `_render_()`: Un método "plantilla". Las clases hijas (como `Personaje`) deben implementar este método para definir cómo se dibujan.

---

## 4. Los Actores: `Personaje` y `Enemigo`

Estas clases heredan toda la lógica de física de `Entidad` y añaden su comportamiento único.

### `Personaje`

*   **Hereda de `Entidad`**: Obtiene automáticamente gravedad, capacidad de salto y un `rect`.
*   **Implementa `handle_events()`**: Aquí es donde cobra vida. Lee el estado del teclado (`keys_pressed`) para el movimiento continuo (izquierda/derecha) y los eventos de pulsación (`pygame.KEYDOWN`) para el salto, evitando saltos infinitos en el aire.

### `Enemigo`

*   **Hereda de `Entidad`**: También tiene física y un `rect`.
*   **Implementa `update()`**: Aquí reside su IA. Primero llama a `super().update()` para aplicar la gravedad, y luego ejecuta `self.mover_derecha()`. Esto hace que el enemigo intente moverse constantemente en una dirección. El motor de colisiones en `Pantalla` se encargará de hacer que rebote.

---

## 5. El Mundo del Juego: `Pantalla` y el Motor de Física

La clase `Pantalla` (`pantallas/escena1.py`) no solo contiene todos los objetos del nivel, sino que también funciona como nuestro **motor de física y colisiones**.

Su método `update()` es el más complejo y crucial:

1.  **Bucle sobre Entidades**: Recorre cada entidad (personaje, enemigos) una por una.
2.  **Actualización de la Entidad**: Llama a `entidad.update()`. Esto aplica la gravedad y, en el caso del enemigo, le da la orden de moverse.
3.  **Colisiones Horizontales**:
    *   Mueve el `rect` de la entidad horizontalmente (`entidad.rect.x += entidad.vel_x`).
    *   Comprueba si el `rect` ahora choca con alguna `estructura`.
    *   Si choca, corrige la posición. Por ejemplo, si se movía a la derecha, su borde derecho (`rect.right`) se alinea con el borde izquierdo de la estructura (`estructura.make().left`).
    *   **Si la entidad es un `Enemigo`**, además de corregir la posición, llama a `entidad.cambiar_direccion()` para que en el siguiente fotograma se mueva en la dirección opuesta.
4.  **Colisiones Verticales**:
    *   Mueve el `rect` de la entidad verticalmente (`entidad.rect.y += entidad.vel_y`).
    *   Comprueba si choca con alguna `estructura`.
    *   Si choca cayendo (`vel_y > 0`), alinea su parte inferior (`rect.bottom`) con la parte superior de la estructura, detiene su caída (`vel_y = 0`) y marca que está en el suelo (`en_suelo = True`).
    *   Si choca saltando (`vel_y < 0`), alinea su cabeza con la parte inferior de la estructura y detiene el ascenso (`vel_y = 0`).

---

## 6. Flujo de un Fotograma: Ejemplo Completo

Para unir todo, imaginemos qué pasa en un solo fotograma si el jugador pulsa la tecla de salto:

1.  **`Game`**: Detecta el evento `pygame.KEYDOWN` con la tecla `K_SPACE`.
2.  **`Game` -> `Pantalla`**: Pasa el evento a `pantalla.handle_events()`.
3.  **`Pantalla` -> `Personaje`**: `pantalla` pasa el evento a `personaje.handle_events()`.
4.  **`Personaje`**: El método `handle_events` ve el evento de salto y llama a `self.saltar()`.
5.  **`Personaje.saltar()`**: Como `self.en_suelo` es `True`, cambia `self.vel_y` a un valor negativo (ej: -15) y pone `en_suelo` a `False`.
6.  **`Game` -> `Pantalla.update()`**: Ahora empieza la fase de actualización.
7.  **`Pantalla`**: Llama a `personaje.update()`. La gravedad se suma a `vel_y` (ej: -15 + 0.8 = -14.2).
8.  **`Pantalla` (Colisiones)**: Mueve el `rect` del personaje hacia arriba según la nueva `vel_y`. No choca con nada.
9.  **`Game` -> `Pantalla.draw()`**: Llama a `personaje.draw()`.
10. **`Personaje`**: Se dibuja a sí mismo en la nueva posición, más alta.

En los siguientes fotogramas, la gravedad seguirá aumentando `vel_y`, haciendo que el salto sea cada vez más lento, hasta que `vel_y` se vuelva positivo y el personaje empiece a caer. Cuando finalmente choque con el suelo, el motor de colisiones detendrá la caída y volverá a poner `en_suelo` en `True`, listo para el siguiente salto.

## En caso de que el miembro del equipo no entienda, puede seguir estos simples pasos:

- 1. Ir a mesa de ayuda de la UCSP
- 2. Registrarse con su correo institucional
- 3. Buscar el apartado de cambios internos de la UCSP
- 4. Cambiarse de carrera a educación inicial.
