Rapport d'incident - Application TODO
Contexte

Date et heure de l'incident : 29 juillet 2025 vers 14h00

Service impacté : API TODO (Flask)

Description : L'API a commencé à renvoyer des erreurs 500 quand on appelait la route /error, ça a cassé le service un moment.

Détection et diagnostic

Comment on a détecté le problème : Sur Grafana, on a vu les erreurs 500 monter en flèche.

Métriques observées : Le taux d'erreurs 5xx qui a brusquement augmenté.

Ce qu'on a fait direct : Vérification des logs pour comprendre d'où venait l'erreur.

Cause racine

Le endpoint /error générait une division par zéro exprès pour simuler une panne.

Cette erreur n'était pas gérée correctement, du coup ça plantait l'API à chaque appel.

Actions prises et rétablissement

Redémarrage du service pour remettre l'API en état.

On a bloqué temporairement l'accès à /error pour éviter d'autres soucis.

On a prévu de mettre une gestion globale des erreurs pour éviter que ça casse tout.

Leçons apprises et prévention

Faut mieux isoler les endpoints de test pour pas impacter la prod.

Mettre en place des alertes pour détecter rapidement les erreurs.

Ajouter des tests pour éviter ce genre d'erreurs dans le futur.

Documenter clairement les endpoints qui peuvent poser probleme.
