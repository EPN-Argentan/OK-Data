screen barre_de_vie :
    $ xposPastille = -30
    $ yposPastille = -20
    $ xtextPastille = -20
    $ ytextPastille = -5

    hbox:
        xalign 0.1
        yalign 0.05

        #pastille d'intérêt
        hbox:
            spacing xposPastille
            imagebutton:
                idle "barre_de_vie/intérêt.png"
                at custom_zoom
            add "barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[point_interet]" xpos xtextPastille ypos ytextPastille

        #pastille santé
        hbox:
            spacing xposPastille
            imagebutton:
                idle "barre_de_vie/santé.png"
                at custom_zoom
            add "barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[point_sante]" xpos xtextPastille ypos ytextPastille

        #pastille conviction
        hbox:
            spacing xposPastille
            imagebutton:
                idle "barre_de_vie/conviction.png"
                at custom_zoom
            add "barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[point_conviction]" xpos xtextPastille ypos ytextPastille

        #pastille localisation
        hbox:
            spacing xposPastille
            imagebutton:
                idle "barre_de_vie/localisation.png"
                at custom_zoom
            add "barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[point_localisation]" xpos xtextPastille ypos ytextPastille

        #pastille sociaux
        hbox:
            spacing xposPastille
            imagebutton:
                idle "barre_de_vie/sociaux.png"
                at custom_zoom
            add "barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[point_sociaux]" xpos xtextPastille ypos ytextPastille

        #pastille administrative
        hbox:
            spacing xposPastille
            imagebutton:
                idle "barre_de_vie/administrative.png"
                at custom_zoom
            add "barre_de_vie/pastilleverte.png" zoom 0.4 ypos yposPastille
            hbox:
                text "[point_administrative]" xpos xtextPastille ypos ytextPastille

transform custom_zoom:
    zoom 0.3
