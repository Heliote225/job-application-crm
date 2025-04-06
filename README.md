# job-application-crm

Un mini CRM personnel pour gérer les candidatures envoyées, les offres à postuler, les entretiens et les retours.

> Stack : Django (API) + Vue 3 (Frontend) + TailwindCSS + Vue.Draggable

---

## Fonctionnalités

- Interface *Kanban* pour organiser ses candidatures
- Création, modification, suppression de candidatures
- Glisser-déposer entre les colonnes (comme Trello)
- API REST sécurisée avec Django REST Framework
- UI responsive, moderne, rapide

---

## Aperçu

![demo](./screenshot.png)

---

## Stack technique

### Frontend
- [Vue 3](https://vuejs.org/)
- [Vite](https://vitejs.dev/)
- [TailwindCSS](https://tailwindcss.com/)
- [Vue.Draggable](https://github.com/SortableJS/vue.draggable.next)

### Backend
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- Authentification possible avec SimpleJWT ou session

---

## Lancer le projet

### Backend

```bash
# Créer un environnement virtuel
python -m venv env
source env/bin/activate  # ou .\env\Scripts\activate sur Windows

# Installer les dépendances
pip install django djangorestframework

# Lancer le serveur
python manage.py runserver
