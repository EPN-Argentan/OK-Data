screen barre_de_vie :

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
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[points['point_interet'][0]]" xpos xtextPastille ypos ytextPastille + points['point_interet'][1]

        #pastille santé
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/santé.png"
                at custom_zoom
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[points['point_sante'][0]]" xpos xtextPastille ypos ytextPastille + points['point_sante'][1]

        #pastille conviction
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/conviction.png"
                at custom_zoom
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[points['point_conviction'][0]]" xpos xtextPastille ypos ytextPastille + points['point_conviction'][1]

        #pastille localisation
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/localisation.png"
                at custom_zoom
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[points['point_localisation'][0]]" xpos xtextPastille ypos ytextPastille + points['point_localisation'][1]

        #pastille sociaux
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/sociaux.png"
                at custom_zoom
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[points['point_sociaux'][0]]" xpos xtextPastille ypos ytextPastille + points['point_sociaux'][1]

        #pastille administrative
        hbox:
            spacing xposPastille
            imagebutton:
                idle "UI/barre_de_vie/administrative.png"
                at custom_zoom
            add "UI/barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[points['point_administrative'][0]]" xpos xtextPastille ypos ytextPastille + points['point_administrative'][1]

transform custom_zoom:
    zoom 0.3
