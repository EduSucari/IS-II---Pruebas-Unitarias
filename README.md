# IS-II - Pruebas Unitarias

Proyecto académico de **Ingeniería de Software II** que muestra cómo aplicar pruebas unitarias en Python sobre el algoritmo de ordenamiento **Bubble Sort** (ordenamiento de burbuja), usando casos de prueba diseñados a partir de los caminos del código.

## Estructura del proyecto

```
.
├── main/
│   ├── __init__.py
│   └── bubble_sort.py      # Implementación de Bubble Sort
├── tests/
│   ├── __init__.py
│   └── tests.py            # Pruebas unitarias (unittest)
├── requirements.txt        # Dependencias (pytest, pytest-cov)
├── .gitignore
└── README.md
```

## El algoritmo

`bubble_sort(vet)` ordena una lista de **menor a mayor, in situ**: modifica la lista recibida y no devuelve ningún valor (`None`).

En cada pasada compara elementos adyacentes y los intercambia si están en el orden incorrecto. El rango de comparación se reduce en cada pasada, porque el elemento mayor ya queda en su posición final.

```python
from main.bubble_sort import bubble_sort

datos = [3, 1, 2]
bubble_sort(datos)
print(datos)  # [1, 2, 3]
```

## Casos de prueba

Las pruebas están escritas con `unittest` y siguen el patrón **Arrange - Act - Assert**.

| ID  | Prueba                      | Entrada     | Resultado esperado | Qué cubre                                     |
|-----|-----------------------------|-------------|--------------------|-----------------------------------------------|
| CP1 | `test_cp1_un_elemento`      | `[7]`       | `[7]`              | Lista de un solo elemento                     |
| CP2 | `test_cp2_sin_intercambio`  | `[1, 2]`    | `[1, 2]`           | Lista ya ordenada, sin intercambios           |
| CP3 | `test_cp3_un_intercambio`   | `[2, 1]`    | `[1, 2]`           | Un único intercambio                          |
| CP4 | `test_cp4_dos_pasadas`      | `[3, 1, 2]` | `[1, 2, 3]`        | Varias pasadas del ciclo externo              |

## Requisitos

- Python 3.8 o superior
- `pytest` y `pytest-cov` (ver `requirements.txt`)

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/EduSucari/IS-II---Pruebas-Unitarias.git
cd IS-II---Pruebas-Unitarias

# 2. Crear y activar un entorno virtual
python -m venv .venv

# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt
```

## Ejecutar las pruebas

Con `unittest`:

```bash
python -m unittest discover -s tests -t . -v
```

Con `pytest` (el archivo se llama `tests.py`, por lo que hay que indicar la ruta explícitamente):

```bash
pytest tests/tests.py -v
```

## Cobertura de código

```bash
pytest tests/tests.py --cov=main --cov-branch --cov-report=term-missing
```

Para generar un reporte HTML (se guarda en `htmlcov/`):

```bash
pytest tests/tests.py --cov=main --cov-branch --cov-report=html
```

Resultado actual: **100 % de cobertura de sentencias y de ramas** en `main/bubble_sort.py`.
