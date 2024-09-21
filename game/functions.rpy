# function to call to add value to one of lifebar element
# value = number to increment
# key = wich lifebar element has to be increment
# condition = if condition is not empty, increment will be effective if the condition is true else it will decrement
# losemessage = message to display if player lose points
# winmessage = message to display if player earn points
# labelNext = allow to jump to another label at the end of the function if needed
# Exemple d'usage de la fonction :
# addPoints(5,'point_sante',BluetoothState,True,"Tu n'as pas désactivé le bluetooth", "Tu as bien pensé à désactiver le bluetooth")
label addPoints(values = 0, key = '', condition = '', conditionValue = True, losemessage='', winmessage='', labelNext= ''):
    $ oldValue = points[key][0]
    #start bounce effect
    $ points[key][1] = 1
    if not condition:
        $ points[key][0] += values
    else:
        if condition == conditionValue:
            $ points[key][0] += values
        else:
            $ points[key][0] -= values
    $ newValue = points[key][0]
    nvl clear
    #you lose points
    if newValue < oldValue :
        play sound "loose_point.wav"
        show screen barre_de_vie with hpunch
        if losemessage:
            $ renamePoint = key.replace("point_","")
            $ intro = 'Tu as perdu '+str(values) + ' points de données personnelles de type ' + str(renamePoint)
            e_nvl '[intro]'
            $ phrases = losemessage.split("µ")
            $ nbrPhrases = len(phrases)
            $ i = 0
            while i < nbrPhrases:
                $ phrase = phrases[i]
                e_nvl '[phrase]'
                $ i = i + 1
            #stop bounce effect after mediateur message
            $ points[key][1] = 0
        else:
            #stop bounce effect
            pause 1.2
            $ points[key][1] = 0
    #nothing happens
    elif newValue == oldValue :
        return
    #you earn points
    else:
        play sound "win_point.wav"
        if winmessage:
            #e_nvl '[winmessage]'
            $ renamePoint = key.replace("point_","")
            $ intro = 'Tu as gagné '+str(values) + ' points de données personnelles de type ' + str(renamePoint)
            e_nvl '[intro]'
            $ phrases = winmessage.split("µ")
            $ nbrPhrases = len(phrases)
            $ i = 0
            while i < nbrPhrases:
                $ phrase = phrases[i]
                e_nvl '[phrase]'
                $ i = i + 1
            #stop bounce effect after mediateur message
            $ points[key][1] = 0
        else:
            #stop bounce effect
            pause 1.2
            $ points[key][1] = 0
    #If needed, after text messages, jump to this label if needed
    if not labelNext:
        return
    else:
        $ renpy.scene(layer = "screens")
        $ renpy.jump(labelNext)

#Bounce imagebutton from lifebar
transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -16
    easeout .175 yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat

#Algortihmn function
label checkClueALL():
    python:
        # Stocker toutes les clés dans une liste
        combinaisonKey = list(combinaisonClues.keys())

        # Parcourir les clés dans l'ordre défini
        for i in range(len(combinaisonKey)):
            key = combinaisonKey[i]
            value = combinaisonClues[key]

            if (whatInsideTop == value[0] and whatInsideBottom == value[1]) or (whatInsideTop == value[1] and whatInsideBottom == value[0]):
                if value[4] == False:
                    phrase = value[3]
                    renpy.say(e_nvl, phrase)
                    cluesDisplay += value[2]
                    value[4] = True
                    value[7] = False
                    if categoriesIndex < len(combinaisonClues):
                        categoriesIndex += 1
                        # Vérifier si l'élément suivant existe
                        if i + 1 < len(combinaisonKey):
                            next_key = combinaisonKey[i + 1]
                            combinaisonClues[next_key][7] = True
                    else:
                        
                        renpy.jump('endAlgorithm')
                else:
                    renpy.say(e_nvl, "Tu as déjà trouvé cet indice")
#Count total points
init python:
    def totalPoints():
        totalPts = 0
        for key, value in points.items():
            totalPts = totalPts + value[0]
        return totalPts
           

#clean the clues spot
label clearClues():
    $ whatInsideTop = ""
    $ whatInsideBottom = ""

#Function to display information when click on specific word
style infoStyle:
    xalign 0.5

init python:
  def information_display(txt):
    renpy.call_in_new_context("infoLabel",txt)

label infoLabel(txt = ""):
    if txt:
        info "[txt]"
    else:
        pass

define config.hyperlink_handlers = {
    "information": information_display
}

#Display information bubble clickable to go to ecternal URL

screen sourcesDisplay(title,URL,categorie):
    hbox:
        xcenter 0.8
        ycenter 0.1
        frame:
            padding (12, 8,50,8)
            textbutton title:
                text_color "#fff"
                text_hover_color "#ccc"
                action [OpenURL(URL),Hide("sourcesDisplay"),Call("addPoints",1,categorie,"","","","Il est toujours bon de se renseigner",'')]
            xalign 1.0  yalign 0.5
        imagebutton:
            idle "UI/imagebuttons/InfoUrl.png"
            action NullAction()

#Map function
init python:
    def translate(value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)
