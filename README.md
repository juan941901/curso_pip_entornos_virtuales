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