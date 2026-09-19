# Validation obligatoire avant publication

Ne pas déclarer une version « stable » uniquement parce que `lb build` se termine sans erreur.

## 1. Compilation

- [ ] La compilation se termine sans erreur ; l'ISO est créée.
- [ ] La somme SHA-256 est calculée et enregistrée.
- [ ] Le nom de version, la date, la liste des paquets et le journal sont conservés.

## 2. Démarrage en machine virtuelle (sur **disques de test uniquement**)

- [ ] Démarrage Live en mode BIOS/Legacy.
- [ ] Démarrage Live en mode UEFI.
- [ ] L'interface XFCE, clavier français et connexion réseau fonctionnent.
- [ ] Firefox ESR et LibreOffice démarrent.
- [ ] L'installateur démarre depuis le menu de démarrage.
- [ ] Installation complète sur disque virtuel vierge, sans connexion Internet.
- [ ] Redémarrage sur le disque installé **sans** l'ISO.
- [ ] Session utilisateur, réseau et mise à jour des paquets testés après installation.

## 3. Validation sur ordinateurs reconditionnés

Sur plusieurs modèles de l'atelier, consigner CPU, RAM, SSD/HDD, carte Wi-Fi, carte graphique et mode de démarrage :

- [ ] Démarrage USB BIOS ou UEFI selon les possibilités du PC.
- [ ] Affichage, clavier, pavé tactile/souris, audio, Ethernet et Wi-Fi.
- [ ] Mise en veille et reprise, redémarrage et extinction.
- [ ] Installation sur **disque dédié aux tests**, puis démarrage autonome.
- [ ] Test d'usage prolongé, contrôle des journaux d'erreur et des mises à jour.

## Rapport d'anomalie

Dans GitHub Issues, préciser le modèle, le mode BIOS/UEFI, la version ISO, les étapes de reproduction et les messages d'erreur. Masquer les identifiants, adresses et données personnelles.

**Une ISO non testée doit rester une version de développement, jamais une image destinée aux bénéficiaires.**
