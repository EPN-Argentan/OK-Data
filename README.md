# OK Data

## Implémenter du contenu (nouveau scénario)
Pour ajouter un nouveau scénario au jeu, il faut d'abord créer l'élément cliquable dans le salon (comme le sont le téléphone ou le chien) puis ensuite associer cet élément à un label.

### Créer un élément cliquable sur le hub
Afin de rendre un scénario accessible il faut créer un élément cliquable dans le hub qui sera la porte d'entrée.
Pour cela, il faut d'abord créer un fichier dans le dossier "game" qui servira de squelette pour la scène sous cette dénomination : "scene_leNomDeVotreScene.rpy"
Ce fichier doit commencer avec l'élément suivant :
```python
  label leNomDeVotreScene:
    empty "" #cette ligne permet d'éviter que cela entraine des erreurs en affichant un premier texte vide à l'ouverture du label
```

Ensuite, il faut créer l'élément dans le fichier *my_screens.rpy* dans le screen *HubElements* :
```python
  if hubClickable["le_nom_de_votre_element_cliquable"] == 1:
    imagebutton:
      xpos 1400 #sa position X
      ypos 797 #sa position Y
      idle "UI/imagebuttons/dog_idle.png" #chemin de l'image de l'élément cliquable avec un contour blanc
      hover "UI/imagebuttons/dog_hover.png" #chemin de l'image de l'élément cliquable sans un contour blanc
      action Jump("leNomDeVotreScene") #le nom du label où est la scène
```
Afin de rendre l'élément cliquable, il faut au moment opportun du scénario écrire ceci :
```python
  $ hubClickable["le_nom_de_votre_element_cliquable"]= 1
```
Cela peut être définit à n'importe quel moment
Si vous souhaitez que l'élément soit cliquable dés le début du jeu, il faut dans "script.rpy", dans la liste "$ hubClickable = {" ajouter une ligne :
```python
le_nom_de_votre_element_cliquable: 1,
```
### Structure d'un scénario
| Nom de l'élément  | Description |
| ------------- | ------------- |
| label  | Élément principal d'un scénario. C'est une sorte d'encapsuleur dans lequel vous pourrez mettre des images, des éléments d'interfaces, des dialogues. Chaque Scénario s'ouver avec un labl : "label forest :"  |
| screen  | Élément flottant à afficher et positionner où l'on souhaite dans l'image. La barre de vie privée est, par exemple, un screen appelé à chaque fois que celle-ci doit être affichée. Les screens sont rangés dans le fichier "my_screens.rpy"  |

## Les points
### Ajouter ou enlever des points SANS une condition
Pour ajouter des points de vie sans condition, il suffit d'écrire :
```python
  $ points['le_nom_des_points'][0] += 5
```
Pour retirer des points de vie sans condition, il suffit d'écrire :
```python
  $ points['le_nom_des_points'][0] -= 5
```

### Ajouter ou enlever des points AVEC une condition 
Pour ajouter ou retirer des points de vie selon une condition, une fonction existe :
```python
call addPoints(value,key,condition, conditionValue, "losemessage", "winmessage")

# value = number to increment
# key = wich lifebar element has to be increment
# condition = condition to check
# conditionValue = waiting condition value to determine if it's a win or not
# losemessage = message to display if player lose points
# winmessage = message to display if player earn points
```
Exemple d'usage de la fonction :
```python
addPoints(5,'point_sante',BluetoothState,True,"Vous n'avez pas désactivé le bluetooth", "Vous avez bien pensé à désactiver le bluetooth")
# Si l'état du Bluetooth est activé alors ajoute 5 points et affiche "Vous avez bien pensé à désactiver le bluetooth" et sinon, retire 5 points et affiche "Vous n'avez pas désactivé le bluetooth"
```



