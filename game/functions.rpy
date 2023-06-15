
#function to call to add value to one of lifebar element
# value = number to increment
# key = wich lifebar element has to be increment
# condition = if condition is not empty, increment will be effective if the condition is true else it will decrement
# lsoemessage = message to display if player lose points
# winmessage = message to display if player earn points
# Exemple d'usage de la fonction :
# addPoints(5,'point_sante',BluetoothState,"Vous n'avez pas désactivé le bluetooth", "Vous avez bien pensé à désactiver le bluetooth")
label addPoints(values = 0, key = '', condition = '', losemessage='', winmessage=''):
    call shake(key)
    $ oldValue = points[key][0]
    if not condition:
        $ points[key][0] += values
    else:
        if condition:
            $ points[key][0] += values
        else:
            $ points[key][0] -= values
    $ newValue = points[key][0]

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

label shake( key = '' ):
    $ pauseDelay = 0.05
    $ points[key][1] = 5
    pause pauseDelay
    $ points[key][1] = 4
    pause pauseDelay
    $ points[key][1] = 3
    pause pauseDelay
    $ points[key][1] = 2
    pause pauseDelay
    $ points[key][1] = 1
    pause pauseDelay
    $ points[key][1] = -10
    pause pauseDelay
    $ points[key][1] = 5
