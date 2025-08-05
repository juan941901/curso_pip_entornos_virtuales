# curso_pip_entornos_virtuales

Es importante que usemos WSL de windows, para tener un entorno linux dentro de nuestra maquina con windows, para ello ejecutaremos en power shell 

```powershell
wsl --install
```

Con el entorno linux configurado procedemos a verificar que este instalado corretamente pyhton con el comando 

```bash
python3 -V
```

Si python no se encuentra instalado lo instalaremos con 

```bash
sudo apt update && sudo apt -y upgrade
```

Si esta intalado procedemos a instalar el gestor de paquetes pip 

```bash
sudo apt install -y python3-pip
```