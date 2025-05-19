# Odoo-PayementProgress


Un module Odoo pour suivre facilement le montant payé et le pourcentage d’apport payé sur les factures.

---

## Description

Ce module étend le modèle `account.move` d'Odoo pour ajouter deux champs calculés :

- **Montant payé** : montant déjà réglé sur une facture.
- **Apport payé (%)** : pourcentage du total de la facture déjà payé.

Idéal pour avoir une vision claire et en temps réel de l’état des paiements de vos factures.

---

## Fonctionnalités

- Calcul automatique du montant payé (`amount_paid`).
- Calcul automatique du pourcentage d’apport payé (`apport_paye`).
- Compatible avec les factures et reçus.
- Stockage des valeurs calculées pour optimisation.

---

## Installation

1. Copier le module dans votre dossier `addons` d’Odoo.
2. Mettre à jour la liste des modules dans Odoo.
3. Installer le module via l’interface Odoo.
4. Redémarrer le serveur Odoo si nécessaire.

---

## Utilisation

Une fois installé, les nouveaux champs seront disponibles dans les factures. Ils se mettent à jour automatiquement à chaque paiement ou modification.

---

## Contribution

Contributions, suggestions et améliorations sont les bienvenues !  
N’hésitez pas à ouvrir une issue ou une pull request.

---

## Licence

Ce projet est sous licence MIT.

---

**Crée avec ❤️ par Ibrahim Mohamed**

