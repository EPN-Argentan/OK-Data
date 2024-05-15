#caption on hover
default mtt = MouseTooltip(Text(""), padding={"x": 10, "y": -10})
transform dark_tint(value):
    matrixcolor  HueMatrix(translate(value, minPts, maxPts, -110, 0))

screen barre_de_vie :
    add mtt # add caption on hover
    $ checkMinMax()
#position of green pastille
    $ xposPastille = -30
    $ yposPastille = -20
#position of text inside green pastille
    $ xtextPastille = -20
    $ ytextPastille = -5
    hbox:
        xalign 0.1
        yalign 0.05
        #pastille d'intérêt
        hbox:
            spacing xposPastille    
            imagebutton:
                idle "UI/barre_de_vie/intérêt.png"
                at custom_zoom
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Intérêt"))]
                action NullAction()
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille at dark_tint(points['point_interet'][0])
            hbox:
                text "[points['point_interet'][0]]" xpos xtextPastille ypos ytextPastille + points['point_interet'][1]

        #pastille santé
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/santé.png"
                at custom_zoom
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Santé"))]
                action NullAction()
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille at dark_tint(points['point_sante'][0])
            hbox:
                text "[points['point_sante'][0]]" xpos xtextPastille ypos ytextPastille + points['point_sante'][1]

        #pastille conviction
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/conviction.png"
                at custom_zoom
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Conviction"))]
                action NullAction()
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille at dark_tint(points['point_conviction'][0])
            hbox:
                text "[points['point_conviction'][0]]" xpos xtextPastille ypos ytextPastille + points['point_conviction'][1]

        #pastille localisation
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/localisation.png"
                at custom_zoom
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Localisation"))]
                action NullAction()
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille at dark_tint(points['point_localisation'][0])
            hbox:
                text "[points['point_localisation'][0]]" xpos xtextPastille ypos ytextPastille + points['point_localisation'][1]

        #pastille sociaux
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/sociaux.png"
                at custom_zoom
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Sociaux"))]
                action NullAction()
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille at dark_tint(points['point_sociaux'][0])
            hbox:
                text "[points['point_sociaux'][0]]" xpos xtextPastille ypos ytextPastille + points['point_sociaux'][1]

        #pastille administrative
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/administrative.png"
                at custom_zoom
                hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Administratif"))]
                action NullAction()
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille at dark_tint(points['point_administrative'][0])
            hbox:
                text "[points['point_administrative'][0]]" xpos xtextPastille ypos ytextPastille + points['point_administrative'][1]
        
    $ tooltip = GetTooltip()

    if tooltip:
        frame:
            background "#00B6ED"
            xpos 500
            yalign 0.17
            text "[tooltip]"

transform custom_zoom:
    zoom 0.3

