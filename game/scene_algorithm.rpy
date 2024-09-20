    
define algo = Character("")

#List clues that has to be found to resolve algorithmn mini game 
define combinaisonClues = {
    'Afrique' : ['Miniature Youtube','Historique de recherche',"Afrique \n","mmmm...Il semblerait que cette personne aime l'Afrique",False, 'catIntérêt', 'intérêt',True],
    'Asie' : ['Logged','Historique de recherche',"Asie \n","mmmm...Il semblerait que cette personne aime l'asie",False, 'catSanté', 'santé',False],
    'Europe' : ['Logged','Miniature Youtube',"Europe \n","mmmm...Il semblerait que cette personne aime l'europe",False, 'catConviction', 'conviction',False],
}

#Track how many clues have been found
define categoriesIndex = 0

#Text to display with clue resume
define cluesDisplay = ""

define whatInsideTop = ""
define whatInsideBottom = ""

#Function to check wich draggable object is on which
init python:

    def displayData() :
        for key, value in combinaisonClues.items():
            if value[7] == True:
                print(len(combinaisonClues))
                print(value[5])
                renpy.call_screen(value[5])

    def drag_placed(drags, drop):
        global whatInsideTop
        global whatInsideBottom
        if not drop: 
            return
        # Update the store variables
        if drop:
            drags[0].snap(drop.x,drop.y)
            store.draggable = drags[0].drag_name
            store.droppable = drop.drag_name
            if droppable == "Drop Zone Top":
                whatInsideTop = drags[0].drag_name
                print(whatInsideTop)    
            if droppable == "Drop Zone Bottom":
                whatInsideBottom = drags[0].drag_name
                print(whatInsideBottom)
            if whatInsideBottom != "" and whatInsideTop != "":
                renpy.call('checkClueALL')
                renpy.call('clearClues')
            return
        
        return True

label openTablet:
    nvl clear
    hide screen hubElements
    pass 

label algorithmGame:
    nvl clear
    hide screen barre_de_vie
    scene black
    $ displayData()
    #call screen catAdministrative
    #Enounce all combinaison possible and results

    #if droppable == "Drop Zone Top":
    #    $ whatInsideTop = draggable
    #if droppable == "Drop Zone Bottom":
    #    $ whatInsideBottom = draggable
    #if whatInsideTop != "" and whatInsideBottom != "":
    #    call checkClueALL()
    #    call clearClues()
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
        spacing 30
        #pastille d'intérêt
        for key, value in combinaisonClues.items():
            imagebutton :
                if value[4] == False:
                    idle "UI/barre_de_vie/"+value[6]+".png"
                else:
                    idle At("UI/barre_de_vie/"+value[6]+".png", outline_transform(20, "#ffffff", 4.0))
                at custom_zoom
                action NullAction()
transform custom_zoom:
    zoom 0.7