# curso_pip_entornos_virtuales

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

