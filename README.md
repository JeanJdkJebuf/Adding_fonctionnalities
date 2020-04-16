# Adding_fonctionnalities

Ce site est la suite du [projet 8](https://github.com/JeanJdkJebuf/Pur_Beurre_Website)
On y ajoute deux fonctionnalités.
* La première permet à l'utilisateur de pouvoir modifier ses informations et son mot de passe dans sa page de profil.
* La seconde permet à l'utilisateur de pouvoir consulter les informations liées au produit précédent le substitut. Il pourra y accéder pendant ses recherches, ou pendant la consultation de son profil.

## Description

1. **Python**
Python 3.6 est utilisé pour ce projet. N'ayant pas essayé d'autres versions, merci de me laisser un commentaire en issue si vous rencontrez des problèmes.

2. **tests écrits à la fin d’une fonctionnalité**
Pour chaque fonctionnalité ajoutée, des tests unitaires ont été effectués pour s'assurer de la qualité du code et de pouvoir répondre aux besoins du projet.
**Coverage est utilisé en parallèle avec les tests de django. Ils sont utilisables seulement en mode développement.**

3. **Django**
Django permet de partitionner les différentes parties du site en applications.
Cela permet d'utiliser une méthode de travail itérative, d'implémenter une fonctionnalité après l'autre.

4. **Serveur de développement Django**
Le site est disponible uniquement sur le serveur de développement fourni par le framework django.

## Installation
*Créer une instance pipenv :
```python
pipenv install --python 3.6
```

1. **PostgreSQL**
Créer un utilisateur ainsi qu'une base de données PostgreSQL pour le projet.

2. **Fichier .env**
Créer le fichier .env dans la racine du projet.
Vous y fournirez les informations suivantes :
⋅⋅* la variable "BDD" devra contenir le nom de la base de données créée
⋅⋅* "PW_POSTGRES" contiendra le mot de passe de l'utilisateur
⋅⋅* "USER" fournira le nom de l'utilisateur
..* "SECRET_KEY" contiendra la clé de production

3. **Créer et peupler la bdd**
Faire les commandes suivantes :
```python
python manage.py makemigrations
```
```python
python manage.py migrate
```
```python
python manage.py populate_db
```

4. **Lancer le serveur**
```python
python manage.py populate_db
```
*Note : La page principale se trouve à l'adresse suivante : /main/homepage/
