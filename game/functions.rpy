
# function to call to add value to one of lifebar element
# value = number to increment
# key = wich lifebar element has to be increment
# condition = if condition is not empty, increment will be effective if the condition is true else it will decrement
# losemessage = message to display if player lose points
# winmessage = message to display if player earn points
# Exemple d'usage de la fonction :
# addPoints(5,'point_sante',BluetoothState,True,"Vous n'avez pas désactivé le bluetooth", "Vous avez bien pensé à désactiver le bluetooth")
label addPoints(values = 0, key = '', condition = '', conditionValue = True, losemessage='', winmessage=''):
    $ oldValue = points[key][0]
    if not condition:
        $ points[key][0] += values
    else:
        if condition == conditionValue:
            $ points[key][0] += values
        else:
            $ points[key][0] -= values
    $ newValue = points[key][0]

    #you lose points
    if newValue < oldValue :
        show screen barre_de_vie with hpunch
        if losemessage:
            e_nvl '[losemessage]'
    #nothing happens
    elif newValue == oldValue :
        return
    #you earn points
    else:
        if winmessage:
            e_nvl '[winmessage]'
            #$ phrases = winmessage.split("µ")
            #$ nbrPhrases = len(phrases)
            #$ i = 1
            #e_nvl '[phrases[i]]'
