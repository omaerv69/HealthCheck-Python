
# Health Calculator Service

## Description
Health Calculator Service est une application Flask qui propose deux calculateurs principaux : 
- **BMI (Body Mass Index)** : Permet de calculer l'indice de masse corporelle à partir de la taille et du poids.
- **BMR (Basal Metabolic Rate)** : Permet de calculer le taux métabolique basal en fonction de la taille, du poids, de l'âge et du sexe.

L'application est conteneurisée avec Docker et dispose d'un pipeline CI/CD pour les déploiements sur Azure.

---

## Fonctionnalités
- Calcul du BMI à l'aide d'une interface utilisateur simple.
- Calcul du BMR basé sur des facteurs personnalisés.

---

## Arborescence du projet

```
Projet_Python-Devops/
├── .github/workflows         # CI/CD configuration
│   └── ci-cd.yml             # Définition du pipeline GitHub Actions
├── health-calculator-service
│   ├── static/               # Fichiers CSS (style.css)
│   ├── templates/            # Templates HTML pour le front-end
│   │   ├── bmi_form.html     # Formulaire BMI
│   │   ├── bmr_form.html     # Formulaire BMR
│   │   ├── index.html        # Page d'accueil
│   │   └── result.html       # Résultats des calculs
│   ├── app.py                # Script principal Flask
│   ├── health_utils.py       # Utilitaires pour les calculs de santé
│   ├── requirements.txt      # Dépendances Python
│   ├── Dockerfile            # Fichier Docker pour conteneurisation
│   ├── Makefile              # Automatisation des tâches courantes
│   └── test.py               # Tests unitaires
```

---

## Prérequis

- **Python 3.9+**
- **Docker**
- **Azure Web App** (pour le déploiement)

---

## Installation et utilisation

### 1. Cloner le dépôt
```bash
git clone <url-du-depot>
cd Projet_Python-Devops/health-calculator-service
```

### 2. Installer les dépendances
```bash
make init
```

### 3. Lancer l'application
```bash
make run
```
L'application sera accessible sur `http://127.0.0.1:5000`.

---

## Conteneurisation avec Docker

### Construire l'image Docker
```bash
make build
```

### Exécuter le conteneur
```bash
docker run -p 5000:5000 health-calculator-service
```

---

## Pipeline CI/CD

Le pipeline CI/CD est configuré avec GitHub Actions pour :
1. Vérifier et tester le code.
2. Construire une image Docker.
3. Déployer l'application sur une **Azure Web App**.

### Secrets nécessaires
- **AZURE_CREDENTIALS** : Identifiants pour se connecter à Azure.
- **AZURE_WEBAPP_PUBLISH_PROFILE** : Profil de publication pour l'application Web.

---

## Tests

Pour exécuter les tests unitaires :
```bash
make test
```

---

## Auteur
- **HASSAS Mohammed-Omar** - Créateur et développeur principal.
