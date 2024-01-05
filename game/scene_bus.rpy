label bus:
hide screen hubElements
scene busAdFreeze
show busAdReveal
a "c'est bon, ce n'est pas encore mon bus"
$ renpy.pause(3.0, hard=True)
a "mais...mais..."
a "C'est pas possible c'est Thierry !"
a "Mais comment ils ont eu cette photo, je l'ai déjà vu"
a "..."
show screen galeryOpening with easeinbottom
a "C'est moi qui l'ai prise, j'en suis sûre"
show screen galeryNoFilter
hide screen galeryOpening
a "Cherchons"
a "Il faut que je fasse le tri"
show screen galeryFilter
hide screen galeryNoFilter
a "Trouvé !"
hide screen galeryFilter
show getInsideBus
$ renpy.pause(3.0, hard=True)
a "mais comment ils ont obtenu cette photo..."


#All scenes elements used in this label
screen galeryOpening:
    add "UI/applications/galeryOpening.jpg" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen galeryNoFilter:
    add "UI/applications/galeryNoFilter.jpg" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen galeryFilter:
    add "UI/applications/galeryFilter.jpg" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5
