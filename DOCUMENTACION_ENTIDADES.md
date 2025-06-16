# Documentación Profunda del Sistema de Entidades

Este documento se centra exclusivamente en el diseño y funcionamiento de las clases `Entidad`, `Personaje` y `Enemigo`. Este sistema es el núcleo de la arquitectura orientada a objetos del juego.

## 1. El Concepto: Herencia y Polimorfismo

En lugar de escribir código separado para el jugador y para cada tipo de enemigo, utilizamos un diseño más inteligente basado en la **herencia**.

1.  **Clase Base (`Entidad`)**: Creamos una clase "plantilla" o "molde" que contiene toda la lógica y los atributos que son **comunes a cualquier objeto interactivo** del juego. ¿Qué tienen en común un personaje y un enemigo? 
    *   Tienen una posición y un tamaño.
    *   Les afecta la gravedad.
    *   Pueden moverse.
    *   Pueden chocar con cosas.
    *   Necesitan ser dibujados en pantalla.

2.  **Clases Derivadas (`Personaje`, `Enemigo`)**: Estas clases **heredan** todo lo de `Entidad`. No necesitan reescribir la lógica de la gravedad o el movimiento. Su único trabajo es añadir el comportamiento que las hace **únicas**:
    *   El `Personaje` es único porque **responde a los comandos del jugador**.
    *   El `Enemigo` es único porque **se mueve por sí mismo** (IA).

Este enfoque no solo ahorra código, sino que hace que el sistema sea increíblemente **extensible**. Si quisiéramos crear un nuevo tipo de enemigo que vuela, solo tendríamos que crear una nueva clase que herede de `Entidad` y modificar su lógica de `update` para que no le afecte la gravedad.

---

## 2. La Clase Base: `Entidad` - El ADN de los Objetos

`entidades/entidad.py`

Esta es la clase más importante. Define la estructura fundamental de cualquier objeto dinámico en el juego.

### Atributos Clave

*   `self.rect = pygame.Rect(x, y, width, height)`: Este es el corazón de la entidad. Un objeto `Rect` de Pygame no es solo un rectángulo; es una herramienta poderosa que almacena coordenadas (`x`, `y`), dimensiones (`width`, `height`) y proporciona métodos para la detección de colisiones (`.colliderect()`) y la manipulación de la posición (`.left`, `.right`, `.top`, `.bottom`). Usar `Rect` para la física y el dibujado asegura una consistencia perfecta.

*   `self.velocidad = 5`: La **magnitud** del movimiento. Es la velocidad base cuando se mueve.
*   `self.vel_x = 0` y `self.vel_y = 0`: Estos son los **componentes vectoriales** de la velocidad. `vel_x` controla el movimiento horizontal (positivo a la derecha, negativo a la izquierda) y `vel_y` el vertical (positivo hacia abajo, negativo hacia arriba). Separarlos nos permite manejar la física de cada eje de forma independiente.

*   `self.gravedad = 0.8`: Una constante que se suma a `vel_y` en cada fotograma. Simula una aceleración gravitacional constante, lo que produce un movimiento de caída y salto parabólico y realista.
*   `self.fuerza_salto = -15`: La velocidad vertical inicial que se aplica al saltar. Es negativa porque en Pygame el eje Y crece hacia abajo, por lo que para moverse hacia arriba necesitamos una velocidad negativa.

*   `self.en_suelo = False`: Un **indicador de estado (flag)**. Es `True` solo si el `rect` de la entidad está en contacto con la parte superior de una estructura. Es fundamental para la lógica del juego, ya que solo se puede saltar si `en_suelo` es `True`.

### Métodos Clave

*   `update()`: Este método define la **física pasiva** de la entidad. Su única responsabilidad es aplicar la gravedad. Al llamarlo en cada fotograma, garantizamos que todas las entidades (jugador, enemigos) se vean afectadas por la gravedad de la misma manera.

*   `mover_derecha()` / `mover_izquierda()`: Estos métodos no mueven directamente la entidad. En su lugar, **establecen la intención de movimiento** al asignar un valor a `self.vel_x`. Es el motor de colisiones en `Pantalla` el que finalmente usará `vel_x` para actualizar la posición `rect.x`.

*   `saltar()`: Este método comprueba el estado `en_suelo`. Si es `True`, inicia un salto aplicando la `fuerza_salto` a `vel_y` y pone `en_suelo` a `False` para evitar un doble salto en el aire.

*   `cambiar_direccion()`: Simplemente invierte el signo de `self.velocidad`. Este es el mecanismo que usa el enemigo para rebotar en las paredes.

*   `_render_(screen)`: Es un método **abstracto** o "contrato". Obliga a que cualquier clase que herede de `Entidad` deba proporcionar su propia lógica de dibujado. Esto es polimorfismo en acción.

---

## 3. Clase Derivada: `Personaje` - La Voluntad del Jugador

`entidades/personaje.py`

Esta clase hereda toda la maquinaria de `Entidad` y le añade una capa para interpretar las acciones del jugador.

### `handle_events(events, keys_pressed)`

Este es el único método importante que define el `Personaje`. Su lógica es sutil y crucial:

1.  **Movimiento Continuo (Izquierda/Derecha)**: Utiliza `keys_pressed`, que es una lista del estado de todas las teclas en el fotograma actual. 
    *   `if keys_pressed[pygame.K_LEFT]:` comprueba si la tecla está **mantenida pulsada**. Esto permite un movimiento fluido y continuo. Llama a `mover_izquierda()` para establecer la intención de movimiento.
    *   Si no se pulsa ninguna tecla de dirección, se establece `self.vel_x = 0` para que el personaje se detenga inmediatamente.

2.  **Acciones Discretas (Salto)**: Utiliza el bucle `for event in events:`. La lista `events` solo contiene las acciones que han ocurrido **justo en este fotograma** (ej: una tecla que *acaba* de ser pulsada).
    *   `if event.type == pygame.KEYDOWN:` se asegura de que reaccionamos solo al momento de la pulsación, no mientras se mantiene pulsada.
    *   Esto es perfecto para el salto: queremos que el personaje salte una sola vez por cada pulsación de la barra espaciadora, no que siga saltando mientras la mantenemos apretada.

### `_render_(screen)`

Implementa el "contrato" de `Entidad`. Simplemente dibuja el `self.rect` en la pantalla con su color correspondiente.

---

## 4. Clase Derivada: `Enemigo` - IA Simple y Autónoma

`entidades/enemigos.py`

Esta clase también hereda de `Entidad`, pero en lugar de reaccionar al teclado, tiene un comportamiento predefinido.

### `update()`

Aquí reside la "Inteligencia Artificial" del enemigo. Es engañosamente simple pero muy efectivo gracias a la interacción con el resto del sistema:

1.  `super().update()`: **Siempre** se debe llamar al método del padre primero. Esto asegura que al enemigo le afecte la gravedad, igual que al jugador. Si olvidáramos esta línea, el enemigo flotaría en el aire.

2.  `self.mover_derecha()`: Esta es la **intención** o el **deseo** del enemigo. En cada fotograma, el enemigo dice "quiero moverme a la derecha". No sabe nada de paredes ni de plataformas.

La magia ocurre en la clase `Pantalla`. Cuando el motor de colisiones de `Pantalla` detecta que el enemigo ha chocado con una pared mientras intentaba moverse a la derecha, hace dos cosas:

*   Corrige su posición para que no la atraviese.
*   Llama a `enemigo.cambiar_direccion()`.

En el siguiente fotograma, la `velocidad` del enemigo será negativa, por lo que cuando su `update()` llame a `mover_derecha()`, en realidad estará estableciendo `self.vel_x` a un valor negativo, haciendo que se mueva a la izquierda hasta que vuelva a chocar.
