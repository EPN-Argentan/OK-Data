# OK Data
## Videogame about data and privacy
Game has been made on renpy game engine.
It's a point'n'click where you pass through several levels. Each level is about one main idea.

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
Ensuite, il faut créer les images cliquables. Pour cela il faut exporter deux image de l'élément en png transparent, l'une avec un contour blanc de **3px** et l'autre sans contour blanc. **Ces deux images doivent avoir exactement la même taille à l'export.**

![Example d'élément cliquable en version hover et idle](https://github.com/EPN-Argentan/OK-Data/blob/main/src/example_imageButtons.png)

Afin de faciliter le stockage, ces images doivent être stockées dans *OK Data\game\images\UI\imagebuttons* sous l'appelation : nomDeLElement_hover.png (sans contour blanc) et nomDeLElement_idle.png (avec contour blanc)

#### Placement de l'objet
Ensuite, il faut créer l'élément dans le fichier *my_screens.rpy* dans le screen *HubElements* :
```python
  if hubClickable["le_nom_de_votre_element_cliquable"] == 1:
    imagebutton:
      xpos 1400 #la position X du bord supérieur gauche
      ypos 797 #la position Y du bord supérieur gauche
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

##Gestion des bulles
Pour modifier la dimension et l'emplacement des bulles il suffit de se place dans le jeu sur la bulle correspondante et faire shift+R. ensuite, en haut à gauche cliquer sur "AREA... " puis faire un cliquer glisser pour placer et dimensionner la bulle.
## Structure d'un scénario
| Nom de l'élément  | Description |
| ------------- | ------------- |
| label  | Élément principal d'un scénario. C'est une sorte d'encapsuleur dans lequel vous pourrez mettre des images, des éléments d'interfaces, des dialogues. Chaque Scénario s'ouver avec un labl : "label forest :"  |
| screen  | Élément flottant à afficher et positionner où l'on souhaite dans l'image. La barre de vie privée est, par exemple, un screen appelé à chaque fois que celle-ci doit être affichée. Les screens sont rangés dans le fichier "my_screens.rpy"  |
### En attente d'un clic dans le scénario
Dans certains moment du jeu, on souhaite que le joueur clique sur un élément pour avancer. Le problème dans renpy, est que la narration est linéaire et que en l'absence d'éléments, le jeu va s'arrêter tout seul. Pour éviter cela, il suffit d'ajouter, au moment de l'attente, cet élément :
```python
    while True:
        empty ""
```

## Les points
### Typologie de points
La barre de vie privée est composée d'un ensemble de points de vie. Chaque points de vie a un nom spécifique.

![La barre de vie](https://github.com/EPN-Argentan/OK-Data/blob/main/src/example_barre_de_vie.png)

Vous trouverez dans l'ordre :
1. point_interet
2. point_sante
3. point_conviction
4. point_localisation
5. point_sociaux
6. point_administrative

Ce nommage vous sera particuliérement utile si vous souhaitez ajoutez ou retirer des points.

### Ajouter ou enlever des points SANS une condition
Pour ajouter des points de vie sans condition, il suffit d'écrire :
```python
  # $ points['le_nom_des_points'][0] += 5 DEPRECIATE
  call addPoints(5,'point_administrative')
```
Pour retirer des points de vie sans condition, il suffit d'écrire :
```python
    # $ points['le_nom_des_points'][0] -= 5 DEPRECIATE
    call addPoints(-5,'point_administrative')
```

### Ajouter ou enlever des points AVEC une condition
Pour ajouter ou retirer des points de vie selon une condition, une fonction existe :
```python
call addPoints(value,key,condition, conditionValue, "losemessage", "winmessage",labelNext)

# value = number to increment
# key = wich lifebar element has to be increment
# condition = condition to check
# conditionValue = waiting condition value to determine if it's a win or not
# losemessage = message to display if player lose points
# winmessage = message to display if player earn points
# labelNext = jump to the specify label if needed
```
Exemple d'usage de la fonction :
```python
call addPoints(5,'point_sante',BluetoothState,True,"Vous n'avez pas désactivé le bluetooth", "Vous avez bien pensé à désactiver le bluetooth",tuto)
# Si l'état du Bluetooth est activé alors ajoute 5 points et affiche "Vous avez bien pensé à désactiver le bluetooth" et sinon, retire 5 points et affiche "Vous n'avez pas désactivé le bluetooth puis jump au label tuto"
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

#### Mini jeu de l'algorithme
Le jeu de l'algorithme consiste à associer deux éléments (*clues*) pour révéler un indice.
Pour ajouter des éléments à ce jeu, il vous suffit, dans un premier temps, de créer un ensemble d'éléments. Cet ensemble d'éléments dans comporter les deux éléments à associer ensemble et les autres ne servant qu'à être des leurres.
Rendez-vous dans le script *scene_algorithm* et créez un screen comme ceci :

```python
screen nomDeVotreEnsemble:
  text '{font=fonts/FiraCode-Bold.ttf}[cluesDisplay]{/font}'
```

Ensuite, ajoutez un *Dragroup* ainsi :
```python
screen nomDeVotreEnsemble:
  text '{font=fonts/FiraCode-Bold.ttf}[cluesDisplay]{/font}'
    draggroup:
```

Dans ce *dragGroup*, ajoutez deux *drag* qui serviront de zone de dépôt où le joueur viendra *drag and drop* chacun de ses indices à combiner :

```python
screen nomDeVotreEnsemble:
  text '{font=fonts/FiraCode-Bold.ttf}[cluesDisplay]{/font}'
    draggroup:
      drag:
          drag_name "Drop Zone Top"
          child "images/UI/algorithm/dropZone.png"
          align(0.5,0.3)
          draggable False
          droppable True   
      drag:
          drag_name "Drop Zone Bottom"
          child "images/UI/algorithm/dropZone.png"
          align(0.5,0.8)
          draggable False
          droppable True
```
Enfin, ajoutez autant d'éléments *drags* que d'indices que vous souhaitez mettre dedans :

```python
drag:
  drag_name "Nom de votre indice"
  child "images/UI/algorithm/nomDeVotreImageIndice.png"
  align(positionX,positionY)
  draggable True
  droppable False
  dragged drag_placed
  drag_raise True
```  
À la fin vous devez obtenir quelque chose comme ça :

```python
screen catSanté:
    text '{font=fonts/FiraCode-Bold.ttf}[cluesDisplay]{/font}'
    draggroup:
        drag:
            drag_name "Miniature Youtube"
            child "images/UI/algorithm/youtubeMini.png"
            align(0.1,0.2)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Historique de recherche"
            child "images/UI/algorithm/searchHistory.png"
            align(0.3,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Logged"
            child "images/UI/algorithm/logged.png"
            align(0.8,0.6)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True  

        drag:
            drag_name "Drop Zone Top"
            child "images/UI/algorithm/dropZone.png"
            align(0.5,0.3)
            draggable False
            droppable True   
        drag:
            drag_name "Drop Zone Bottom"
            child "images/UI/algorithm/dropZone.png"
            align(0.5,0.8)
            draggable False
            droppable True
```

Une fois votre ensemble (screen créée), vous devez déclarer quels éléments indices combinés ensemble vont donner la bonne réponse.
Pour cela, toujours dans *scene_algorithm*, rendez vous dans la variable *define combinaisonClues*. Il ne vous reste plus qu'à ajouter un élément en respectant cette nomenclature :

```python
'IntituléDeVotreIndice' : ['Nom de votre indice n°1','Nom de votre indice n°2',"MEssage à laissé afficher comme trace de l'indice révélé \n","Dialogue à afficher quand l'indice est trouvé",False, 'nomDeVotreEnsemble',"nom de l'image png de l'icône à afficher sur le coté",False]
```
À noter que si vous souhaitez que votre ensemble d'indice soit le premier révélé dans la séquence, il suffit de placer votre élément en premier de la liste et de mettre le dernier de celui-ci argument à *True* et bien vérifier que tous les autres sont à *False*.

Vous devriez obtenir quelquechose comme ceci :

```python
define combinaisonClues = {
    'Afrique' : ['Miniature Youtube','Historique de recherche',"Afrique \n","mmmm...Il semblerait que cette personne aime l'Afrique",False, 'catIntérêt', 'intérêt',True],
    'Asie' : ['Logged','Historique de recherche',"Asie \n","mmmm...Il semblerait que cette personne aime l'asie",False, 'catSanté', 'santé',False],
    'Europe' : ['Logged','Miniature Youtube',"Europe \n","mmmm...Il semblerait que cette personne aime l'europe",False, 'catConviction', 'conviction',False],
}
```