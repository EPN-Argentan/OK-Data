
default lect_mail =[True,True,True]
default cross_cb =True

init:
    style texte_rouge:
        color "#ff0000"  # Rouge

label dataZon :
  nvl clear
  $ default_clicks = 0
  hide screen hubElements
  hide screen phoneDown
  stop music fadeout 1.0
  show zoomPC
  show curseurTexte
  show screen barre_de_vie
  stop music fadeout 1.0
  play music "Trickling Up - Godmode.mp3"
  a "Il serait temps que je check mes mails !"
  window auto hide
  $ renpy.pause(2.0, hard=True)
  show screen desktopbutton
  a "Voyons voir ce que j’ai reçu !"
  while True:
      empty ""



label mailx3 :
    $ renpy.scene(layer="screens")

    show screen mailx3
    with dissolve
    show screen barre_de_vie
    if default_clicks >= 3:
        show screen notifMail
    a "Bon… qu’y a-t-il d’autre !"

    while True:
        empty ""


label brouillon :
    $ renpy.scene(layer="screens")

    show screen pc_vierge
    show screen brouillon

    show screen a_cci

    with dissolve

    show screen barre_de_vie

    a "Ah tiens, j’avais commencé ce mail hier soir…\nIl serait temps de l’envoyer ! "

    a "Je vais l’envoyer à tous mes contacts…\nmais je choisis quoi, moi ? En A ou en CCI ?"

    while True:
        empty ""

label Brouillon_phone_ok :
    $ renpy.scene(layer="screens")

    show screen pc_vierge

    show screen brouillon
    show screen barre_de_vie
    call addPoints(2,'point_sociaux') from _call_addPoints_2
    e_nvl "Bravo ! En effet, les personnes en CCI reçoivent bien le message, mais personne ne voit qu’elles y sont."
    e_nvl "Du coup, tu ne diffuses pas les adresses de tout le monde sans leur autorisation."
    jump mailx3

    while True:
        empty ""


label Brouillon_phone_No:
    $ renpy.scene(layer="screens")

    show screen pc_vierge
    show screen brouillon
    show screen barre_de_vie


    call addPoints(-2,'point_sociaux') from _call_addPoints_3
    e_nvl "Si tu mets plusieurs adresses dans le champ A, tu risques de partager les adresses de tout le monde sans leur accord."
    e_nvl "Quand on écrit à plusieurs personnes en même temps, c’est mieux de mettre les adresses en caché, dans le champ CCI (Copie Carbone Invisible)."
    jump mailx3

    while True:
        empty ""


label mail_coli6mots :
    $ renpy.scene(layer="screens")

    if default_clicks > 3:
        show screen notifMail
    else :
        $ default_clicks = default_clicks+1
        $ lect_mail[0] = False


    show screen pc_vierge
    show screen mail_coli6mots
    with dissolve
    show screen barre_de_vie
    a "Étrange… je ne me rappelle même plus ce que j’ai bien pu commander."

    while True:
        empty ""


label feed_coli6mots :
    $ renpy.scene(layer="screens")

    show screen feed_coli6mots
    show screen barre_de_vie
    a "C’est bien la première fois qu’on me demande\nde payer des frais supplémentaires."

label Noformok :
    nvl clear
    call addPoints(+2,'point_administrative') from _call_addPoints_22
    e_nvl "Bon réflexe ! L’adresse mail de l’expéditeur était suspecte."
    e_nvl "Au moindre doute, évite de cliquer sur des liens ou des boutons." 
    jump mailx3

label phonestopcoli6mots :
    nvl clear
    $ renpy.scene(layer="screens")

    show screen pc_vierge
    show screen feed_coli6mots_statique
    show screen barre_de_vie
    call addPoints(-2,'point_administrative') from _call_addPoints_4
    e_nvl "Adopte le bon réflexe, vérifie toujours l’adresse de l’expéditeur."
    e_nvl "Elle te donne souvent un indice précieux pour repérer une tentative de phishing."
    e_nvl "Les fraudeurs imitent l’apparence d’un message officiel, ta banque, un service de livraison, une administration, pour t’inciter à cliquer, à donner des informations personnelles ou à t’extorquer de l’argent."
    jump mailx3


label superclerc:
    $ renpy.scene(layer="screens")
    if default_clicks > 3:
        show screen notifMail
    else :
        $ default_clicks = default_clicks+1
        $ lect_mail[1] = False


    show screen pc_vierge
    show screen superclerc
    with dissolve
    show screen barre_de_vie
    a "L’adresse me semble correcte …@superclerc.com\nGrace a ma carte fidélité, je peux recevoir mon ticket par mail,\nmais du coup ils ont accès à tout l’historique de mes achats."
    jump mailx3


label mailsepharo :
    $ renpy.scene(layer="screens")
    if default_clicks >= 3:
        show screen notifMail
    else :
        $ default_clicks = default_clicks+1
        $ lect_mail[2] = False


    show screen pc_vierge
    show screen mailsepharo
    with dissolve
    show screen barre_de_vie
    a "Tiens, on n’est jamais tranquille : que tu promènes ton chien\nou que tu sois affalé sur ton canapé, il ne t’oublie jamais."
    jump mailx3

label datazonmail :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen datazonmail
    with dissolve
    show screen barre_de_vie
    scene black
    with dissolve

    a "Ça vaut le coup d’essayer, ça me donnera\npeut-être des idées, qui sait."

    while True:
        empty ""
#label navigateur :
#    $ renpy.scene(layer="screens")
#    show screen mailx3
#    show screen navigateur
#    show screen barre_de_vie
#    a "Bon il faudrait que je trouve le cadeau de ma mère quand même pour le frérôt"
#arrivé du mail dataZon

#label datasearchresultx3 :
#    $ renpy.scene(layer="screens")
#    show screen mailx3
#    show screen datasearchresultx3
#    show screen barre_de_vie
#    a "alors...."
#    while True :
#        empty ""

label datazonsite :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen cookies
    with dissolve
    show screen barre_de_vie
    a "C’est dingue, on ne peut plus rien faire sans ces fichus cookies."
    while True :
        empty ""

label datazonsiteafternocookie :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen datazonsiteafternocookie
    show screen barre_de_vie
    call addPoints(+1,'point_interet') from _call_addPoints_23
    e_nvl "Bien joué ! pas besoin de donner des informations sur ta navigation"
    jump datazonsiteok

label datazonsiteaftercookieok :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen datazonsiteaftercookieok
    show screen barre_de_vie
    call addPoints(-2,'point_conviction') from _call_addPoints_5
    call addPoints(-2,'point_interet') from _call_addPoints_6
    e_nvl "Attention : en acceptant les cookies (ou traceurs), tu autorises une petite armée d’espions numériques à suivre tes moindres faits et gestes ainsi que les informations que tu transmets."
    e_nvl "Cela dit, tous les cookies ne sont pas à jeter, parmi les « nécessaires », certains sont vraiment utiles."
    e_nvl "Par exemple pour conserver le contenu d’un panier d’achat pendant ta navigation sur un site marchand."
    jump datazonsiteok

label datazonsiteok :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen datazonsiteok
    show screen barre_de_vie
    a "Faisons une petite recherche pour voir ce qu’il nous propose… "
    while True :
        empty ""

label aspisite :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen datasearchresultx3
    show screen barre_de_vie
    a "alors...."
    while True :
        empty ""

label aspidatazon_page :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen aspidatazon_page
    with dissolve
    show screen barre_de_vie
    a "alors...."
    while True :
        empty ""

label aspidatazon_pagewithcookies :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen aspidatazon_pagewithcookies
    show screen barre_de_vie
    a "alors...."
    while True :
        empty ""

label aspidatazon_aftercookieok :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen aspidatazon_aftercookieok
    show screen barre_de_vie

    call addPoints(-2,'point_conviction') from _call_addPoints_7
    call addPoints(-2,'point_interet') from _call_addPoints_10
    e_nvl "En acceptant les cookies, tu fournies des informations sur ta façon de d'utiliser le site Internet a Datazon"
    jump aspidatazon_page
    while True :
        empty ""

label aspidatazon_afternocookie :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen aspidatazon_afternocookie
    show screen barre_de_vie

    e_nvl "Bien jouée, pas besoin de donner des informations sur ta navigation"
    jump aspidatazon_page
    while True :
        empty ""


label aspicute :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen aspicute
    show screen barre_de_vie

    a "il est TROOOOP mignon !"
    while True :
        empty ""

label McDyzon :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen McDyzon
    show screen barre_de_vie

    a "il est TROOOOP Badasssss !"
    while True :
        empty ""

label achatAspiCute :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen achatAspiCute
    show screen barre_de_vie

    a "Il pourrait m'offrir les frais de port quand même à ce prix..."
    while True :
        empty ""

label achatmcdyzon :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen achatmcdyzon
    show screen barre_de_vie

    a "Il pourrait m'offrir les frais de port quand même à ce prix..."
    while True :
        empty ""

label paiementmcdyzon :
    $ renpy.scene(layer="screens")
    show screen mailx3
    show screen paiementmcdyzon
    show screen barre_de_vie

    while True :
        empty ""

label CBmcdyson :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen CBmcdyson
    show screen barre_de_vie

    while True :
        empty ""

label validationachat :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen validationachat
    with dissolve
    show screen barre_de_vie
    nvl clear
    if cross_cb == True :
        call addPoints(-4,'point_administrative') from _call_addPoints_11
        e_nvl "Même si tes données de carte bleu sont cryptées, il est préférable de ne pas enregistrer celle-ci sur le site d'achat."
        e_nvl "En cas de piratage cela pourrait être délicat..."
        a "oh zut"
    else :
        call addPoints(2,'point_administrative') from _call_addPoints_12
        e_nvl "Même si tes données de carte bleu sont cryptées, il est préférable en effet de ne pas enregistrer celle-ci sur le site d'achat."
    a "Voilà une bonne chose de faite"
    jump mailconfirmation


label paiementAspiCute :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen paiementAspiCute
    show screen barre_de_vie
    while True :
        empty ""

label CBaspicute :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen CBaspicute
    show screen barre_de_vie
    while True :
        empty ""


label searchaspi :
    $ renpy.scene(layer="screens")
    show screen pc_vierge
    show screen searchaspi
    show screen barre_de_vie
    a "Oh, pas mal du tout : un aspirateur connecté !"
    while True :
        empty ""

label mailconfirmation :
    $ renpy.scene(layer="screens")

    show screen mailconfirmation
    with dissolve
    show screen barre_de_vie
    a "Bon, voilà pour le moment. Allez hop je ferme l'ordinateur !"
    hide screen mailconfirmation
    scene black
    with fade
    $ hubClickable["laptop"]= 0
    $ trackScenarios["laptop"] = True
    jump hub


screen desktopbutton:
    imagebutton:
        xalign 0.517
        yalign 0.435
        idle "UI/datazon/mailbutton_idle.png"
        hover "UI/datazon/mailbutton_hover.png"
        action Jump("brouillon")
#    imagebutton:
#        xalign 0.695
#        yalign 0.43
#        idle "UI/datazon/nav_button_idle.png"
#        hover "UI/datazon/nav_button_hover.png"
#        action Jump("navigateur")


screen pc_vierge :
    add "UI/datazon/pc_vierge.png"

screen brouillon :
    add "UI/datazon/brouillon.png" xalign 0.5 yalign 0.5

#bouton CCI
    imagebutton:
        xalign 0.515
        yalign 0.37
        idle "UI/datazon/zone_envoi_idle.jpg"
        hover "UI/datazon/zone_envoi_hover.jpg"
        action Jump("Brouillon_phone_ok")
#boutton A
    imagebutton:
        xalign 0.515
        yalign 0.32
        idle "UI/datazon/zone_envoi_idle.jpg"
        hover "UI/datazon/zone_envoi_hover.jpg"
        action Jump("Brouillon_phone_No")



screen a_cci :

    fixed:
        xpos 750
        ypos 330

        vbox:
            button:
                    text "{a=information: Le champ A: dans un mail sous entend  A qui on envoie ce mail} A :{/a}" style "texte_rouge"
            button:
                    text "{a=information: Le champ CCI: signifie Copie Carbonne Invisible. Ce champ permet que chaque destinataire d'un mail ne connaîtra pas l'adresse des autres destinataires} CCI :{/a}"

screen mailx3 :
    add "UI/datazon/mailx3.jpg"
    if lect_mail[0]==True :
        imagebutton:
            xalign 0.546
            yalign 0.264
            idle "UI/datazon/mail1_idle.jpg"
            hover "UI/datazon/mail1_hover.jpg"
            action Jump("mail_coli6mots")

    if lect_mail[1]==True :
        imagebutton:
            xalign 0.546
            yalign 0.412
            idle "UI/datazon/mail2_idle.jpg"
            hover "UI/datazon/mail2_hover.jpg"
            action Jump("superclerc")

    if lect_mail[2]==True :
        imagebutton:
            xalign 0.546
            yalign 0.562
            idle "UI/datazon/mail3_idle.jpg"
            hover "UI/datazon/mail3_hover.jpg"
            action Jump("mailsepharo")


screen mail_coli6mots :
    add "UI/datazon/mail_coli6mots.jpeg" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.447
        yalign 0.667
        idle "UI/datazon/formbutton_idle.jpeg"
        hover "UI/datazon/formbutton_hover.jpeg"
        action Jump("feed_coli6mots")

    imagebutton:
        xalign 0.65
        yalign 0.667
        idle "UI/datazon/Noformbutton_idle.jpeg"
        hover "UI/datazon/Noformbutton_hover.jpeg"
        action Jump ("Noformok")

screen feed_coli6mots :
    add "UI/datazon/feedcoli6mots.jpeg" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "UI/datazon/feedcoli6mots.jpeg"
        hover "UI/datazon/feedcoli6mots.jpeg"
        action Jump ("phonestopcoli6mots")

screen feed_coli6mots_statique:
    add "UI/datazon/feedcoli6mots.jpeg" xalign 0.5 yalign 0.5

screen superclerc:
    add "UI/datazon/mailsuperclerc.png" xalign 0.5 yalign 0.5

screen mailsepharo:
    add "UI/datazon/mailsepharo.png" xalign 0.5 yalign 0.5

screen notifMail:
    add "UI/datazon/notif_maildatazon.png" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.562
        yalign 0.285
        idle "UI/datazon/button_maildatazon_idle.png"
        hover "UI/datazon/button_maildatazon_hover.png"
        action Jump ("datazonmail")

screen datazonmail :
    add "UI/datazon/maildatazon.png" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.650
        yalign 0.630
        idle "UI/datazon/button_GOdatazon_idle.png"
        hover "UI/datazon/button_GOdatazon_hover.png"
        action Jump ("datazonsite")

#partie datazon navigateur
screen navigateur:
    add "UI/datazon/datasearch.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.555
        yalign 0.570
        idle "UI/datazon/searchbar_idle.png"
        hover "UI/datazon/searchbar_hover.png"
        action Jump ("datasearchresultx3")

screen datasearchresultx3:
    add "UI/datazon/datasearchresultx3.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.440
        yalign 0.635
        idle "UI/datazon/button_datazon_idle.png"
        hover "UI/datazon/button_datazon_Hover.png"
        action Jump ("datazonsite")
    imagebutton :
        xalign 0.475
        yalign 0.695
        idle "UI/datazon/button_cadeau_idle.png"
        hover "UI/datazon/button_cadeau_Hover.png"
        action Jump ("aspidatazon_pagewithcookies")
    imagebutton :
        xalign 0.475
        yalign 0.765
        idle "UI/datazon/button_aspi_idle.png"
        hover "UI/datazon/button_aspi_Hover.png"
        action Jump ("aspidatazon_pagewithcookies")


screen cookies :
    add "UI/datazon/cookieinfo.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.350
        yalign 0.705
        idle "UI/datazon/okcookie_idle.png"
        hover "UI/datazon/okcookie_hover.png"
        action Jump ("datazonsiteaftercookieok")
    imagebutton :
        xalign 0.645
        yalign 0.705
        idle "UI/datazon/nocookie_idle.png"
        hover "UI/datazon/nocookie_hover.png"
        action Jump ("datazonsiteafternocookie")



screen datazonsite:
    add "UI/datazon/datasite.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.249
        yalign 0.545
        idle "UI/datazon/searchdatazon_idle.png"
        hover "UI/datazon/searchdatazon_hover.png"
        action Jump ("searchaspi")
    add "UI/datazon/cookieinfo.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.350
        yalign 0.705
        idle "UI/datazon/okcookie_idle.png"
        hover "UI/datazon/okcookie_hover.png"
        action Jump ("datazonsiteaftercookieok")
    imagebutton :
        xalign 0.645
        yalign 0.705
        idle "UI/datazon/nocookie_idle.png"
        hover "UI/datazon/nocookie_hover.png"
        action Jump ("datazonsiteafternocookie")

screen datazonsiteafternocookie:
    add "UI/datazon/datasite.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.249
        yalign 0.475
        idle "UI/datazon/searchdatazon_idle.png"
        hover "UI/datazon/searchdatazon_hover.png"
        action Jump ("datazonsiteok")

screen datazonsiteaftercookieok:
    add "UI/datazon/datasite.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.249
        yalign 0.475
        idle "UI/datazon/searchdatazon_idle.png"
        hover "UI/datazon/searchdatazon_hover.png"
        action Jump ("datazonsiteok")

screen datazonsiteok:
    add "UI/datazon/datasite.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.249
        yalign 0.475
        idle "UI/datazon/searchdatazon_idle.png"
        hover "UI/datazon/searchdatazon_hover.png"
        action Jump ("searchaspi")

screen searchaspi:
    add "UI/datazon/datasite_button_aspi.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.249
        yalign 0.532
        idle "UI/datazon/button_aspiconnect_idle.png"
        hover "UI/datazon/button_aspiconnect_hover.png"
        action Jump ("aspidatazon_page")

screen aspidatazon_page:
    add "UI/datazon/aspidatazon_page.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.425
        yalign 0.391
        idle "UI/datazon/button_aspicute_idle.png"
        hover "UI/datazon/button_aspicute_hover.png"
        action Jump ("aspicute")
    imagebutton :
        xalign 0.425
        yalign 0.629
        idle "UI/datazon/button_McDyzon_idle.png"
        hover "UI/datazon/button_McDyzon_hover.png"
        action Jump ("McDyzon")

screen aspidatazon_pagewithcookies:
    add "UI/datazon/aspidatazon_page.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.425
        yalign 0.522
        idle "UI/datazon/button_aspicute_idle.png"
        hover "UI/datazon/button_aspicute_hover.png"
        action Jump ("aspicute")
    imagebutton :
        xalign 0.425
        yalign 0.759
        idle "UI/datazon/button_McDyzon_idle.png"
        hover "UI/datazon/button_McDyzon_hover.png"
        action Jump ("McDyzon")
    add "UI/datazon/cookieinfo.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.350
        yalign 0.705
        idle "UI/datazon/okcookie_idle.png"
        hover "UI/datazon/okcookie_hover.png"
        action Jump ("aspidatazon_aftercookieok")
    imagebutton :
        xalign 0.645
        yalign 0.705
        idle "UI/datazon/nocookie_idle.png"
        hover "UI/datazon/nocookie_hover.png"
        action Jump ("aspidatazon_afternocookie")



screen aspidatazon_aftercookieok :
    add "UI/datazon/aspidatazon_page.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.425
        yalign 0.522
        idle "UI/datazon/button_aspicute_idle.png"
        hover "UI/datazon/button_aspicute_hover.png"
        action Jump ("aspicute")
    imagebutton :
        xalign 0.425
        yalign 0.759
        idle "UI/datazon/button_McDyzon_idle.png"
        hover "UI/datazon/button_McDyzon_hover.png"
        action Jump ("McDyzon")


screen aspidatazon_afternocookie :
    add "UI/datazon/aspidatazon_page.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.425
        yalign 0.522
        idle "UI/datazon/button_aspicute_idle.png"
        hover "UI/datazon/button_aspicute_hover.png"
        action Jump ("aspicute")
    imagebutton :
        xalign 0.425
        yalign 0.759
        idle "UI/datazon/button_McDyzon_idle.png"
        hover "UI/datazon/button_McDyzon_hover.png"
        action Jump ("McDyzon")

screen aspicute:
    add "UI/datazon/aspicute_page.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.655
        yalign 0.650
        idle "UI/datazon/button_panier_idle.png"
        hover "UI/datazon/button_panier_hover.png"
        action Jump ("achatAspiCute")

screen McDyzon:
    add "UI/datazon/mcdyzon_page.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.655
        yalign 0.650
        idle "UI/datazon/button_panier_idle.png"
        hover "UI/datazon/button_panier_hover.png"
        action Jump ("achatmcdyzon")

screen achatmcdyzon:
    add "UI/datazon/feedachatmcdyson.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.455
        yalign 0.715
        idle "UI/datazon/paiement_idle.png"
        hover "UI/datazon/paiement_hover.png"
        action Jump ("paiementmcdyzon")

screen achatAspiCute:
    add "UI/datazon/feedachatAspiCute.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.455
        yalign 0.715
        idle "UI/datazon/paiement_idle.png"
        hover "UI/datazon/paiement_hover.png"
        action Jump ("paiementAspiCute")

screen paiementmcdyzon:
    add "UI/datazon/paiementmcdyzon.png" xalign 0.5 yalign 0.5
    add "UI/datazon/formCBrempli.png" xalign 0.665 yalign 0.600
    imagebutton :
        xalign 0.670
        yalign 0.600
        idle "UI/datazon/buttonCB_idle.png"
        hover "UI/datazon/buttonCB_hover.png"
        action Jump ("CBmcdyson")
    imagebutton :
        xalign 0.4075
        yalign 0.682
        action SetVariable("cross_cb",not cross_cb)
        if cross_cb ==False :
            idle "UI/datazon/checkboxoff.png"
        else :
            idle "UI/datazon/checkboxon.png"


screen paiementAspiCute:
    add "UI/datazon/paiementAspiCute.png" xalign 0.5 yalign 0.5
    add "UI/datazon/formCBrempli.png" xalign 0.665 yalign 0.600
    imagebutton :
        xalign 0.670
        yalign 0.600
        idle "UI/datazon/buttonCB_idle.png"
        hover "UI/datazon/buttonCB_hover.png"
        action Jump ("CBaspicute")
    imagebutton :
        xalign 0.4075
        yalign 0.682
        action SetVariable("cross_cb",not cross_cb)
        if cross_cb ==False :
            idle "UI/datazon/checkboxoff.png"
        else :
            idle "UI/datazon/checkboxon.png"




screen CBmcdyson:
    add "UI/datazon/paiementmcdyzon.png" xalign 0.5 yalign 0.5
    add "UI/datazon/formCBrempli.png" xalign 0.665 yalign 0.600
    imagebutton :
        xalign 0.692
        yalign 0.730
        idle "UI/datazon/validCB_Idle.png"
        hover "UI/datazon/validCB_hover.png"
        action Jump ("validationachat")
    imagebutton :
        xalign 0.4075
        yalign 0.682
        if cross_cb ==True :
            idle "UI/datazon/checkboxon.png"
            action SetVariable("cross_cb", False)
        else :
            idle "UI/datazon/checkboxoff.png"
            action SetVariable("cross_cb", True)


screen CBaspicute:
    add "UI/datazon/paiementAspiCute.png" xalign 0.5 yalign 0.5
    add "UI/datazon/formCBrempli.png" xalign 0.665 yalign 0.600
    imagebutton :
        xalign 0.692
        yalign 0.730
        idle "UI/datazon/validCB_Idle.png"
        hover "UI/datazon/validCB_hover.png"
        action Jump ("validationachat")
    imagebutton :
        xalign 0.4075
        yalign 0.682
        if cross_cb ==True:
            idle "UI/datazon/checkboxon.png"
            action SetVariable("cross_cb", False)
        elif cross_cb ==False:
            idle "UI/datazon/checkboxoff.png"
            action SetVariable("cross_cb", True)



screen validationachat:
    add "UI/datazon/validationachat.png" xalign 0.5 yalign 0.5


screen datasite:
    add "UI/datazon/button_cadeau_idlesite.png" xalign 0.5 yalign 0.5

screen datasite:
    add "UI/datazon/aspisite.png" xalign 0.5 yalign 0.5

screen mailconfirmation:
    add "UI/datazon/pc_vierge.png"
    add "UI/datazon/confirmationmail.png" xalign 0.5 yalign 0.5
