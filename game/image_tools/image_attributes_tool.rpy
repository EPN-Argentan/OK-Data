################################################################################
##
## Image Attributes Tool by Feniks (feniksdev.itch.io / feniksdev.com) v1.5
##
################################################################################
## This file contains the code and screens for the Image Attributes Tool.
## This tool requires image_tool_common.rpy to work.
##
## If you use these tools during development, credit me as Feniks @ feniksdev.com
##
## This tool is designed to be used during development only, and should be
## excluded from a proper build. The code to do so is included with this file.
##
## It also has a visual component, and includes in-game tutorials you can
## go through to learn how to use the tools.
## To access the tools, simply make yourself a button (probably on the main
## menu) that goes to the main tool screen, image_tools:
##
# textbutton "Image Tools" action ShowMenu("image_tools")
##
## Then you can select the Image Attributes Tool button and get started.
## You will be shown the tutorial the first time you use a tool.
## Leave a comment on the tool page on itch.io if you run into any issues!
################################################################################
## VARIABLES
################################################################################
## Persistent ##################################################################
################################################################################
## Saved filters
default persistent.sprt_saved_filters = []

## Tutorial flags
default persistent.sprt_tutorial1_shown = False

## Remember the position of the image drag
default persistent.sprt_text_xpos = config.screen_width-int(config.screen_width/2.2)
default 10 persistent.sprt_text_ypos = sprt.SPACER*3

## Normal ######################################################################
################################################################################
## A query that filters out the attributes to apply to the image
default sprt.search = ""

################################################################################
## FUNCTIONS
################################################################################
init -80 python in sprt:

    def record_sprt_drag_pos(drags, drop):
        """
        Remember where the box with image attributes was dragged to.

        Parameters:
        -----------
        drags : Drag[]
            A list of Drag objects (which will contain one Drag, the window).
        drop : Drag
            The Drag object that was dropped onto; this will always be None
            since there are no drop targets.
        """
        if not drags:
            return
        drag = drags[0]
        persistent.sprt_text_xpos = drag.x
        persistent.sprt_text_ypos = drag.y

    def get_current_attributes(who, what):
        """
        Retrieve the attributes being currently applied to the image, not
        including the tag.

        Parameters:
        -----------
        who : str
            The image tag of the image.
        what : str
            The attributes being applied to the image.

        Returns:
        --------
        (tag, attributes[])
            A tuple of the image tag plus a list of the attributes being applied
            to the image.
        """
        tag, attrs = get_tag_attrs(who, what, adjust=False)

        return attrs

    def remove_attr(attr):
        """
        Remove the provided attribute from the attributes
        applied to this image.
        """
        global persistent, what

        dev_who = persistent.sprt_who.split(' ')
        dev_what = what.split(' ')

        if attr in dev_what:
            dev_what.remove(attr)
            what = ' '.join(dev_what)
            return
        if attr in dev_who:
            dev_who.remove(attr)
            persistent.sprt_who = ' '.join(dev_who)
            return

    def get_possible_attributes(dev_who, search):
        """
        Return all the attributes that it's possible to apply to this image,
        based on the currently applied attributes and any filtered search
        queries.

        Parameters:
        -----------
        dev_who : string
            The image tag of the image.
        search : string
            The search query to filter the attributes by.
        """
        global what, swap_attr

        current_img = get_image(dev_who)
        if current_img == "image_not_found":
            if not dev_who or what:
                return [ ]

        tag, attrs = get_tag_attrs(dev_who, what, filter_swap=True)
        # Otherwise, it's valid
        ret = get_ordered_image_attributes(tag, attrs, sort=lambda x: x)
        if ret:
            ret.sort()

        if swap_attr: # They have an attribute to swap out
            tag2, attrs2 = get_tag_attrs(dev_who, swap_attr)
            # Compare the list of attributes that can only be used if the
            # filter attribute isn't present
            ret2 = get_ordered_image_attributes(tag2, attrs2, sort=lambda x: x)
            stable_attrs = [x for x in ret if x in ret2]
            ## Keep the stable attribute in there so the attributes aren't
            ## moving around all the time
            stable_attrs.remove(swap_attr)
        else:
            stable_attrs = [ ]

        # Also filter out "notransform"
        stable_attrs.append("notransform")

        # Filter out stable attributes
        ret = [x for x in ret if x not in stable_attrs]

        if search:
            # Filter based on search
            return filter(lambda x: search in x, ret)
        else:
            return ret

    def add_attribute(attr, short_form=False):
        """
        Add a new attribute to this image.
        """
        global what, swap_attr, persistent
        if short_form:
            attr = transform_attr(persistent.sprt_who, attr)
            ## Remove the name
            if attr.startswith(persistent.sprt_who):
                attr = attr[len(persistent.sprt_who):].strip()
            ## Also remove any duplicates
            attr_list = attr.split(' ')
            attr_list = [x for x in attr_list if x not in what.split(' ')]
            attr = ' '.join(attr_list)
        elif swap_attr:
            # Remove the swap attribute
            remove_attr(swap_attr)
            # This new attribute should replace the current swap attribute
            swap_attr = attr
        what += ' ' + attr
        what = what.strip()

    def copy_image_to_clipboard(copy_all=True):
        """
        Copy the image attributes to the clipboard. If copy_all is True, also
        copies the tag/name of the image. Otherwise, just copies the
        attributes (suitable for copying into dialogue, for example).
        """
        global persistent, what
        if copy_all:
            tag, attrs = get_tag_attrs(persistent.sprt_who, what)
            result = tag
            result += ' '
            if len(attrs) > 1:
                result += ' '.join(attrs)
            elif attrs:
                result += attrs[0]
            result = "show " + result
        else:
            result = what

        result = result.strip()
        copy_to_clipboard(result)

    def save_shortform():
        """
        Saves the inputted short form for the current image tag.
        """
        global persistent, what

        if what not in persistent.sprt_shortforms:
            persistent.sprt_shortforms.add(what)
            renpy.notify("Saved!")
        else:
            renpy.notify("Short form already added.")
        what = ""

    ## Note: this function exists in the engine, but it does not correctly
    ## convert the attributes to a list, so it is reimplemented here with
    ## that correction.
    def get_ordered_image_attributes(tag, attributes=(), sort=None):
        """
        :doc: image_func

        Returns a list of image attributes, ordered in a way that makes sense to
        present to the user.

        `attributes`
            If present, only attributes that are compatible with the given
            attributes are considered. (Compatible means that the attributes
            can be in a single image at the same time.)

        `sort`
            If not None, the returned list of attributes is sorted. This is a
            one-argument function that should be used as a tiebreaker - see
            `this tutorial <https://docs.python.org/3/howto/sorting.html#key-functions>`_
            for more information.
        """
        import collections

        sequences = [ ]

        attrcount = collections.defaultdict(int)
        attrtotalpos = collections.defaultdict(float)

        for attrs, d in sorted(renpy.display.image.image_attributes[tag].items()):

            la = getattr(d, "_list_attributes", None)
            if la is not None:

                sequence = list(attrs) + list(la(tag, [ i for i in attributes if i not in attrs ]))

                if not all(i in sequence for i in attributes):
                    continue

                sequences.append(sequence)

            else:

                if not all(i in attrs for i in attributes):
                    continue

                for i, attr in enumerate(attrs):
                    attrcount[attr] += 1
                    attrtotalpos[attr] += i

        if sort is None:
            return list(set(attrcount.keys()) | set(j for i in sequences for j in i))

        # If we have a sequence, do a topological sort on the before-after relation -
        # with an adjustment to make sure it will complete even if it loops.

        rv = [ ]

        # A map from an attribute to all the attributes it is after.
        after = collections.defaultdict(set)

        for i in sequences:
            while i:

                j = i.pop(0)

                # Ensure it exists.
                after[j]

                for k in i:
                    after[k].add(j)

        while after:

            mincount = min(len(i) for i in after.values())
            ready = set(k for k, v in after.items() if len(v) == mincount)

            for i in ready:
                del after[i]

            for k in after:
                after[k] = after[k] - ready

            ready = list(ready)
            ready.sort(key=lambda a : (sort(a), a))

            rv.extend(ready)

        l = [ ]

        for attr in attrcount:
            if attr not in rv:
                l.append((attrtotalpos[attr] // attrcount[attr], sort(attr), attr))

        l.sort()
        for i in l:
            rv.append(i[2])

        return rv

################################################################################
## SCREENS
################################################################################
################################################################################
## The Expression tester (textbutton-based input)
screen image_attribute_tool():
    tag menu

    ## Ensure coordinates are saved so you don't have to reposition
    ## the image each time the tool is used.
    on 'replaced' action Function(sprt.save_xyinitial)

    ## Ensure the user sees the tutorial the first time they open this screen
    if not persistent.sprt_tutorial1_shown:
        on 'replace' action ShowMenu("sprt_tutorial1")
        on 'show' action ShowMenu("sprt_tutorial1")

    predict False ## Too much happening in this screen to predict

    default sprt_search = SpecialInputValue(store.sprt, 'search')

    use image_attribute_tool_common():
        style_prefix 'sprt_pick'
        ## Header & Clear button
        hbox:
            label "Current Attributes" style 'sprt_label'
            if sprt.what:
                textbutton "Clear":
                    style 'sprt_small_button'
                    action [SetField(sprt, "what", ""),
                            SetField(sprt, "swap_attr", "")]
        ## Attribute list
        hbox:
            for attr in sprt.get_current_attributes(persistent.sprt_who, sprt.what):
                textbutton attr:
                    selected sprt.swap_attr == attr
                    if sprt.swap_attr == attr:
                        action ToggleField(sprt, "swap_attr", attr, None)
                    else:
                        action Function(sprt.remove_attr, attr)
                    alternate ToggleField(sprt, "swap_attr", attr, None)
        ## Filter Input
        hbox:
            spacing sprt.PADDING*2 xmaximum int(config.screen_width/2.2)-150
            style_prefix 'sprt_small' xalign 0.5
            # This is silly but the code plugin colouring freaks out otherwise
            label "{}".format("Filter:") yalign 0.5
            button:
                key_events True style_prefix 'sprt_input'
                action sprt_search.Toggle()
                input value sprt_search
            textbutton "Clear":
                action SetField(sprt, "search", "")
        ## Save & Clear filters
        hbox:
            style_prefix 'sprt_small' xalign 0.5
            textbutton "Save Current Filter":
                sensitive (sprt.search and sprt.search not in persistent.sprt_saved_filters)
                action AddToSet(persistent.sprt_saved_filters, sprt.search)
            textbutton "Clear Saved Filters":
                sensitive persistent.sprt_saved_filters
                action SetField(persistent, 'sprt_saved_filters', [])
        ## Saved Filters
        hbox:
            box_wrap True spacing sprt.PADDING*2 box_wrap_spacing sprt.PADDING*2
            style_prefix 'sprt_small' xalign 0.5
            if persistent.sprt_saved_filters:
                label "Saved\nFilters:" text_size sprt.SMALL_TEXT:
                    text_text_align 0.5 text_align (0.5, 0.5) right_padding 8
            for f in sorted(persistent.sprt_saved_filters):
                textbutton f:
                    style_prefix 'sprt_pick'
                    selected sprt.search.strip() != f
                    selected_hover_foreground None
                    action If(sprt.search == f,
                        RemoveFromSet(persistent.sprt_saved_filters, f),
                        SetField(sprt, 'search', f))
        ## Add a divider
        add Transform("#fff2", ysize=max(1, config.screen_height//300), yalign=1.0)
        ## Viewport with all the attributes
        viewport:
            style_prefix 'attr_vp'
            mousewheel True scrollbars "vertical"
            yinitial 0.0
            has vbox
            hbox:
                for attr in sprt.get_possible_attributes(persistent.sprt_who,
                        sprt.search):
                    textbutton attr:
                        sensitive attr not in sprt.what
                        action Function(sprt.add_attribute, attr)
            if persistent.sprt_who and list(filter(lambda x : (sprt.has_adjusted_attr(
                        persistent.sprt_who, x)
                    and (not sprt.search or sprt.search in x)
                    and not sprt.swap_attr),
                    persistent.sprt_shortforms)):
                hbox:
                    text "Short forms:"
                    for attr in sorted(filter(lambda x : (sprt.has_adjusted_attr(
                                    persistent.sprt_who, x)
                                and (not sprt.search or sprt.search in x)),
                            persistent.sprt_shortforms)):
                        textbutton attr:
                            action Function(sprt.add_attribute, attr, True)
            null height 100

## Screen with the text input-based input
screen image_attribute_tool_page2():
    tag menu
    predict False
    ## Includes the text-based input
    default sprt_what_input = SpecialInputValue(store.sprt, 'what')

    use image_attribute_tool_common():
        style_prefix 'sprt_enter'
        label "Enter expression:"
        hbox:
            style 'sprt_small_hbox' xalign 0.5
            button:
                key_events True style_prefix 'sprt_input'
                xsize sprt.SPACER*10
                action sprt_what_input.Toggle()
                input value sprt_what_input allow sprt.INPUT_ALLOW
            textbutton "Clear":
                action SetField(sprt, "what", "")
            null height sprt.SPACER*3

## Screen with the text input-based input
screen image_attribute_tool_page3():
    tag menu
    predict False
    ## Includes the text-based input
    default sprt_short_input = SpecialInputValue(store.sprt, 'what',
        enter_callback=sprt.save_shortform, disable_on_enter=False)

    use image_attribute_tool_common():
        style_prefix 'sprt_enter'
        label "Enter short form:"
        hbox:
            style 'sprt_small_hbox' xalign 0.5
            button:
                key_events True style_prefix 'sprt_input'
                xsize sprt.SPACER*10
                action sprt_short_input.Toggle()
                input value sprt_short_input allow sprt.INPUT_ALLOW
            textbutton "Clear":
                action SetField(sprt, "what", "")
            null height sprt.SPACER*3
        # Add a divider
        add Transform("#fff2", ysize=max(1, config.screen_height//300), yalign=1.0)

        textbutton "Clear All Short Forms":
            style_prefix 'sprt_enter'
            action Confirm("Are you sure you want to remove all\nthe short forms you've added?",
                SetField(persistent, "sprt_shortforms", set()),
                Hide("confirm"))
        viewport:
            style_prefix 'attr_vp'
            mousewheel True scrollbars "vertical"
            yinitial 0.0
            has hbox
            for attr in sorted(persistent.sprt_shortforms):
                textbutton attr:
                    if not sprt.has_adjusted_attr(persistent.sprt_who, attr):
                        ## Grey it out a bit
                        background sprt.construct_frame(sprt.GRAY, "#0000", sprt.PADDING)
                        action NullAction()
                        text_hover_color sprt.RED
                        selected False
                    action SetField(sprt, "what", attr)
                    alternate RemoveFromSet(persistent.sprt_shortforms, attr)
            null height 100

    ## Since enter doesn't disable this input, use ESC instead
    key 'K_ESCAPE' action DisableAllInputValues()

## Has the side menu, tag input, the image, and zoom tools
screen image_attribute_tool_common():

    ## The input values for the character name and attributes
    default sprt_who_input = SpecialInputValue(persistent, 'sprt_who',
        enter_callback=sprt.save_xyinitial)

    add sprt.GRAY

    use sprt_viewport() id "sprt_viewport"

    hbox:
        style_prefix 'sprt_copy'
        textbutton "Copy\nAll" sensitive sprt.what:
            action Function(sprt.copy_image_to_clipboard, True)
        textbutton "Copy\nAttrs" sensitive sprt.what:
            action Function(sprt.copy_image_to_clipboard, False)

    drag:
        id 'text_attr_drag'
        draggable True drag_handle (0, 0, 1.0, sprt.SPACER*2)
        dragged sprt.record_sprt_drag_pos
        xpos persistent.sprt_text_xpos
        ypos persistent.sprt_text_ypos
        frame:
            style_prefix 'sprt_drag'
            has vbox
            frame:
                style 'sprt_drag_label'
                text "(Drag to\nmove)" size int(sprt.SMALL_TEXT*0.65) text_align 1.0
                hbox:
                    textbutton "Button Input":
                        action ShowMenu("image_attribute_tool",
                            _transition=Dissolve(0.0))
                    textbutton "Text Input":
                        action ShowMenu("image_attribute_tool_page2",
                            _transition=Dissolve(0.0))
                    textbutton "Short Forms":
                        action ShowMenu("image_attribute_tool_page3",
                            _transition=Dissolve(0.0))
            transclude

    ## Dim the background behind the input button when it's active
    if renpy.get_editable_input_value() == (sprt_who_input, True):
        add sprt.GRAY alpha 0.7
        dismiss action sprt_who_input.Disable()

    ## The tag input
    frame:
        style_prefix 'sprt_small'
        xpos sprt.MENU_SIZE+sprt.SPACER*2
        has hbox
        textbutton "Tag:" action CaptureFocus("tag_drop")

        button:
            style_prefix 'sprt_input'
            key_events True
            selected renpy.get_editable_input_value() == (sprt_who_input, True)
            action [sprt_who_input.Toggle(),
                Function(sprt.save_xyinitial),
                ## Ensure we don't have attribute conflicts
                If(not sprt_who_input.editable,
                [SetField(sprt, "what", ""),
                SetField(sprt, "swap_attr", "")])]
            input value sprt_who_input allow sprt.INPUT_ALLOW

        textbutton "Clear":
            sensitive persistent.sprt_who
            action [SetField(persistent, "sprt_who", ""),
                    ## Also clear the attributes associated with them
                    SetField(sprt, "what", ""),
                    Function(sprt.save_xyinitial),
                    SetField(sprt, "swap_attr", "")]
        textbutton "Save":
            sensitive (persistent.sprt_who
                and persistent.sprt_who not in persistent.sprt_tags)
            action [AddToSet(persistent.sprt_tags, persistent.sprt_who),
                Function(sprt.save_xyinitial),
                Notify("Saved!")]

    if GetFocusRect("tag_drop"):
        add sprt.GRAY alpha 0.7
        dismiss action ClearFocus("tag_drop")
        nearrect:
            focus "tag_drop"
            frame:
                modal True style_prefix 'sprt_drop'
                has vbox
                for tg in sorted(persistent.sprt_tags):
                    hbox:
                        textbutton tg:
                            yalign 0.5 text_yalign 0.5
                            action [SetField(sprt, "what", ""),
                                SetField(sprt, "swap_attr", ""),
                                Function(sprt.save_xyinitial),
                                Function(sprt.retrieve_xyinitial, tg),
                                SetField(persistent, "sprt_who", tg),
                                ClearFocus("tag_drop")]
                        textbutton "(Remove)" size_group None:
                            background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
                            hover_background sprt.construct_frame(sprt.MAROON, sprt.RED, sprt.PADDING)
                            action [RemoveFromSet(persistent.sprt_tags, tg)]

    use hamburger_menu():
        style_prefix 'hamburger'
        textbutton _("Return") action Return()
        textbutton "How to Use" action ShowMenu("sprt_tutorial1")

################################################################################
## STYLES
################################################################################
## Note that these are also coded in a fairly specific way in order to adapt
## to various projects. It borrows heavily from default styling without relying
## on any images so the tool can be as lightweight as possible.
style sprt_enter_label:
    background None xalign 0.5
style sprt_enter_label_text:
    is sprt_text
    size sprt.BIG_TEXT
style sprt_enter_button:
    is sprt_small_button
style sprt_enter_button_text:
    is sprt_small_button_text

style sprt_pick_hbox:
    xalign 0.5 spacing sprt.PADDING*2 box_wrap_spacing sprt.PADDING*2
    box_wrap True
style sprt_label_text:
    is sprt_text
    size sprt.BIG_TEXT
style sprt_pick_button:
    background sprt.construct_frame(sprt.ORANGE, "#0000", sprt.PADDING)
    hover_background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
    hover_foreground Text("X", color=sprt.RED, bold=True, align=(0.5, 0.5),
        font="DejaVuSans.ttf", size=sprt.MED_TEXT)
    selected_background sprt.construct_frame(sprt.YELLOW, "#000d", sprt.PADDING)
    selected_hover_background sprt.construct_frame(sprt.YELLOW, "#000d", width=2)
    selected_hover_foreground Text("X", color=sprt.YELLOW,
        bold=True, align=(0.5, 0.5), font="DejaVuSans.ttf", size=sprt.MED_TEXT)
    padding (sprt.PADDING*2, sprt.PADDING*2)
style sprt_pick_button_text:
    is sprt_text
    hover_color sprt.RED
    selected_hover_color Color(sprt.YELLOW).replace_opacity(0.4)
    selected_color Color(sprt.YELLOW).replace_lightness(0.85)

style attr_vp_viewport:
    xsize int(config.screen_width/2.2)-sprt.PADDING*2*6
style attr_vp_hbox:
    xmaximum int(config.screen_width/2.2)-sprt.PADDING*2*12 box_wrap True
    spacing sprt.PADDING*2 box_wrap_spacing sprt.PADDING*2
style attr_vp_button:
    is sprt_pick_button
    insensitive_background sprt.construct_frame(sprt.GRAY, "#0000", sprt.PADDING)
    background sprt.construct_frame(sprt.BLUE, "#fff2", sprt.PADDING)
    hover_background sprt.construct_frame(sprt.BLUE, "#fff2", sprt.PADDING)
    selected_background sprt.construct_frame(sprt.BLUE, "#fff2", sprt.PADDING)
    selected_hover_background sprt.construct_frame(sprt.BLUE, "#fff2", sprt.PADDING)
    foreground None selected_foreground None hover_foreground None
    selected_hover_foreground None
style attr_vp_button_text:
    is sprt_pick_button_text
    hover_color sprt.YELLOW
    insensitive_color "#fff5"
style attr_vp_vscrollbar:
    base_bar sprt.MAROON
    thumb sprt.RED xsize sprt.PADDING*3
    unscrollable "hide"
style attr_vp_text:
    is sprt_text
    yalign 0.5

################################################################################
## TUTORIAL
################################################################################
## Note that this is coded in a pretty specific way due to the flexibility
## of the tool. It's not meant to be a good example of how to code a screen,
## in particular due to the repeated code. Normally it would be easier to
## have images showing highlighted areas of the screen, which isn't possible
## here due to how the tool adapts to different projects + I didn't want to
## include unnecessary images in the tool.
################################################################################
init -30 python in sprt:
    ## A special way of declaring the tutorial text in order to make it easy
    ## to add or remove text without having to change the code.
    tut1 = Tutorial(
        TutorialText("intro", "Welcome to the Image Attributes Tool!",
        "This tool has many features to help you test and debug image attributes, particularly for character sprites.",
        "This tutorial will show you how to use the tool.",
        xalign=0.5),
        TutorialText("tag1", "Entering an Image Tag",
        "The first thing you need to do is type an image tag in the input box beside the \"Tag\" button.",
        "(This is just a tutorial so you can't type anything here, now!)",
        "This can be be any image tag, but it's usually a character name like \"eileen\", or sometimes a multi-word tag like \"side mc\" or \"bg\" for backgrounds.",
        "The \"Clear\" button will remove all text in the tag field.",
        xalign=1.0),
        TutorialText("tag2", "Saving an Image Tag",
        "You can also save tags to quickly access later with the \"Save\" button.",
        "Tags that you've saved can be accessed by clicking the \"Tag\" text to the left of the input box.",
        "This will show a dropdown of all the tags you've saved. Click \"(Remove)\" to remove a saved tag from this list, or click the tag itself to switch to it.",
        "Clicking on a tag or anywhere outside of the dropdown will close the dropdown.",
        xalign=1.0),
        TutorialText("moving_img", "Moving the Image",
        "After entering an image tag, you can move the image around by clicking and dragging it.",
        "If you can't find your image, use the \"Re-center\" button to center it.",
        "If the game can't find your image, you'll see a big red square with some text on it.",
        xalign=1.0),
        TutorialText("moving_img2", "Moving the Image 2",
        "The slider in the bottom left lets you zoom the image in and out so you can better see outfit or expression changes. You can also use the mouse wheel to zoom in and out (so long as you're not hovering over the viewport on the right).",
        "You can see the text printout of all the current attributes being applied to the image just above the zoom bar.",
        xalign=1.0),
        TutorialText("adjusting_attr", "Adjusting Attributes",
        "Once you've entered an image tag, you can adjust the attributes of the image.",
        "There are two main ways to do so: the first, by choosing from a list of buttons, and the second by typing them in directly.",
        "These tabs at the top let you switch between the two input methods.",
        "We'll look at the \"Button Input\" tab first."),
        TutorialText("choosing_attr", "Choosing Attributes",
        "After entering an image tag, you will see a list of the possible attributes for that image in the viewport on the right.",
        "You can click on any of these attributes to add them to the image.",
        "You can also drag the coloured bar at the top to move this UI element around so it's not in the way of your image."),
        TutorialText("choosing_attr2", "Choosing Attributes 2",
        "When you click on an attribute, other attributes may disappear from the list. This is because some attributes are mutually exclusive - for example, many layered images are set up with a group for \"mouths\", so mouth attributes will replace each other.",
        "Obviously, you wouldn't want a character to have more than one mouth displayed at once!",
        "Since you can't have two mouths, once you've selected a mouth attribute from the list, other mouth attributes will be removed from the list."),
        TutorialText("filters", "Filters",
        "You can also filter attributes to make them easier to find.",
        "This is especially useful if you use a consistent naming scheme, like \"_mouth\" for all your mouth attributes.",
        "Simply click the input field next to \"Filter\" and type in the text you want to use to filter the results."),
        TutorialText("filters2", "Filters 2",
        "You can also save filters for later use by clicking the \"Save Current Filter\" button.",
        "Click on any of your saved filters to apply them to the list. If a filter is already active, clicking it will remove it from the saved filters list.",
        "You can also use the \"Clear Saved Filters\" button to remove all the saved filters at once."),
        TutorialText("current_attr", "Current Attributes",
        "Once you've picked some attributes to apply to your image, you will see them displayed at the top of the screen.", "{b}Left{/b}-clicking an attribute will remove it from the image.",
        "The attribute \"work_outfit\" shows what the attribute will look like when you hover over it to indicate it will be removed if you click on it.",
        "You can also click \"Clear\" at the top to remove all attributes at once.",
        "This won't remove the image tag you entered earlier."),
        TutorialText("swapping_attr", "Swapping Attributes",
        "You can also {b}right{/b}-click an attribute to mark it as \"swappable\".", "This means that any attributes you select from the list below will replace the swappable attribute.", "Only one attribute can be marked as swappable at a time.", "If an attribute is marked as swappable, it will be highlighted in yellow.", "You can right- or left-click the attribute again to cancel the swappable property."),
        TutorialText("swapping_attr2", "Swapping Attributes 2",
        "When an attribute is marked as swappable, {b}only attributes that conflict with the swappable attribute will be shown{/b}.", "What this means is that if you have layered image groups for things like eyes, mouths, or eyebrows, right-clicking an \"eye\" attribute will only show other eye attributes in the list below.", "This makes it very useful for quickly swapping out expression parts.", "So, for the example on the right, if you clicked the \"swimsuit\" attribute, it would replace the \"work_outfit\" attribute, since the \"work_outfit\" attribute is marked as swappable."),
        TutorialText("adjusting_attr2", "Adjusting Attributes pt 2",
        "Next, we'll look at the \"Text Input\" tab.",
        "You can switch tabs by clicking on them at the top of the window."),
        TutorialText("typing_attr", "Typing Attributes",
        "Here, you can click on the input box below \"Enter attributes\" to freely type in a space-separated attributes.",
        "This can be particularly useful if you're using {b}config.adjust_attributes{/b} to make short forms for your attributes.",
        "You can use the \"Clear\" button to clear all text from the input box as well to start over.",
        "It can also be helpful if the attribute filters on the other tab are getting in the way of what you're trying to do."),
        TutorialText("shortform1", "Short Forms",
        "The last tab is the Short Forms tab. This tab is meant to be used in combination with {b}config.adjust_attributes{/b}, which allows you to show an image like \"show eileen happy\" and Ren'Py will translate that into \"show eileen happy_eyes happy_mouth\".",
        "If you're using those sorts of short forms, you can type them into the input box on this page so they can be used with the image tools.",
        "To make it easy to type several short forms in a row, hitting Enter will save the short form and clear the input box so you can type another one. You can hit ESC to disable the input box when you're done.",
        ),
        TutorialText("shortform2", "Short Forms 2",
        "To quickly apply a short form to your image, {b}left-{/b}click on it in the list below. To remove a short form from your list, {b}right-{/b}click it instead.",
        "You can also remove all short forms at once with the \"Clear All Short Forms\" button.",
        "You can only apply a short form to the current image tag if it is valid - that is, the short form must provide a different set of attributes when it is put through the {b}config.adjust_attributes{/b} function.",
        "Not every short form has to be valid for all image tags, however.",
        ),
        TutorialText("shortform3", "Short Forms 3",
        "To make it easier to add short forms to the tool, there is a set at the top of {b}image_tool_common.rpy{/b} where you can type out all your short forms. {b}You will need to Delete Persistent from the launcher to see the short forms applied initially,{/b} and then you can modify or add to it however you like.",
        "Note that your modifications will be reset if you ever Delete Persistent again, however.",
        ),
        TutorialText("shortform4", "Short Forms 4",
        "If you've added short forms, you will be able to see any applicable short forms for the current image tag listed at the bottom of the attributes button on the \"Button Input\" tab.",
        "Click these buttons to apply them to your image. Note, however, that they are not compatible with the Swap Attribute system, and it is your responsibility to manage conflicting attributes.",
        ),
        TutorialText("copy_attr", "Copying Attributes",
        "Lastly, there are two ways of copying attributes to make it easy to paste them into your script.",
        "The first is the \"Copy All\" button, which will copy {b}both{/b} the image tag {b}and{/b} the currently applied attributes to the clipboard.",
        "This makes it most suitable for use with the {b}show{/b} statement."),
        TutorialText("copy_attr2", "Copying Attributes 2",
        "So, if your character tag is \"eileen\", and you've applied the attributes \"happy_eyes\" and \"happy_mouth\" to her, \"Copy All\" will copy the text {b}show eileen happy_eyes happy_mouth{/b} to your clipboard.",
        "You can then paste that into your script wherever you like."),
        TutorialText("copy_attr3", "Copying Attributes 3",
        "The second is the \"Copy Attrs\" button, which will only copy the currently applied attributes and NOT the image tag.",
        "This makes it most suitable for side images or attributes applied during dialogue, like {b}e happy_eyes \"Some happy dialogue.\"{/b}.",
        "So, if your character tag is \"eileen\" and you've applied the attributes \"happy_eyes\" and \"happy_mouth\" to her, \"Copy Attrs\" will copy the text {b}happy_eyes happy_mouth{/b} to your clipboard.", "You can then paste that into your script wherever you like."),
        TutorialText("conclusion", "Conclusion",
        "And that's everything! I hope this helped you learn how to use the Image Attributes Tool, and that it helps you during development.",
        "To view this tutorial again, click the three lines in the top left corner and select \"How to Use\".",
        "If you run into any problems or have questions, feel free to leave a comment on itch.io.",
        "You can find more of my Ren'Py tools at {a=https://feniksdev.itch.io/}feniksdev.itch.io{/a}.",
        xalign=0.5)
    )

screen sprt_tutorial1():
    tag menu
    on 'show' action SetField(persistent, 'sprt_tutorial1_shown', True)
    on 'replace' action SetField(persistent, 'sprt_tutorial1_shown', True)

    default step = 0

    add sprt.GRAY

    add Placeholder() xcenter 0.25 yanchor 0.6 ypos 1.0 zoom 1.5 matrixcolor BrightnessMatrix(0.3)
    use sprt_viewport(demonstration=True) id "sprt_viewport"

    if sprt.tut1.after_id("moving_img2", step):
        add sprt.GRAY alpha 0.9

    hbox:
        style_prefix 'sprt_copy'
        textbutton "Copy\nAll" action NullAction():
            if not sprt.tut1.between_ids("copy_attr", "copy_attr3", step):
                foreground "#0008"
        textbutton "Copy\nAttrs" action NullAction():
            if not sprt.tut1.between_ids("copy_attr", "copy_attr3", step):
                foreground "#0008"

    frame:
        xpos config.screen_width-int(config.screen_width/2.2)
        ypos sprt.SPACER*3 anchor (0.0 , 0.0)
        style_prefix 'sprt_drag'
        if (sprt.tut1.between_ids("moving_img", "moving_img2", step)
                or sprt.tut1.after_id("shortform4", step)):
            foreground "#000c"
        has vbox
        frame:
            style 'sprt_drag_label'
            text "(Drag to\nmove)" size int(sprt.SMALL_TEXT*0.65) text_align 1.0
            hbox:
                textbutton "Button Input" action NullAction():
                    selected (sprt.tut1.between_ids("adjusting_attr", "swapping_attr2", step)
                        or sprt.tut1.tut(step).id == "shortform4")
                textbutton "Text Input" action NullAction():
                    selected sprt.tut1.between_ids("adjusting_attr2", "typing_attr", step)
                textbutton "Short Forms" action NullAction():
                    selected sprt.tut1.between_ids("shortform1", "shortform3", step)

        if sprt.tut1.between_ids("adjusting_attr2", "typing_attr", step):
            label "Enter expression:" style 'sprt_enter_label'
            hbox:
                style_prefix 'sprt_enter'
                style 'sprt_small_hbox' xalign 0.5
                button:
                    style_prefix 'sprt_input'
                    xsize sprt.SPACER*10
                    action NullAction()
                    text "sad_eyes arm_up" style 'sprt_input_input'
                textbutton "Clear" action NullAction()
                null height sprt.SPACER*3
        elif sprt.tut1.between_ids("shortform1", "shortform3", step):
            label "Enter short form:" style_prefix 'sprt_enter'
            hbox:
                style_prefix 'sprt_enter'
                style 'sprt_small_hbox' xalign 0.5
                button:
                    key_events True style_prefix 'sprt_input'
                    xsize sprt.SPACER*10 action NullAction()
                    text "happy" style 'sprt_input_input'
                textbutton "Clear" action NullAction()
                null height sprt.SPACER*3
            # Add a divider
            add Transform("#fff2", ysize=max(1, config.screen_height//300), yalign=1.0)
            textbutton "Clear All Short Forms":
                style_prefix 'sprt_enter'
                action NullAction()
            viewport:
                style_prefix 'attr_vp'
                mousewheel True scrollbars "vertical"
                yinitial 0.0
                has hbox
                for attr in ("angry", "embarrassed", "happy", "normal", "sad", "surprised"):
                    textbutton attr:
                        if attr == "embarrassed":
                            ## Grey it out a bit
                            background sprt.construct_frame(sprt.GRAY, "#0000", sprt.PADDING)
                            action NullAction()
                            text_hover_color sprt.RED
                            selected False
                        action NullAction()
                null height 100
        else:
            frame:
                style 'sprt_temp_tut_frame'
                if not sprt.tut1.between_ids("current_attr", "swapping_attr2", step):
                    foreground "#000b"
                has hbox
                style_prefix 'sprt_pick'
                label "Current Attributes" style 'sprt_label'
                textbutton "Clear":
                    style 'sprt_small_button'
                    action NullAction()
            frame:
                style 'sprt_temp_tut_frame'
                if not sprt.tut1.between_ids("current_attr", "swapping_attr2", step):
                    foreground "#000b"
                has hbox
                style_prefix 'sprt_pick'
                for attr in ("front", "happy_mouth", "work_outfit",):
                    textbutton attr:
                        if (sprt.tut1.tut(step).id == "current_attr"
                                and attr == "work_outfit"):
                            background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
                            foreground Text("X", color=sprt.RED, bold=True, align=(0.5, 0.5),
                                font="DejaVuSans.ttf", size=sprt.MED_TEXT)
                        elif (sprt.tut1.tut(step).id in ("swapping_attr", "swapping_attr2")
                                and attr == "work_outfit"):
                            selected True
                        action NullAction()

            frame:
                style 'sprt_temp_tut_frame'
                if not sprt.tut1.between_ids("filters", "filters", step):
                    foreground "#000b"
                has hbox
                spacing sprt.PADDING*2 xmaximum int(config.screen_width/2.2)-150
                style_prefix 'sprt_small' xalign 0.5
                ## Workaround for the code plugin parser
                label "{}".format("Filter:") yalign 0.5
                button:
                    style_prefix 'sprt_input'
                    action NullAction()
                    text "eyes" style 'sprt_input_input'
                textbutton "Clear" action NullAction()

            frame:
                style 'sprt_temp_tut_frame'
                if not sprt.tut1.between_ids("filters", "filters2", step):
                    foreground "#000b"
                has hbox
                style_prefix 'sprt_small' xalign 0.5
                textbutton "Save Current Filter" action NullAction():
                    if sprt.tut1.tut(step).id != "filters2":
                        foreground "#000b"
                textbutton "Clear Saved Filters" action NullAction():
                    if sprt.tut1.tut(step).id != "filters2":
                        foreground "#000b"

            frame:
                style 'sprt_temp_tut_frame'
                if not sprt.tut1.between_ids("filters", "filters2", step):
                    foreground "#000b"
                has hbox
                box_wrap True spacing sprt.PADDING*2 box_wrap_spacing sprt.PADDING*2
                style_prefix 'sprt_small' xalign 0.5
                if persistent.sprt_saved_filters:
                    label "Saved\nFilters:" text_size sprt.SMALL_TEXT:
                        text_text_align 0.5 text_align (0.5, 0.5) right_padding 8
                for f in ("eyes", "mouths"):
                    textbutton f:
                        style_prefix 'sprt_pick'
                        selected f == "eyes"
                        selected_hover_foreground None
                        action NullAction()

            # Add a divider
            add Transform("#fff2", ysize=max(1, config.screen_height//300), yalign=1.0)

            viewport:
                style_prefix 'attr_vp'
                mousewheel True scrollbars "vertical"
                yinitial 0.0
                has vbox
                hbox:
                    if (sprt.tut1.tut(step).id in ("swapping_attr", "swapping_attr2")
                                and attr == "work_outfit"):
                        for attr in ("pajamas", "swimsuit", "work_outfit"):
                            textbutton attr action NullAction():
                                sensitive attr != "work_outfit"
                    else:
                        for attr in ("angry_eyes", "happy_eyes", "normal_eyes", "sad_eyes",):
                            textbutton attr action NullAction()
                if sprt.tut1.tut(step).id == "shortform4":
                    hbox:
                        text "Short forms:"
                        for attr in ("angry", "happy", "normal", "sad", "surprised"):
                            textbutton attr action NullAction()
                null height 100


    if (sprt.tut1.before_id("moving_img", step)):
        add sprt.GRAY alpha 0.9

    ## The tag input
    frame:
        style_prefix 'sprt_small'
        xpos sprt.MENU_SIZE+sprt.SPACER*2
        if not sprt.tut1.between_ids("tag1", "tag2", step):
            foreground "#0008"
        has hbox
        textbutton "Tag:" action NullAction():
            if sprt.tut1.tut(step).id not in ("tag2",):
                foreground "#0008"

        button:
            style_prefix 'sprt_input'
            action NullAction()
            if sprt.tut1.tut(step).id != "tag1":
                foreground "#0008"
            text "eileen" style 'sprt_input_input'

        textbutton "Clear" action NullAction():
            if sprt.tut1.tut(step).id != "tag1":
                foreground "#0008"
        textbutton "Save" action NullAction():
            if sprt.tut1.tut(step).id != "tag2":
                foreground "#0008"

    if sprt.tut1.tut(step).id in ("tag2",):
        frame:
            modal True style_prefix 'sprt_drop'
            xpos sprt.MENU_SIZE+sprt.SPACER*2
            ypos sprt.MENU_SIZE+sprt.SPACER*2
            has vbox
            for tg in ("ashwin", "side mc", "xia", "zoran"):
                hbox:
                    textbutton tg:
                        yalign 0.5 text_yalign 0.5
                        action NullAction()
                    textbutton "(Remove)" size_group None:
                        background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
                        hover_background sprt.construct_frame(sprt.MAROON, sprt.RED, sprt.PADDING)
                        action NullAction()

    if sprt.tut1.tut(step).id in ("intro", "conclusion"):
        use hamburger_menu()

    if sprt.tut1.tut(step).id == "intro":
        add sprt.GRAY alpha 0.9

    use sprt_tutorial_text(sprt.tut1, step, "image_attribute_tool")

################################################################################
## Code to remove these files for a distributed game. Do not remove.
init python:
    build.classify("**image_attributes_tool.rpy", None)
    build.classify("**image_attributes_tool.rpyc", None)
################################################################################
