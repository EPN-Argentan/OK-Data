
define algo = Character("")

#List clues that has to be found to resolve algorithmn mini game 
define combinaisonClues = {
    'Afrique' : ['Miniature Youtube','Historique de recherche',"Afrique \n","mmmm...Il semblerait que cette personne aime l'Afrique",False, 'catIntérêt',True],
    'Asie' : ['Logged','Historique de recherche',"Asie \n","mmmm...Il semblerait que cette personne aime l'asie",False, 'catSanté',False],
    'Europe' : ['Logged','Miniature Youtube',"Europe \n","mmmm...Il semblerait que cette personne aime l'europe",False, 'catConviction',False],
}

#Track how many clues have been found
define categoriesIndex = 0

define cluesDisplay = ""

define dragX = 0.1

define whatInsideTop = ""
define whatInsideBottom = ""

#Function to check wich draggable object is on which
init python:
    def displayData() :
        for key, value in combinaisonClues.items():
            if value[6] == True:
                print(len(combinaisonClues))
                print(value[5])
                renpy.call_screen(value[5])

    def drag_placed(drags, drop):
        if not drop: 
            return

        drags[0].snap(drop.x, drop.y, 0.5)
        # Update the store variables
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        
        return True
    


label algorithmGame:
    show screen algorithmnMenu
    hide screen barre_de_vie
    $ displayData()
    #call screen catAdministrative
    #Enounce all combinaison possible and results
    if droppable == "Drop Zone Top":
        $ whatInsideTop = draggable
    if droppable == "Drop Zone Bottom":
        $ whatInsideBottom = draggable
    if whatInsideTop != "" and whatInsideBottom != "":
        call checkClueALL()
        call clearClues()
    call algorithmGame

label endAlgorithm:
    e_nvl "Analyse terminée"


screen catIntérêt:
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

screen catConviction:
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

screen catLocalisation:
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

screen catSociaux:
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

screen catAdministrative:
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

# Side menu to display all categories
screen algorithmnMenu :
    vbox:
        xalign 0.9
        yalign 0.3
        spacing 35
        #pastille d'intérêt
        imagebutton:
            idle "UI/barre_de_vie/intérêt.png"
            at custom_zoom
            action NullAction()
        #pastille santé
        imagebutton:
            idle "UI/barre_de_vie/santé.png"
            at custom_zoom
            action NullAction()
        #pastille conviction
        imagebutton:
            idle "UI/barre_de_vie/conviction.png"
            at custom_zoom
            action NullAction()
        #pastille localisation
        imagebutton:
            idle "UI/barre_de_vie/conviction.png"
            at custom_zoom
            action NullAction()
        #pastille sociaux
        imagebutton:
            idle "UI/barre_de_vie/sociaux.png"
            at custom_zoom
            action NullAction()
        #pastille administrative
        imagebutton:
            idle "UI/barre_de_vie/administrative.png"
            at custom_zoom
            action NullAction()
transform custom_zoom:
    zoom 0.3
