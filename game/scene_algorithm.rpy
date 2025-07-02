    
define algo = Character("")
image backgroundAlgorithm = "images/UI/algorithm/backgroundAlgorithm.jpg" 

#List clues that has to be found to resolve algorithmn mini game 
define combinaisonClues = {
    'Caen': ['BonLocalisation','BonLocalisation',"Caen \n","Il semblerait que cette personne vivie vers Caen",False, 'catLocalisation', 'localisation',True],
    'Cuisine' : ['BonInteret','BonInteret',"Cuisine \n","mmmm...Il semblerait que cette personne apprécie la cuisine",False, 'catIntérêt', 'intérêt',False],
    'Asie' : ['BonSociaux','BonSociaux',"Asie \n","mmmm...Il semblerait que cette personne apprécie l'Asie",False, 'catSociaux', 'sociaux',False],
    'Végétarisme' : ['BonConviction','BonConviction',"Végétarien \n","mmmm...Il semblerait que cette personne ait une affinité avec le végétarisme",False, 'catConviction', 'conviction',False],
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
            drags[0].draggable = False #avoid a droppable objet to be draggable
            drop.droppable = False #avoid a drop zone to contain more than one object
            store.draggable = drags[0].drag_name
            store.droppable = drop.drag_name
            if droppable == "Drop Zone Top":
                whatInsideTop = drags[0].drag_name
                print(f"whatInsideTop updated to: {whatInsideTop}")
            if droppable == "Drop Zone Bottom":
                whatInsideBottom = drags[0].drag_name
                print(f"whatInsideBottom updated to: {whatInsideBottom}")
            if whatInsideBottom != "" and whatInsideTop != "":
                renpy.call('checkClueALL')
                renpy.call('clearClues')
            return

        return True

label openTablet:
    nvl clear
    hide screen hubElements
    hide screen barre_de_vie
    show SearchScreen
    a "ça craint, je ne lui ai toujours rien trouvé comme cadeau..."
    a "une tablette graphique...non il la laissera dans un coin"
    a "Kickboxer !...Non il l'a déjà..."
    a "'Un manque d'inspiration...demandez à notre IA de vous aider'"
    a "pourquoi pas, ça me donnera surement une piste"
    a "Vous êtes l'algorithme de recommendation"
    a "Croisez les données afin d'en extraire des informations sensées"
    nvl clear

label algorithmGame:
    nvl clear
    hide screen hubElements
    hide screen barre_de_vie
    scene black
    scene backgroundAlgorithm
    show screen algorithmnMenu
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
    call algorithmGame from _call_algorithmGame 

label endAlgorithm:
    e_nvl "Analyse terminée"
    a "un cours de cuisine japonnaise végétarienne sur caen"
    a " Super idée !"
    hide screen algorithmnMenu
    $ hubClickable["tablet"]= 0
    jump hub
#####################################################################SCREEN#####################################################################
#All scenes elements used in this label
image SearchScreen:
    "UI/algorithm/SearchScreen.png"
#####################################################################SCREENS#########################################################################
screen catLocalisation:
    text '{font=fonts/FiraCode-Bold.ttf}[cluesDisplay]{/font}'
    draggroup:
        ###True clues display
        drag:
            drag_name "BonLocalisation"
            child "images/UI/algorithm/LogBonneReponse.png"
            hover_child At("images/UI/algorithm/LogBonneReponse.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/LogBonneReponse.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.1,0.2)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "BonLocalisation"
            child "images/UI/algorithm/CarteBonneReponse.png"
            hover_child At("images/UI/algorithm/CarteBonneReponse.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/CarteBonneReponse.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.3,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        ###False clues display
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Log1.png"
            hover_child At("images/UI/algorithm/Log1.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Log1.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.2,0.7)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Log2.png"
            hover_child At("images/UI/algorithm/Log2.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Log2.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Carte1.png"
            hover_child At("images/UI/algorithm/Carte1.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Carte1.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


        drag:
            drag_name "Drop Zone Top"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.3)
            draggable False
            droppable True   
        drag:
            drag_name "Drop Zone Bottom"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.8)
            draggable False
            droppable True


screen catIntérêt:
    text '{font=fonts/FiraCode-Bold.ttf}[cluesDisplay]{/font}'
    draggroup:
        ###True clues display
        drag:
            drag_name "BonInteret"
            child "images/UI/algorithm/SearchBonneReponse.png"
            hover_child At("images/UI/algorithm/SearchBonneReponse.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/SearchBonneReponse.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.1,0.2)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "BonInteret"
            child "images/UI/algorithm/VideoBonneReponse.png"
            hover_child At("images/UI/algorithm/VideoBonneReponse.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/VideoBonneReponse.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.3,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        ###False clues display
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Search1.png"
            hover_child At("images/UI/algorithm/Search1.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Search1.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.2,0.7)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Search2.png"
            hover_child At("images/UI/algorithm/Search2.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Search2.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Search3.png"
            hover_child At("images/UI/algorithm/Search3.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Search3.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Video1.png"
            hover_child At("images/UI/algorithm/Video1.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Video1.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.4,0.3)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Video2.png"
            hover_child At("images/UI/algorithm/Video2.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Video2.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.8)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


        drag:
            drag_name "Drop Zone Top"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.3)
            draggable False
            droppable True   
        drag:
            drag_name "Drop Zone Bottom"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.8)
            draggable False
            droppable True

screen catSanté:
    text '{font=fonts/FiraCode-Bold.ttf}[cluesDisplay]{/font}'
    draggroup:
        drag:
            drag_name "Historique de recherche"
            child "images/UI/algorithm/searchHistory.png"
            hover_child At("images/UI/algorithm/searchHistory.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/searchHistory.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.3,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Logged"
            child "images/UI/algorithm/logged.png"
            hover_child At("images/UI/algorithm/logged.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/logged.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.6)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True  
        ###False clues display
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/likeSister.png"
            hover_child At("images/UI/algorithm/likeSister.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/likeSister.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.2,0.7)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/logCebo.png"
            hover_child At("images/UI/algorithm/logCebo.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/logCebo.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/videoToy.png"
            hover_child At("images/UI/algorithm/videoToy.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/videoToy.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True



        drag:
            drag_name "Drop Zone Top"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.3)
            draggable False
            droppable True   
        drag:
            drag_name "Drop Zone Bottom"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.8)
            draggable False
            droppable True

screen catSociaux:
    text '{font=fonts/FiraCode-Bold.ttf}[cluesDisplay]{/font}'
    draggroup:
        drag:
            drag_name "BonSociaux"
            child "images/UI/algorithm/GroupeBonneReponse.png"
            hover_child At("images/UI/algorithm/GroupeBonneReponse.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/GroupeBonneReponse.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.3,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "BonSociaux"
            child "images/UI/algorithm/CommentBonneReponse.png"
            hover_child At("images/UI/algorithm/CommentBonneReponse.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/CommentBonneReponse.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.6)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True  
        ###False clues display
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Comment1.png"
            hover_child At("images/UI/algorithm/Comment1.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Comment1.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.2,0.7)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Groupe1.png"
            hover_child At("images/UI/algorithm/Groupe1.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Groupe1.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Groupe2.png"
            hover_child At("images/UI/algorithm/Groupe2.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Groupe2.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Groupe3.png"
            hover_child At("images/UI/algorithm/Groupe3.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Groupe3.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.1,0.5)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True



        drag:
            drag_name "Drop Zone Top"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.3)
            draggable False
            droppable True   
        drag:
            drag_name "Drop Zone Bottom"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.8)
            draggable False
            droppable True

screen catConviction:
    text '{font=fonts/FiraCode-Bold.ttf}[cluesDisplay]{/font}'
    draggroup:
        drag:
            drag_name "BonConviction"
            child "images/UI/algorithm/LikeBonneReponse.png"
            hover_child At("images/UI/algorithm/LikeBonneReponse.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/LikeBonneReponse.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.1,0.2)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "BonConviction"
            child "images/UI/algorithm/CommentBonneReponse.png"
            hover_child At("images/UI/algorithm/CommentBonneReponse.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/CommentBonneReponse.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.8,0.6)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True  
        ###False clues display
        drag:
            drag_name "Mauvais indice"
            child "images/UI/algorithm/Like1.png"
            hover_child At("images/UI/algorithm/Like1.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            selected_child At("images/UI/algorithm/Like1.png", outline_transform(10, "#16ec4f", 4.0))
            align(0.2,0.7)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


        drag:
            drag_name "Drop Zone Top"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.3)
            draggable False
            droppable True   
        drag:
            drag_name "Drop Zone Bottom"
            child "images/UI/algorithm/dropZone.png"
            selected_child At("images/UI/algorithm/dropZone.png", glow_outline(25, "#16ec4f", num_passes=15, smoothstep=False))
            align(0.5,0.8)
            draggable False
            droppable True


# Side menu to display all categories
screen algorithmnMenu :
    add "UI/algorithm/+.png" xpos 936 ypos 536
    text "{font=fonts/FiraCode-Bold.ttf}{size=*2}{color=#00B6ED}Croisez les\ndonnées{/color}{/size}{/font}":
        xalign 0.5
        yalign 0.1 
        textalign 0.5 
    vbox:
        xalign 0.95
        yalign 0.3
        spacing 30
        #pastille d'intérêt
        for key, value in combinaisonClues.items():
            imagebutton :
                xalign 0.5
                if value[4] == False:
                    if value[7]:
                        idle "UI/barre_de_vie/"+value[6]+".png" at higlight_zoom
                    else:
                        idle "UI/barre_de_vie/"+value[6]+".png" at greyscale(), custom_zoom
                else:
                    idle At("UI/barre_de_vie/"+value[6]+".png", outline_transform(20, "#ffffff", 4.0))
                at custom_zoom
                action NullAction()
transform custom_zoom:
    zoom 0.7

transform higlight_zoom:
    zoom 0.4
    
