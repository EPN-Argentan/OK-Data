# OK Data

## Implémenter du contenu (nouveau scénario)
Pour ajouter un nouveau scénario au jeu, il faut d'abord créer l'élément cliquable dans le salon (comme le sont le téléphone ou le chien) puis ensuite associer cet élément à un label.

### Créer un élément cliquable sur le hub
#### Initialisation du scénario
Afin de rendre un scénario accessible il faut créer un élément cliquable dans le hub qui sera la porte d'entrée.
Pour cela, il faut d'abord créer un fichier dans le dossier "game" qui servira de squelette pour la scène sous cette dénomination : "scene_leNomDeVotreScene.rpy"
Ce fichier doit commencer avec l'élément suivant :
```python
  label leNomDeVotreScene:
    empty "" #cette ligne permet d'éviter que cela entraine des erreurs en affichant un premier texte vide à l'ouverture du label
```
#### Image de l'objet cliquable
Ensuite, il faut créer les images cliquables. Pour cela il faut exporter deux image de l'élément en png transparent, l'une avec un contour blanc et l'autre sans contour blanc. **Ces deux images doivent avoir exactement la même taille.**
![Example d'élément cliquable en version hover et idle](https://github.com/EPN-Argentan/OK-Data/blob/main/src/example_imageButtons.png)
Afin de faciliter le stockage, ces images doivent être stockées dans *OK Data\game\images\UI\imagebuttons* sous l'appelation : nomDeLElement_hover.png (sans contour blanc) et nomDeLElement_idle.png (avec contour blanc)

#### Placement de l'objet
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
#### Mise en fonctionnement de l'objet
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
### Splitter un message à afficher après un gain ou une perte de points
Si votre message, gagnant ou perdant, est trop long, il risque de ne pas être totalement lisible. Pour éviter cela, il suffit d'ajouter dans les textes, à chaque fin d'un message : *"µ"*
# Les dialogues
## Paroles
Pour afficher une parole il suffit de créer un personnage émetteur (si celui-ci n'existe pas déjà) dans le fichier *script.rpy* :
```python
define raccourcisDuNom = Character('nomDuPersonnage', color="#codeColorTextBackground")
```
Puis pour le faire parler, il suffira d'écrire à l'endroit souhaité :
```python
raccourcisDuNom "Le texte à faire dire à votre personnage"
```

## Le téléphone
### Afficher un message dans le téléphone
Pour afficher un message depuis l'interface texto du téléphone, il suffit de créer un personnage émetteur (si celui-ci n'existe pas déjà) dans le fichier *script.rpy* :
```python
define nomDuPersonnage_nvl = Character("nomDuPersonnage", kind=nvl, callback=Phone_ReceiveSound)
```
Puis pour le faire parler, il suffira d'écrire à l'endroit souhaité :
```python
nomDuPersonnage_nvl "Le texte à faire dire à votre personnage"
```
### Retirer les messages précédents
Pour éviter que les anciens messages du téléphone soient visibles au moment de la réception d'un nouveau message, il faut ajouter en amont :
```python
nvl clear
```


