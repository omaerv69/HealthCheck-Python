# Utilisation de l'image Python 3.9 slim
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY . /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application Flask écoute
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "app.py"]
