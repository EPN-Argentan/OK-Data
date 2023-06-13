
#function to call to add value to one of lifebar element
# value = number to increment
# key = wich lifebar element has to be increment
# condition = if condition is not empty, increment will be effective if the condition is true else it will decrement
# lsoemessage = message to display if player lose points
# winmessage = message to display if player earn points
# Exemple d'usage de la fonction :
# addPoints(5,'point_sante',BluetoothState,"Vous n'avez pas désactivé le bluetooth", "Vous avez bien pensé à désactiver le bluetooth")
label addPoints(values = 0, key = '', condition = '', losemessage='', winmessage=''):
    $ oldValue = points[key]
    if not condition:
        $ points[key] += values
    else:
        if condition:
            $ points[key] += values
        else:
            $ points[key] -= values
    $ newValue = points[key]

    #you lose points
    if newValue < oldValue :
        if losemessage:
            e_nvl '[losemessage]'
    #nothing happens
    elif newValue == oldValue :
        return
    #you earn points
    else:
        if winmessage:
            e_nvl '[winmessage]'
