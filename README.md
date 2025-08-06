# Curso pip Entornos Virtuales

## Instalación entorno windows
Es importante que usemos WSL de windows, para tener un entorno linux dentro de nuestra maquina con windows, para ello ejecutaremos en power shell:

```powershell
wsl --install
```

Con el entorno linux configurado procedemos a verificar que este instalado corretamente pyhton con el comando: 

```bash
python3 -V
```

Si python no se encuentra instalado lo instalaremos con:

```bash
sudo apt update && sudo apt -y upgrade
```

Si esta instalado procedemos a instalar el gestor de paquetes pip:

```bash
sudo apt install -y python3-pip
```

Librerias esenciales a tener build-essential, libssl-dev, libffi-dev y python3-dev. 

Para su instalación ejecutaremos el comando:

```bash
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```
## Instalación MAC
Los siguientes pasos son para realizar la configuración en equipos mac.

Instalamos las herramientas de comandos con:

```bash
sudo xcode-select --install
```

Instaladas ejecutaremos:

```bash
sudo xcode-select --reset
```

Ahora para realizar la instalacción de python3 usaremos homebrew, para realizar la instalacción usaremos:

```brew
brew install python3
```

## Extesiones a usar en visual code
- Python
- WSL (Si estas trabajando desde windows)

## Creación de archivo gitignore

Podemos usar la herramienta [gitignore.io](https://www.toptal.com/developers/gitignore/), en ella por estandar vamos a indicar que no genere archivo para windows, linux, mac y python

# Pasos para correr juego de piedra, papel y tijera

para ejecutar el juego debes ingresar a la carpeta game

```bash
cd game
python3 main.py
```

# Crear entorno virtual

Para crear un entorno virtual usaremos el comando:

```bash
python3 -m venv entorno_charts
```

Y luego:

```bash
source entorno_charts/bin/activate
```

y para salir del entorno usamos:

```bash
deactivate
```

se puede cambiar entorno_charts por el nombre que le deseemos asignar.

Puede pasar que no cree la carpeta activate dentro de bin, y esto genere un error, que es debido a que falta paquete por instalar de python, para solucionarlo vamos a ejecutar los siguientes comando:

```bash
sudo apt update
sudo apt install python3.12-venv
```
instalado las dependencias eliminamos la carpeta creada de entorno_charts, con todo su contenido haciendo uso del comando:

```bash
rm -rf entorno_charts
```

y procedemos ahora si a ejecutar el comando de creación del entorno

# Copiar información al entorno ubuntu(wsl)

Para copiar carpetas o archivos dentro de nuestro entorno vamos a usar el comando:

```bash
cp -r /mnt/c/Users/tu_usuario/Desktop/mi_carpeta ~/
```
Esto copia `mi_carpeta` desde tu escritorio de Windows a tu carpeta personal (~) en Ubuntu.

# Instalar paquetes con pip

Para realizar una instalación de un paquete usamos el comando:
```bash
pip3 install nombre-del-paquete
```

Si quieres usar una versión especifica debes agrega `==` al final del nombre del paquete y luego la versión que deseas instalar

## ⚠️instalar libreria en entorno global, no recomendado hacer

para realizar el proceso de instalar una liberia en el entorno global debemos agregar `--break-system-packages`, al final del comando de instalación