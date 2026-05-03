# Mariscos Tawa - Backend API (DRF)

Este es el backend para el sistema de gestión del restaurante "Mariscos Tawa", construido utilizando Django y Django REST Framework (DRF). El sistema provee soporte para el Menú Digital de Clientes y el Kitchen Display System (KDS) utilizado por los empleados y chefs.

## Requisitos Previos

Asegúrate de tener instalados los siguientes componentes en tu sistema:
- Python 3.10 o superior.
- MySQL Server (versión 8.0+ recomendada).
- Git (opcional, para control de versiones).

## Configuración del Entorno de Desarrollo

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio
Si usas Git, clona el repositorio y navega al directorio del proyecto:
```bash
# git clone <tu-repositorio-url>
cd tawa
```

### 2. Crear y activar el entorno virtual
Es una buena práctica aislar las dependencias del proyecto usando un entorno virtual.

**En Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar las dependencias
Con el entorno virtual activado, instala los paquetes requeridos usando `pip`:
```bash
pip install -r requirements.txt
```

### 4. Configurar las Variables de Entorno (`.env`)
El proyecto utiliza variables de entorno para manejar las credenciales de la base de datos de forma segura. 

Crea un archivo llamado `.env` en la raíz de tu proyecto (al mismo nivel que `manage.py`) y agrega la configuración de tu conexión a MySQL:

```env
# Ejemplo de contenido para el archivo .env
DB_NAME=tawa
DB_USER=root
DB_PASSWORD=root
DB_HOST=localhost
DB_PORT=3306
```
*(Nota: Asegúrate de crear una base de datos llamada `tawa` en tu MySQL local antes de continuar).*

### 5. Ejecutar Migraciones
Genera y aplica las migraciones para crear las tablas en tu base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Cargar Datos de Prueba (Opcional)
Si deseas tener platillos y categorías de prueba para poder evaluar el frontend inmediatamente, ejecuta el script proporcionado:

```bash
python insert_test_data.py
```

### 7. Crear un Usuario Administrador / Empleado
Para poder acceder a las rutas protegidas (KDS), necesitas crear al menos un empleado. Puedes hacerlo mediante la consola interactiva:

```bash
python manage.py createsuperuser
```
Sigue las instrucciones en consola para asignar un nombre de usuario y contraseña.

### 8. Iniciar el Servidor
Finalmente, levanta el servidor de desarrollo local:

```bash
python manage.py runserver
```
La API estará disponible en `http://127.0.0.1:8000/`.

---

## Estructura de la API

Todas las rutas de recursos inician con el prefijo `/api/`.

### Rutas Públicas (Lectura / Clientes)
*   `GET /api/categorias/` - Lista de categorías.
*   `GET /api/productos/` - Catálogo completo del menú (Soporta filtros: `?categoria=1&is_active=true`).
*   `POST /api/ordenes/` - Crear una nueva orden con su carrito de detalles y cálculos automáticos de subtotal, IVA y total.

### Rutas Protegidas (Requieren Token de Empleado)
*   `GET, PATCH, PUT /api/ordenes/` - Gestionar el listado y estado de las órdenes en curso (Soporta filtros: `?estado=NUEVA`).
*   `POST, PATCH, DELETE /api/productos/` - Modificar el catálogo.
*   `PATCH /api/detalles-orden/<id>/` - Marcar un platillo específico como `preparado`.

### Autenticación
Para acceder a las rutas protegidas, primero debes obtener un token enviando un POST a:
*   `POST /api/auth/login/`

**Ejemplo de Payload para Login:**
```json
{
    "username": "admin",
    "password": "tu_password"
}
```

El servidor te devolverá un Token (`{"token": "xxxx"}`) el cual debes incluir en los Headers de todas tus peticiones protegidas de la siguiente manera:
```http
Authorization: Token xxxxxxxxxxxxxxxxxxxx
```