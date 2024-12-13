# P10_RecoApp
P10 parcours IA engineer

# Description
Ce projet propose une **API de Recommandation** construite avec Flask. Il utilise des algorithmes de recommandation, y compris un **Recommendeur Basé sur le Contenu** et un **Recommendeur Hybride**, pour suggérer des articles aux utilisateurs en fonction de leurs préférences et interactions. L'API est conçue pour fournir des recommandations via des requêtes HTTP simples.

## Fonctionnalités

- **Algorithmes de Recommandation** : Inclut à la fois des systèmes de recommandation basés sur le contenu et hybrides.
- **Données Préchargées** : Télécharge et charge automatiquement les ensembles de données nécessaires à partir de GitHub Release
- **Points de Terminaison de l'API** :
  - `/` : Message de bienvenue.
  - `/get_recommendation/<id>` : Fournit des recommandations pour un ID utilisateur donné.
- **Conception Évolutive** : Construit avec Flask pour un déploiement et une évolutivité faciles.

---

## Technologies

Le projet utilise les technologies suivantes :

- **Python** : Langage de programmation principal.
- **Flask** : Framework web pour servir l'API.
- **Pickle** : Pour charger les fichiers de données prétraitées.
- **Requests** : Pour récupérer les ensembles de données à partir d'URLs distantes.