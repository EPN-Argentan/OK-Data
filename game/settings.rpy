#life bar set

init python:
    maxPts = 5
    minPts = -10
    incrPts = 1
    points = {
        'point_interet': [5,0],
        'point_sante': [5,0],
        'point_conviction': [5,0],
        'point_localisation': [5,0],
        'point_sociaux': [5,0],
        'point_administrative': [5,0]
    }
    def checkMinMax():
        for key, value in points.items():
            if value[0] >= maxPts:
                value[0] = maxPts
            if value[0] <= minPts:
                value[0] = minPts