
default lect_mail =[True,True,True]
default cross_cb =True

label dataZon :
  nvl clear
  $ default_clicks = 0
  hide screen hubElements
  hide screen phoneDown
  show zoomPC
  show screen barre_de_vie
  a "allors mail ou Internet ?"
  show screen desktopbutton
  a "allons-y !"


label mailx3 :
    $ renpy.scene(layer="screens")
    show screen barre_de_vie
    show screen mailx3
    if default_clicks >= 3:
        show screen notifMail
    a "hum... je lis quel mail"

    while True:
        empty ""


label brouillon :
    $ renpy.scene(layer="screens")
    show screen barre_de_vie
    show screen brouillon
    a "Ah mais oui mon mail d'hier soir... Je dois le finir."
    a "Bon je l'envoi à tous mes contacts. J'envoi en A ou en CCI ?"

    while True:
        empty ""

label Brouillon_phone_ok :
    $ renpy.scene(layer="screens")
    show screen barre_de_vie
    show screen brouillon
    call addPoints(2,'point_sociaux')
    e_nvl "Bravo, En effet rien ne sert de communiquer les mails de tes proches à tous"
    jump mailx3

label Brouillon_phone_No:
    $ renpy.scene(layer="screens")
    show screen barre_de_vie
    show screen brouillon
    call addPoints(-2,'point_sociaux')
    e_nvl "Il faut mieux éviter de placer tous tes contacts dans A car tu communiques les adresses à tous."
    jump mailx3

label mail_coli6mots :
    $ renpy.scene(layer="screens")
    if default_clicks > 3:
        show screen notifMail
    else :
        $ default_clicks = default_clicks+1
        $ lect_mail[0] = False
        show screen notifMail

    show screen mail_coli6mots
    show screen barre_de_vie
    a "Hum un colis ?"

    while True:
        empty ""


label feed_coli6mots :
    $ renpy.scene(layer="screens")
    show screen feed_coli6mots
    show screen barre_de_vie
    a "Oh Zut !"

label Noformok :
    nvl clear
    e_nvl "Bravo, il ne faut pas en effet répondre à ce genre de mail. L'adresse mail était suspecte"
    jump mailx3

label phonestopcoli6mots :
    nvl clear
    $ renpy.scene(layer="screens")
    show screen feed_coli6mots_statique
    show screen barre_de_vie
    call addPoints(-2,'point_administrative')
    e_nvl "Zut, voici un mail du type phishing qui cherche à dérober des informations et à vous extorquer de l'argent."
    e_nvl "Pensez à vérifier l'adresse de l'expéditeur avant de cliquer"
    jump mailx3


label superclerc:
    $ renpy.scene(layer="screens")
    if default_clicks > 3:
        show screen notifMail
    else :
        $ default_clicks = default_clicks+1
        $ lect_mail[1] = False
        show screen notifMail

    show screen superclerc
    show screen barre_de_vie
    a "ok, mon ticket de course"
    jump mailx3

label mailsepharo :
    $ renpy.scene(layer="screens")
    if default_clicks >= 3:
        show screen notifMail
    else :
        $ default_clicks = default_clicks+1
        $ lect_mail[2] = False
        show screen notifMail

    show screen mailsepharo
    show screen barre_de_vie
    a "Oh ? Ah oui c'est vrai j'avais laissé ma géolocalisation activée"
    jump mailx3

label datazonmail :
    $ renpy.scene(layer="screens")
    show screen datazonmail

    a "Oh, c'est gentil de penser à me le rappeler..."

label navigateur :
    $ renpy.scene(layer="screens")
    show screen navigateur
    show screen barre_de_vie
    a "Bon il faudrait que je trouve le cadeau de ma mère quand même pour le frérôt"
#arrivé du mail dataZon

label datasearchresultx3 :
    $ renpy.scene(layer="screens")
    show screen datasearchresultx3
    show screen barre_de_vie
    a "alors...."
    while True :
        empty ""

label datazonsite :
    $ renpy.scene(layer="screens")
    show screen datazonsite
    show screen barre_de_vie
    a "Encore les cookies...."
    while True :
        empty ""

label datazonsiteafternocookie :
    $ renpy.scene(layer="screens")
    show screen datazonsiteafternocookie
    show screen barre_de_vie
    e_nvl "Bien jouée, pas besoin de donner des informations sur ta navigation"
    jump datazonsiteok

label datazonsiteaftercookieok :
    $ renpy.scene(layer="screens")
    show screen datazonsiteaftercookieok
    show screen barre_de_vie
    call addPoints(-2,'point_conviction')
    call addPoints(-2,'point_interet')
    e_nvl "En acceptant les cookies, tu fournies des informations sur ta façon de d'utiliser le site Internet a Datazon"
    jump datazonsiteok

label datazonsiteok :
    $ renpy.scene(layer="screens")
    show screen datazonsiteok
    show screen barre_de_vie
    a "ah je peux enfin acheter un truc"
    while True :
        empty ""

label aspisite :
    $ renpy.scene(layer="screens")
    show screen datasearchresultx3
    show screen barre_de_vie
    a "alors...."
    while True :
        empty ""

label aspidatazon_page :
    $ renpy.scene(layer="screens")
    show screen aspidatazon_page
    show screen barre_de_vie
    a "alors...."
    while True :
        empty ""

label aspidatazon_pagewithcookies :
    $ renpy.scene(layer="screens")
    show screen aspidatazon_pagewithcookies
    show screen barre_de_vie
    a "alors...."
    while True :
        empty ""

label aspidatazon_aftercookieok :
    $ renpy.scene(layer="screens")
    show screen aspidatazon_aftercookieok
    show screen barre_de_vie

    call addPoints(-2,'point_conviction')
    call addPoints(-2,'point_interet')
    e_nvl "En acceptant les cookies, tu fournies des informations sur ta façon de d'utiliser le site Internet a Datazon"
    jump aspidatazon_page
    while True :
        empty ""

label aspidatazon_afternocookie :
    $ renpy.scene(layer="screens")
    show screen aspidatazon_afternocookie
    show screen barre_de_vie

    e_nvl "Bien jouée, pas besoin de donner des informations sur ta navigation"
    jump aspidatazon_page
    while True :
        empty ""


label aspicute :
    $ renpy.scene(layer="screens")
    show screen aspicute
    show screen barre_de_vie

    a "il est TROOOOP mignon !"
    while True :
        empty ""

label McDyzon :
    $ renpy.scene(layer="screens")
    show screen McDyzon
    show screen barre_de_vie

    a "il est TROOOOP Badasssss !"
    while True :
        empty ""

label achatAspiCute :
    $ renpy.scene(layer="screens")
    show screen achatAspiCute
    show screen barre_de_vie

    a "Il pourrait m'offrir les frais de port quand même à ce prix..."
    while True :
        empty ""

label achatmcdyzon :
    $ renpy.scene(layer="screens")
    show screen achatmcdyzon
    show screen barre_de_vie

    a "Il pourrait m'offrir les frais de port quand même à ce prix..."
    while True :
        empty ""

label paiementmcdyzon :
    $ renpy.scene(layer="screens")
    show screen paiementmcdyzon
    show screen barre_de_vie

    while True :
        empty ""

label CBmcdyson :
    $ renpy.scene(layer="screens")
    show screen CBmcdyson
    show screen barre_de_vie

    while True :
        empty ""

label validationachat :
    $ renpy.scene(layer="screens")
    show screen validationachat
    show screen barre_de_vie
    nvl clear
    if cross_cb == True :
        call addPoints(-4,'point_administrative')
        e_nvl "Même si tes données de carte bleu sont cryptées, il est préférable de ne pas enregistrer celle-ci sur le site d'achat."
        e_nvl "En cas de piratage cela pourrait être délicat..."
        a "oh zut"
    else :
        call addPoints(4,'point_administrative')
        e_nvl "Même si tes données de carte bleu sont cryptées, il est préférable en effet de ne pas enregistrer celle-ci sur le site d'achat."
    a "Voilà une bonne chose de faite"
    jump mailconfirmation


label paiementAspiCute :
    $ renpy.scene(layer="screens")
    show screen paiementAspiCute
    show screen barre_de_vie
    while True :
        empty ""

label CBaspicute :
    $ renpy.scene(layer="screens")
    show screen CBaspicute
    show screen barre_de_vie
    while True :
        empty ""


label searchaspi :
    $ renpy.scene(layer="screens")
    show screen searchaspi
    show screen barre_de_vie
    a "oui, un aspirateur connecté. Bonne idée !"
    while True :
        empty ""

label mailconfirmation :
    $ renpy.scene(layer="screens")
    show screen mailconfirmation
    show screen barre_de_vie
    a "Bon, voilà pour le moment. Allez hop je ferme l'ordinateur !"
    hide screen mailconfirmation
    jump hub


screen desktopbutton:
    imagebutton:
        xalign 0.515
        yalign 0.43
        idle "UI/datazon/mailbutton_idle.png"
        hover "UI/datazon/mailbutton_hover.png"
        action Jump("brouillon")
#    imagebutton:
#        xalign 0.695
#        yalign 0.43
#        idle "UI/datazon/nav_button_idle.png"
#        hover "UI/datazon/nav_button_hover.png"
#        action Jump("navigateur")

screen brouillon :
    add "UI/datazon/brouillon.png" xalign 0.5 yalign 0.5
#bouton CCI
    imagebutton:
        xalign 0.515
        yalign 0.43
        idle "UI/datazon/zone_envoi_idle.jpg"
        hover "UI/datazon/zone_envoi_hover.jpg"
        action Jump("Brouillon_phone_ok")
#boutton A
    imagebutton:
        xalign 0.515
        yalign 0.39
        idle "UI/datazon/zone_envoi_idle.jpg"
        hover "UI/datazon/zone_envoi_hover.jpg"
        action Jump("Brouillon_phone_No")

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
        xalign 0.450
        yalign 0.792
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
        yalign 0.545
        idle "UI/datazon/searchdatazon_idle.png"
        hover "UI/datazon/searchdatazon_hover.png"
        action Jump ("datazonsiteok")

screen datazonsiteaftercookieok:
    add "UI/datazon/datasite.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.249
        yalign 0.545
        idle "UI/datazon/searchdatazon_idle.png"
        hover "UI/datazon/searchdatazon_hover.png"
        action Jump ("datazonsiteok")

screen datazonsiteok:
    add "UI/datazon/datasite.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.249
        yalign 0.545
        idle "UI/datazon/searchdatazon_idle.png"
        hover "UI/datazon/searchdatazon_hover.png"
        action Jump ("searchaspi")

screen searchaspi:
    add "UI/datazon/datasite_button_aspi.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.249
        yalign 0.605
        idle "UI/datazon/button_aspiconnect_idle.png"
        hover "UI/datazon/button_aspiconnect_hover.png"
        action Jump ("aspidatazon_page")

screen aspidatazon_page:
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
        yalign 0.745
        idle "UI/datazon/button_panier_idle.png"
        hover "UI/datazon/button_panier_hover.png"
        action Jump ("achatAspiCute")

screen McDyzon:
    add "UI/datazon/mcdyzon_page.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.655
        yalign 0.745
        idle "UI/datazon/button_panier_idle.png"
        hover "UI/datazon/button_panier_hover.png"
        action Jump ("achatmcdyzon")

screen achatmcdyzon:
    add "UI/datazon/feedachatmcdyson.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.455
        yalign 0.745
        idle "UI/datazon/paiement_idle.png"
        hover "UI/datazon/paiement_hover.png"
        action Jump ("paiementmcdyzon")

screen achatAspiCute:
    add "UI/datazon/feedachatAspiCute.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.455
        yalign 0.745
        idle "UI/datazon/paiement_idle.png"
        hover "UI/datazon/paiement_hover.png"
        action Jump ("paiementAspiCute")

screen paiementmcdyzon:
    add "UI/datazon/paiementmcdyzon.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.670
        yalign 0.680
        idle "UI/datazon/buttonCB_idle.png"
        hover "UI/datazon/buttonCB_hover.png"
        action Jump ("CBmcdyson")


screen paiementAspiCute:
    add "UI/datazon/paiementAspiCute.png" xalign 0.5 yalign 0.5
    imagebutton :
        xalign 0.670
        yalign 0.680
        idle "UI/datazon/buttonCB_idle.png"
        hover "UI/datazon/buttonCB_hover.png"
        action Jump ("CBaspicute")



screen CBmcdyson:
    add "UI/datazon/paiementmcdyzon.png" xalign 0.5 yalign 0.5
    add "UI/datazon/formCBrempli.png" xalign 0.665 yalign 0.685
    imagebutton :
        xalign 0.692
        yalign 0.799
        idle "UI/datazon/validCB_Idle.png"
        hover "UI/datazon/validCB_hover.png"
        action Jump ("validationachat")

screen CBaspicute:
    add "UI/datazon/paiementAspiCute.png" xalign 0.5 yalign 0.5
    add "UI/datazon/formCBrempli.png" xalign 0.665 yalign 0.685
    imagebutton :
        xalign 0.692
        yalign 0.799
        idle "UI/datazon/validCB_Idle.png"
        hover "UI/datazon/validCB_hover.png"
        action Jump ("validationachat")
    imagebutton :
        xalign 0.4075
        yalign 0.751
        if cross_cb ==True :
            idle "UI/datazon/checkboxon.png"
            action SetVariable("cross_cb", "False")
        else :
            idle "UI/datazon/checkboxoff.png"
            action SetVariable("cross_cb", "True")



screen validationachat:
    add "UI/datazon/validationachat.png" xalign 0.5 yalign 0.5


screen datasite:
    add "UI/datazon/button_cadeau_idlesite.png" xalign 0.5 yalign 0.5

screen datasite:
    add "UI/datazon/aspisite.png" xalign 0.5 yalign 0.5

screen mailconfirmation:
    add "UI/datazon/confirmationmail.png" xalign 0.5 yalign 0.5
