---
marp: true
theme: default
paginate: true

---

# Dockerizando nuestro Dash.

---

# Ejemplo 
- Vamos a dockerizar nuestro dashboard, para ello seguiremos los siguientes pasos.
- En la carpeta ejemplo tenemos un dash completo funcionado funcionado con docker.

---


- Necesitamos un requeriments.txt:
```
dash
pandas
requests
```

- Podemos obtenerlo con:
```bash
pip freeze
```
si hemos realizado el ejercicio con un venv.

---

- Modificamos la forma en la que ejecutamos el dash:
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8080)
```

---

- El comando del dockerfile para que ejecute dash de la siguiente manera:
```Dockerfile
CMD ["python", "app.py"]
```

---

- Para ejecutar la aplicación podemos usar los siguientes comandos:
```bash
docker build -t ejemplo_docker_dash .
docker run -p 8080:8080 ejemplo_docker_dash 
```

---

- Podemos definir un docker-compose.yaml para hacer la ejecución más sencilla:
```bash
docker-compose build
docker-compose up
```

---

# Ejercicio

- Dockeriza el dashboard que acabas de realizar.
- Sube todos los ficheros a un repositorio de github.
