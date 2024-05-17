#life bar set
init python:
    maxPts = 5
    minPts = -10
    initPts = 5
    incrPts = 1
    points = {
        'point_interet': [initPts,0],
        'point_sante': [initPts,0],
        'point_conviction': [initPts,0],
        'point_localisation': [initPts,0],
        'point_sociaux': [initPts,0],
        'point_administrative': [initPts,0]
    }
    

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


    BluetoothState = True
    LocalisationState = True
    DataState = True
    NeutralState = True #an invisible variable to add points without using settings
