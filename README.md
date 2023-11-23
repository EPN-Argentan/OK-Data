# OK Data

## Implémenter du contenu (nouveau scénario)
### Créer un élément cliquable sur le hub
Afin de rendre un scénario accessible il faut créer un élément cliquable dans le hub qui sera la porte d'entrée.
Pour cela, il faut d'abord créer un fichier dans le dossier "game" qui servira de squelette pour la scène sous cette dénomination : "scene_leNomDeVotreScene.rpy"
Ce fichier doit commencer avec l'élément suivant :
```
  label leNomDeVotreScene:
    empty "" #cette ligne permet d'éviter que cela entraine des erreurs en affichant un premier texte vide à l'ouverture du label
```

Ensuite, il faut créer l'élément dans le fichier *my_screens.rpy* dans le screen *HubElements* :
```
  if hubClickable["le_nom_de_votre_element_cliquable"] == 1:
    imagebutton:
      xpos 1400 #sa position X
      ypos 797 #sa position Y
      idle "UI/imagebuttons/dog_idle.png" #chemin de l'image de l'élément cliquable avec un contour blanc
      hover "UI/imagebuttons/dog_hover.png" #chemin de l'image de l'élément cliquable sans un contour blanc
      action Jump("leNomDeVotreScene") #le nom du label où est la scène
```
Afin de rendre l'élément cliquable, il faut au moment opportun du scénario écrire ceci :
  $ hubClickable["le_nom_de_votre_element_cliquable"]= 1
Cela peut être définit à n'importe quel moment, soit à la fin d'un scénario soit à l'initialisation (dans script.rpy, dans la liste "$ hubClickable = {" sous la forme "le_nom_de_votre_element_cliquable: 1,")


