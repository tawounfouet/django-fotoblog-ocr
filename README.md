# Merchex
Fotoblog est un projet Django pour la gestion d'un blog de photographie.

## Installation

1. Cloner le projet :
    
 ```bash
git clone https://github.com/tawounfouet/django-fotoblog-ocr.git

```

2. Créer un environnement virtuel :

```bash
virtualenv .env -p python3
```

3. Activer l'environnement virtuel :

```bash
source .env/bin/activate
```

4. Installer les dépendances :

```bash
pip install -r requirements.txt
```


5. Créer une base de données et appliquer les migrations :

```bash
python3 manage.py migrate
```

6. Créer un superutilisateur :
    
```bash
python3 manage.py createsuperuser
```


7. Lancer le serveur :

```bash
python3 manage.py runserver
```

6. Accéder à l'application dans votre navigateur à l'adresse `http://localhost:8000/`.

## Contribution

Les contributions sont les bienvenues ! Pour contribuer au projet, veuillez suivre les étapes suivantes :

1. Forker le projet.
2. Créer une branche pour votre fonctionnalité (`git checkout -b nouvelle-fonctionnalité`).
3. Commiter vos modifications (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`).
4. Pousser la branche (`git push origin nouvelle-fonctionnalité`).
5. Ouvrir une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.