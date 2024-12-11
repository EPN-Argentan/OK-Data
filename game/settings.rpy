#life bar set
init:
    define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'ontop' ]

init -10 python:

    import time
    year, month, day, hour, minute, second, dow, doy, dst = time.localtime()

    maxPts = 20
    minPts = 0
    initPts = 10
    incrPts = 1
    points = {
        'point_interet': [initPts,0],
        'point_sante': [initPts,0],
        'point_conviction': [initPts,0],
        'point_localisation': [initPts,0],
        'point_sociaux': [initPts,0],
        'point_administrative': [initPts,0]
    }
    listePoints = list(points.keys())#get list of keys from points array

    #dynamic list of elements clickable in hub
    #if value == 0, the element can't be clicked
    hubClickable = {
        'dog': 1,
        'laptop': 0 ,
        'photoFrame': 0,
        'watch': 0,
        'tablet': 0,
        'homeAssistant': 0,
        'phone': 0,
        'phoneCall': 0,
        'forest' : 0
    }

    #avoid to go upper than maximum points or lower than minimum points
    def checkMinMax():
        for key, value in points.items():
            if value[0] >= maxPts:
                value[0] = maxPts
            if value[0] <= minPts:
                value[0] = minPts


    #BluetoothState = True
    WifiState = True
    LocalisationState = True
    DataState = True
    NeutralState = True #an invisible variable to add points without using settings

    shareSelfie = False #check if Selfie has been shared or not

    speakerState = True #does speaker is active
    speakerTarget = -1 #Number array element points to target to remove a point
    current_category = 0

