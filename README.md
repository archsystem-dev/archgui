
![Image](https://raw.githubusercontent.com/archsystem-dev/archgui-support/refs/heads/main/logo-archgui.png)
  
Archgui est un module basé sur `FreeSimpleGUI`. 
Il permet la création de modèle de fenêtre à partir d’un fichier `.json` et d’un fichier `.py` pour les events
correspondant à ce modèle. Le but de ce module est de simplifier la création d’application nécessitant
la gestion de plusieurs fenêtres.

À terme une `GUI` basé sur ce module sera disponible pour la création des fenêtres. 
Il ne sera plus nécessaire d’éditer à la main les fichiers `.json` qui est la partie la plus chronophage,
le gain de temps devrait etre significatif entre une application développée depuis `FreeSimpleGUI` et 
une développée avec la surcouche `ArchGUI`.

<br/>

⚠️ Le development de ce module est en cours. 
Ce n’est pour le moment qu’une demonstration incomplète. 
Si vous souhaitez tester ce module, il est préférable de le faire dans un environnement dédié.

<br/>

## 😊 Fonctionnalités principales :
- Dimensionnement et positionnement simplifié des fenêtres.
- Dimensionnement et positionnement des fenêtres relatif à une autre fenêtre ou à la résolution du moniteur.
- Création de fenêtre sur la base d’un fichier `.json`.
- Les fenêtres sont gérées comme modèle et peuvent être dupliqué et affiché à volonté.
- Update simple des éléments d’une fenêtre.

<br/>
