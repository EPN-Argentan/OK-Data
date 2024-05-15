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
    def checkMinMax():
        for key, value in points.items():
            if value[0] >= maxPts:
                value[0] = maxPts
            if value[0] <= minPts:
                value[0] = minPts