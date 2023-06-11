# Proyecto de juego

Para correr el juego debes de seguir las siguientes intrucciones en la terminal

```sh
cd game
python3 main.py
```

# Proyecto de charts

Para correr las graficas debes de seguir las siguientes intrucciones en la terminal

```sh
cd charts
python3 main.py
```

# Proyecto de app

Para correr la app debes de seguir las siguientes intrucciones en la terminal

```sh
git clone
cd app
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

# Tips que pueden ser utiles

De ser necesario para crear un ambiente virtual se puede correr el siguiente comando dentro de la carpeta donde se quiere dicho ambiente, se activa con activate y desactiva con deactivate

```sh
python3 -m venv "Nombre del ambiente"
source "Nombre del ambiente"/bin/activate
deactivate
```

Con el siguiente comando podras guardar las dependencias necesarias para hacer uso de ellas despues

```sh
pip3 freeze > requirements.txt
```

Con el siguiente script podras instalar las dependencias y archivos necesarios para un proyecto

```sh
pip3 install -r requirements.txt
```

