# SureBet API

API para obtener cuotas y calcular oportunidades de arbitraje en casas de apuestas.

## Requisitos Previos

- Python 3.13 o superior instalado

## Instalacion

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd surebet-api
```

2. Crear entorno virtual:
```bash
python -m venv .venv
```

3. Activar entorno virtual:

En Windows:
```bash
.venv\Scripts\activate
```

En Linux/Mac:
```bash
source .venv/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar el Proyecto

Para iniciar el servidor de desarrollo:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

La API estara disponible en http://localhost:8000

## Estructura del Proyecto

- `app/` - Aplicacion principal
  - `api/` - Endpoints de la API
  - `core/` - Configuracion global
  - `models/` - Modelos del dominio
  - `providers/` - Conexiones con casas de apuestas
  - `schemas/` - Validacion de datos
  - `services/` - Logica de negocio
  - `utils/` - Funciones auxiliares
- `tests/` - Pruebas automatizadas

## Configuracion

Crear un archivo `.env` en la raiz del proyecto con las siguientes variables:

- `ENVIRONMENT` - Entorno de ejecucion (development/production)
- `DEBUG` - Modo debug (true/false)
- `PORT` - Puerto del servidor (default: 8000)
- `TIMEOUT` - Tiempo de espera en segundos (default: 30)
- `BETPLAY_URL` - URL de la API de Betplay

Ejemplo de archivo `.env`:
```
ENVIRONMENT=development
DEBUG=true
PORT=8000
TIMEOUT=30
BETPLAY_URL=<url-de-la-api-de-betplay>
```

## Proveedores

El proyecto incluye un proveedor base (`Provider`) que define la interfaz que deben implementar todos los proveedores de casas de apuestas.

Actualmente implementado:
- `BetplayProvider` - Proveedor para la API de Betplay

## Desarrollar

Para ejecutar en modo de desarrollo con recarga automatica:

```bash
uvicorn app.main:app --reload
```
