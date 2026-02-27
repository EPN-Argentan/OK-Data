label photoFrameCheck:
$ freeWifiActivate = False
$ WifiState = False
$ DataState = False

hide screen hubElements
stop music fadeout 1.0

#display photo without sister selie or with it depending of previous events (see bar scene)
nvl clear
if shareSelfie == False:
    show frame_slideshow_noselfie with moveinbottom
    a "Ouah, c’est vieux ça !"
else:
    show frame_slideshow_withselfie with moveinbottom
    a "Ah oui c'est vrai, j'avais oublié cette histoire !"
    a "On avait bien rit...Tiens ça ferait un super cadeau souvenir ça"
    a "Elle doit être sur mon cloud !"
    # a "Mais qu’est-ce que cette photo fait là ? Pourvu que personne ne tombe dessus !"
    # e_nvl "Quand tu prends une photo avec ton téléphone, si celui-ci est connecté à ton cloud, la photo peut être automatiquement sauvegardée en ligne."
    # e_nvl "Et là… toute personne ou appareil ayant accès à ce cloud peut aussi y jeter un œil."
    # e_nvl "Pratique pour retrouver tes souvenirs, mais mieux vaut garder un œil sur les paramètres de partage !"



#####################################################################SCREEN#####################################################################
#All scenes elements used in this label

image frame_slideshow_noselfie:
   "/UI/Cadre/slideshowFrame_001.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_002.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_003.png"
   pause 2.5
   repeat

image frame_slideshow_withselfie:
   "/UI/Cadre/frameFunnyPhoto.png"
   pause 2.5
   "/UI/Cadre/slideshowFrame_015.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_002.png"
   pause 2.5
   "UI/Cadre/slideshowFrame_003.png"
   pause 2.5
   repeat
