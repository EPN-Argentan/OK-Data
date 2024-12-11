################################################################################
##
## Image Tools by Feniks (feniksdev.itch.io / feniksdev.com) v1.5
##
################################################################################
## This file contains common code for three main image tools:
## 1) A text-base image attribute tool
## 2) A layered image visualizer
## 3) An image tint tool
##
## It is required for the other tools to work.
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
## Then you can select a tool and get started. You will be shown the tutorial
## the first time you use a tool.
## Leave a comment on the tool page on itch.io if you run into any issues!
################################################################################
## CONFIGURATION
################################################################################
init -100 python in sprt:
    ## FOR YOU: Add your short forms here so they aren't reset when you delete
    ## persistent. Only applies to the persistent short forms when it's empty
    ## i.e. the first time you run the tool or after deleting persistent.
    SHORT_FORMS = {"happy",}
    ## An example might look like:
    # SHORT_FORMS = {"happy", "sad", "worried", "embarrassed", "angry",
    #     "confused", "normal", "nervous", "annoyed", "shocked"}

## Colors used throughout the UI; feel free to change these to suit your
## own needs
define sprt.RED = "#f93c3e"
define sprt.ORANGE = "#ff8335"
define sprt.DARK_ORANGE = "#ca5f1c"
define sprt.DARKER_ORANGE = "#b3410d"
define sprt.BLUE = "#292835"
define sprt.GRAY = "#21212d"
define sprt.CREAM = "#f7f7ed"
define sprt.WHITE = "#fff"
define sprt.YELLOW = "#E5BA54"
define sprt.MAROON = "#572D35"
define sprt.PINK = "#ff3a6a"

## Text sizes used throughout the UI; feel free to change these to suit
## your project better.
define sprt.BIG_TEXT = int(gui.text_size*1.4)
define sprt.MED_TEXT = gui.text_size
define sprt.SMALL_TEXT = int(gui.text_size*0.8)

## Everything beyond this point is not meant to be edited by the user, but
## you're welcome to read it for learning purposes.
################################################################################
## VARIABLES
################################################################################
## Persistent ##################################################################
################################################################################
## The image tag
default persistent.sprt_who = ""
## The image zoom
default persistent.sprt_zoom = 2.0
default persistent.sprt_zoom_dict = dict()
## Remember the image's position in the viewport
default persistent.sprt_yinitial = dict()
default persistent.sprt_xinitial = dict()

## Remembers character tags you've entered
default persistent.sprt_tags = []

## The default attributes of a layered image group
default persistent.sprt_default_attributes = dict()

## Short forms the system can use
default persistent.sprt_shortforms = sprt.SHORT_FORMS

## Normal ######################################################################
################################################################################
## The image attributes
default sprt.what = ""

## Values to remember the position of the image in the viewport.
## A small update in order to not have inertia for this viewport, even
## if the program includes it elsewhere.
define 2 sprt.xadj = NoInertiaAdjustment(range=1.0, value=0.5)
define 2 sprt.yadj = NoInertiaAdjustment(range=1.0, value=0.5)

## Saves the last valid image so it's not flipping between "NOT FOUND"
## when you're typing out attributes
default sprt.last_valid_image = None
## The attribute to swap out for a newly clicked attribute
default sprt.swap_attr = ""

################################################################################
## CONSTANTS
################################################################################
## Some spacing and sizing constants relative to the screen size
define sprt.SPACER = max(
    int(config.screen_width//50),
    int(config.screen_height//50)
)
define sprt.XSPACER = int(config.screen_width//50)
define sprt.YSPACER = int(sprt.XSPACER*config.screen_height/float(config.screen_width))
define sprt.PADDING = max(int(config.screen_width//384), 1)
define sprt.MENU_SIZE = config.screen_height//20

## What you can type into the boxes
define sprt.INPUT_ALLOW = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _-0123456789./"

################################################################################
## IMAGES
################################################################################
## The image shown if a image cannot be found with the current attributes
## or any saved valid attributes.
image image_not_found = Text("Click the button in the top left corner and\nselect How to Use to learn how to use the tool!",
        size=120, color=sprt.WHITE, outlines=[(6, "#000")],
        align=(0.5, 0.5), text_align=0.5, xmaximum=config.screen_width-100)

################################################################################
## FUNCTIONS
################################################################################
init -90 python in sprt:

    from renpy.store import sprt, Solid, HBox, Transform, VBox, Frame, Window
    from renpy.store import persistent, config, DictValue

    def above_version(ver):
        """
        Return True if the provided version is the same or lower than the
        current version.
        """
        cur = renpy.version(tuple=True)
        if cur[0] == 7 and cur[1] >= 5 and ver[0] > 7:
            ## Convert from 8.1 to 7.6 / 8.0 to 7.5 etc
            cur = (8, cur[1]-5, cur[2])
        elif cur[0] == 7:
            ## 7.4 or earlier
            return cur >= ver
        if ver[0] == 7:
            ## Convert to the 8.0+ format
            ver = (8, ver[1]-5, ver[2])
        return cur >= ver

    def save_xyinitial():
        """
        Save the last value/range of the viewport, so it can be set up to
        that position the next time it is used. Saved per-image tag.
        """
        global persistent
        t_xadj = getattr(sprt, 'xadj', None)
        if t_xadj is None:
            return
        t_yadj = getattr(sprt, 'yadj', None)
        if t_yadj is None:
            return

        persistent.sprt_yinitial[persistent.sprt_who] = t_yadj.value/float(t_yadj.range or 1.0)
        persistent.sprt_xinitial[persistent.sprt_who] = t_xadj.value/float(t_xadj.range or 1.0)

        # Make sure this is saved before the game quits
        renpy.save_persistent()

    def retrieve_xyinitial(who=None):
        """
        Grab the last position of the viewport for the current image tag,
        if it exists.
        """
        global persistent, xadj, yadj
        if who is None:
            who = persistent.sprt_who
        xadj.value = persistent.sprt_xinitial.get(who, 0.5)*xadj.range
        yadj.value = persistent.sprt_yinitial.get(who, 0.5)*yadj.range

    if config.developer:
        ## Don't bother to save the coordinates for a dev tool if
        ## not in development
        config.quit_callbacks.append(save_xyinitial)

    def get_image(who, save_last_image=False):
        """
        Get an image to show based on the provided tag and attributes. If
        an image with the provided attributes does not exist, returns
        the image_not_found image.
        """
        global what, last_valid_image

        if not who:
            return "image_not_found"

        tag, attrs = get_tag_attrs(who, what)
        attrs = ' '.join(attrs)
        img = "{} {}".format(tag, attrs).strip()

        result = renpy.can_show(img)

        if result is not None:
            if save_last_image:
                last_valid_image = ' '.join(result)
            return ' '.join(result)

        if last_valid_image is not None:
            return last_valid_image
        return "image_not_found"

    def get_tag_attrs(who, what, adjust=True, filter_swap=False):
        """
        Turn the string with the character tag and list of attributes into
        a string with the tag and a tuple with the attributes.

        Parameters:
        -----------
        who : string
            The image tag and optionally some attributes, separated by spaces.
        what : string
            Attributes for the image tag, separated by spaces.
        adjust : bool
            If True, config.adjust_attributes will be applied to the results.
        filter_swap : bool
            If True, a swap attribute is present. This is used to filter
            the possible attributes that can be applied to the image.
        """
        global swap_attr

        who = who.strip()
        who_split = who.split(' ')
        tag = who_split[0]

        adjust_fn = (config.adjust_attributes.get(tag, None)
            or config.adjust_attributes.get(None, None))

        if len(who_split) > 1:
            attrs = tuple(who_split[1:])
            if what:
                what = tuple(what.split(' '))
                attrs += what
        elif what:
            attrs = tuple(what.split(' '))
        else:
            attrs = tuple()

        # Remove the dev swap attribute, if applicable
        if filter_swap and swap_attr:
            attrs = tuple(filter(lambda x: x != swap_attr, attrs))

        if adjust_fn and attrs and adjust:
            attrs = adjust_fn((tag,) + attrs)
            # Strip off the tag
            attrs = attrs[1:]
        return tag, attrs

    def has_adjusted_attr(who, what):
        """
        Confirms if the provided attributes change when fed into
        config.adjust_attributes, and returns True if so.
        """

        original = who.strip() + ' ' + what.strip()
        ret = transform_attr(who, what)
        return original != ret

    def transform_attr(who, what):
        """
        Transforms the provided attributes using config.adjust_attributes.
        """
        tag = who.split(' ')[0].strip()
        adjust_fn = (config.adjust_attributes.get(tag, None)
            or config.adjust_attributes.get(None, None))

        ## No adjust function
        if adjust_fn is None:
            return who.strip() + ' ' + what.strip()

        original = who.strip() + ' ' + what.strip()
        original = tuple(original.split(' '))
        ret = adjust_fn(original)
        return ' '.join(ret)

    def reset_image_position():
        """Reset the image to the center of the screen."""
        global xadj, yadj
        xadj.set_value(int(xadj.range//2))
        yadj.set_value(int(yadj.range//2))

    from pygame import scrap

    def copy_to_clipboard(txt):
        scrap.put(scrap.SCRAP_TEXT, txt.encode("utf-8"))
        renpy.notify("Copied \"{}\" to clipboard.".format(txt))

    ############################################################################
    ## For styles
    def construct_frame(border_color, inside="#000d", width=5):
        """
        Returns a bordered frame without using image files.

        Parameters:
        -----------
        border_color : string
            The color of the border.
        inside : string
            The color of the inside of the frame.
        width : int
            The width of the border.
        """
        return Frame(HBox(Transform(border_color, xsize=width, ysize=10+width*2),
            VBox(Transform(border_color, ysize=width, xsize=10),
                Transform(inside, ysize=10, xsize=10),
                Transform(border_color, ysize=width, xsize=10)),
            Transform(border_color, xsize=width, ysize=10+width*2),
        ), width, width)

    def construct_checkbox(border_color, inside="#000d", width=5,
            box_size=(30, 30), checked=True):
        """
        Returns a checkbox without using image files.

        Parameters:
        -----------
        border_color : string
            The color of the border.
        inside : string
            The color of the inside of the frame.
        width : int
            The width of the border.
        box_size : tuple
            The size of the checkbox.
        checked : bool
            Whether the checkbox is checked or not.
        """
        inner_size = max(int(box_size[0]//3), 2), max(int(box_size[1]//3), 2)
        if checked:
            s = Transform(sprt.WHITE, align=(0.5, 0.5), xysize=inner_size)
        else:
            s = Transform("#0000", align=(0.5, 0.5), xysize=inner_size)
        return Window(
            s,
            background=construct_frame(border_color, inside, width),
            #xysize=(None, None),
            xysize=box_size,
            padding=(width, width),
            yalign=0.5, xalign=0.0, style='clear_window'
        )

################################################################################
## CLASSES
################################################################################
init python:
    ## Special Input ###########################################################
    ##
    ## This is a custom InputValue which does not begin as selected/ready for
    ## input and requires an action to be enabled. Pressing the Enter button
    ## will disable the input again.
    ##
    ## This makes it a good choice for most custom input screens, particularly
    ## on mobile devices where the keyboard can take up most of the screen space.
    ##
    ## Read more about InputValue here:
    ## https://www.renpy.org/doc/html/screen_python.html#inputvalue
    ##
    ## This version has a special callback for setting text and hitting enter,
    ## which allows it to check for valid input in some cases for the expression
    ## tester.
    ##
    class SpecialInputValue(FieldInputValue):
        """
        Subclass of InputValue which allows the Enter key to dismiss
        the input button. Does not begin as selected (so, on mobile the
        keyboard won't immediately appear). Also includes optional callbacks
        for set_text and enter.
        """

        def __init__(self, object, field, default=False, set_callback=None,
                enter_callback=None, starting_value=None,
                disable_on_enter=True, strip_on_close=True):
            self.object = object
            self.field = field

            self.default = default
            self.set_callback = set_callback
            self.enter_callback = enter_callback
            if starting_value is not None:
                self.set_text(starting_value)
            self.disable_on_enter = disable_on_enter
            self.strip_on_close = strip_on_close

        def set_text(self, s):
            super(SpecialInputValue, self).set_text(s)
            ## Perform a callback
            if self.set_callback is not None:
                self.set_callback(s)

        def strip_text(self):
            s = self.get_text()
            if s != s.strip():
                self.set_text(s.strip())

        def Disable(self):
            if self.strip_on_close:
                return [Function(self.strip_text), super(SpecialInputValue, self).Disable()]
            return super(SpecialInputValue, self).Disable()

        def enter(self):
            """Disable this input when the user presses Enter."""
            if self.disable_on_enter:
                renpy.run(self.Disable())
            elif self.strip_on_close:
                self.strip_text()
            ## Perform a callback
            if self.enter_callback:
                self.enter_callback()
            raise renpy.IgnoreEvent()


    class NoInertiaAdjustment(renpy.display.behavior.Adjustment):
        """A tiny wrapper around Adjustment that disables inertia."""
        def inertia(self, amplitude, time_constant, st):
            self.end_animation()

init -90 python in sprt:

    class SafeDictValue(DictValue):
        """
        A class which creates a dictionary entry if one does not already
        exist when adjusting it as a screen action.
        """
        def __init__(self, dict, key, range, max_is_zero=False, style='bar',
                offset=0, step=None, action=None, force_step=False,
                default_value=None):
            if dict.get(key, "DOESNOTEXIST") == "DOESNOTEXIST":
                dict[key] = default_value
            super(SafeDictValue, self).__init__(dict, key, range, max_is_zero,
                style, offset, step, action, force_step)

    class TutorialText():
        """
        A class that holds information to make it easier to display
        tutorial information for the image tools.

        Attributes:
        -----------
        id : string
            The id of the tutorial text. Used to identify this particular
            tutorial "step" (and non-numerical in case more steps are added
            or removed, or change order).
        title : string
            The title of the tutorial text.
        text : list
            A list of strings to display as the tutorial text.
        properties : dict
            A dictionary of style properties to apply to the tutorial text
            frame.
        """
        def __init__(self, id, title, *text, **properties):
            self.id = id
            self.title = title
            self.text = list(text)
            final_txt = properties.pop('final_txt', True)
            if id is None or final_txt is None:
                pass
            elif id != "conclusion":
                self.text.append("Click anywhere to continue.")
            else:
                self.text.append("Thanks for reading! Click again to close the tutorial.")
            self.properties = properties

    class Tutorial():
        """
        A class that holds information to make it easier to display
        tutorial information for the image tools.

        Attributes:
        -----------
        tutorials : tuple
            A tuple of TutorialText objects.
        length : int
            The length of the tutorials list.
        """
        def __init__(self, *tutorials):
            self.tutorials = tutorials
            self.length = len(tutorials)

        def tut(self, ind):
            """Returns the TutorialText object at the given index."""
            return self.tutorials[ind]

        def between_ids(self, start_id, end_id=None, step=0):
            """
            Return True if the provided step is between the provided
            start and end ids.
            """
            start = 0
            end = self.length
            for tut in self.tutorials:
                if tut.id == start_id:
                    start = self.tutorials.index(tut)
                if tut.id == end_id:
                    end = self.tutorials.index(tut)
            return start <= step <= end

        def before_id(self, start_id, step=0):
            """
            Return True if the provided step is before the provided
            start id.
            """
            start = 0
            for tut in self.tutorials:
                if tut.id == start_id:
                    start = self.tutorials.index(tut)
                    return step < start
            return False

        def after_id(self, end_id, step=0):
            """
            Return True if the provided step is after the provided
            end id.
            """
            end = self.length
            for tut in self.tutorials:
                if tut.id == end_id:
                    end = self.tutorials.index(tut)
                    return step > end
            return False

################################################################################
## SCREENS
################################################################################
## A slideout menu to tuck away additional options
screen hamburger_menu():

    default show_options = False

    ## Put together three "hamburger" lines
    button:
        ysize sprt.MENU_SIZE+sprt.SPACER
        xsize sprt.MENU_SIZE+sprt.SPACER
        padding (sprt.SPACER, sprt.SPACER)
        alt "Menu"
        action ToggleLocalVariable("show_options")
        has vbox
        spacing int(sprt.MENU_SIZE/6.0/3.0*3.0)
        for i in range(3):
            frame:
                background sprt.ORANGE
                hover_background sprt.CREAM
                ysize (sprt.MENU_SIZE//6) xsize sprt.MENU_SIZE

    if show_options:
        add sprt.GRAY alpha 0.7
        dismiss action SetLocalVariable("show_options", False)
        frame:
            style_prefix 'hamburger'
            at transform:
                on show:
                    xanchor 1.0
                    ease 0.3 xalign 0.0
                on hide:
                    ease 0.3 xanchor 1.0
            has vbox

            button:
                xysize (None, None)
                xalign 1.0 foreground None
                alt "Close Menu" style 'empty'
                action SetLocalVariable("show_options", False)
                hover_background sprt.construct_frame(sprt.RED, "#0000", 2)
                ypadding -sprt.PADDING*2
                text "←" color sprt.ORANGE style 'sprt_text':
                    size int(sprt.BIG_TEXT*2.0) outlines [(1, sprt.ORANGE)]
            label "" style 'hamburger_button' ysize sprt.PADDING

            transclude

            if renpy.has_screen("image_attribute_tool"):
                textbutton "Image Attributes Tool":
                    action ShowMenu("image_attribute_tool")
            if renpy.has_screen("layered_image_visualizer"):
                textbutton "Layered Image Visualizer":
                    action ShowMenu("layered_image_visualizer")
            if renpy.has_screen("tinting_tool"):
                textbutton "Image Tinting Tool":
                    action ShowMenu("tinting_tool")
            if renpy.has_screen("colorizing_tool"):
                textbutton "Image Colorizing Tool":
                    action ShowMenu("colorizing_tool")
            if renpy.has_screen("frame_tool"):
                textbutton "Frame Tool":
                    action ShowMenu("frame_tool")

## A hub screen from which to access the various image tools
screen image_tools():

    tag menu

    add sprt.GRAY

    hbox:
        style_prefix 'image_tools'

        if renpy.has_screen("image_attribute_tool"):
            textbutton "Image Attributes Tool":
                action ShowMenu("image_attribute_tool")
        if renpy.has_screen("layered_image_visualizer"):
            textbutton "Layered Image Visualizer":
                action ShowMenu("layered_image_visualizer")
        if renpy.has_screen("tinting_tool"):
            textbutton "Image Tinting Tool":
                action ShowMenu("tinting_tool")
        if renpy.has_screen("mask_tool"):
            textbutton "Image Mask Tool":
                action ShowMenu("mask_tool")
        if renpy.has_screen("position_tool"):
            textbutton "Image Position Tool":
                action ShowMenu("position_tool")
        if renpy.has_screen("colorizing_tool"):
            textbutton "Image Colorizing Tool":
                action ShowMenu("colorizing_tool")
        if renpy.has_screen("frame_tool"):
            textbutton "Frame Tool":
                action ShowMenu("frame_tool")

    use hamburger_menu():
        style_prefix 'hamburger'
        textbutton _("Return") action Return()

## The viewport that shows the image
screen sprt_viewport(demonstration=False, tinted=False):

    viewport:
        ## Where the image is shown
        draggable True id 'image_vp'
        yadjustment sprt.yadj xadjustment sprt.xadj
        yinitial persistent.sprt_yinitial.setdefault(persistent.sprt_who, 0.5)
        xinitial persistent.sprt_xinitial.setdefault(persistent.sprt_who, 0.5)
        fixed:
            xysize (config.screen_width*4, config.screen_height*4)
            if not demonstration and not tinted:
                add sprt.get_image(persistent.sprt_who, True):
                    align (0.5, 0.5) zoom persistent.sprt_zoom_dict.setdefault(
                        persistent.sprt_who, 1.0)
            elif not demonstration:
                transclude

    vbox:
        style_prefix 'sprt_zoom'
        ## Textual representation of the corrected attributes
        if sprt.get_image(persistent.sprt_who) and not demonstration:
            text sprt.get_image(persistent.sprt_who)
        hbox:
            textbutton "Re-center" action Function(sprt.reset_image_position)
            fixed:
                bar value sprt.SafeDictValue(persistent.sprt_zoom_dict,
                    persistent.sprt_who, 5.0, default_value=1.0)
                text "Zoom {:.2f}".format(
                        persistent.sprt_zoom_dict.get(
                            persistent.sprt_who, 1.0))

    ## Mouse wheel allows you to zoom in and out
    key 'viewport_wheelup' action SetDict(persistent.sprt_zoom_dict,
        persistent.sprt_who,
        min(persistent.sprt_zoom_dict.setdefault(
            persistent.sprt_who, 1.0) + 0.1, 5.0))
    key 'viewport_wheeldown' action SetDict(persistent.sprt_zoom_dict,
        persistent.sprt_who,
        max(persistent.sprt_zoom_dict.setdefault(
            persistent.sprt_who, 1.0) - 0.1, 0.0))

## A screen for dropdowns
screen sprt_dropdown(drop_focus, **frame_properties):
    add sprt.GRAY alpha 0.7
    dismiss action ClearFocus(drop_focus)
    nearrect:
        focus drop_focus
        frame:
            properties frame_properties
            modal True style_prefix 'sprt_drop'
            viewport:
                mousewheel True scrollbars "vertical"
                has vbox
                transclude
                null height sprt.YSPACER


default tut_adj = ui.adjustment()
## A screen to display the text for the tutorial sections
screen sprt_tutorial_text(tutorial, step, return_screen):


    ## Click anywhere to continue
    if return_screen:
        dismiss action If(step < tutorial.length-1,
            [SetScreenVariable("step", step+1),
            Function(tut_adj.change, 0)],
            ShowMenu(return_screen))
        key 'dismiss' action If(step < tutorial.length-1,
            [SetScreenVariable("step", step+1),
            Function(tut_adj.change, 0)],
            ShowMenu(return_screen))
        ## Esc or right-click to exit the tutorial
        key 'game_menu' action ShowMenu(return_screen)
        ## Rollback to see the previous step
        key 'rollback' action [SetScreenVariable("step", max(step-1, 0)),
            Function(tut_adj.change, 0)]

    frame:
        style_prefix "sprt_tut"
        properties tutorial.tut(step).properties
        viewport:
            mousewheel True scrollbars "vertical" yadjustment tut_adj
            fixed:
                if tutorial.tut(step).properties.get('xsize', None) is not None:
                    xsize tutorial.tut(step).properties['xsize']-sprt.PADDING*8
                if tutorial.tut(step).properties.get('ysize', None) is not None:
                    ysize tutorial.tut(step).properties['ysize']-sprt.PADDING*4
                else:
                    fit_first "height"
                vbox:
                    label tutorial.tut(step).title
                    for txt in tutorial.tut(step).text:
                        text txt

################################################################################
## STYLES
################################################################################
style sprt_copy_hbox:
    spacing sprt.PADDING*2 xalign 1.0 yalign 0.0
style sprt_copy_button:
    background sprt.construct_frame(sprt.YELLOW, sprt.BLUE, sprt.PADDING)
    hover_background sprt.construct_frame(sprt.ORANGE, sprt.BLUE, sprt.PADDING)
    padding (sprt.PADDING*4, sprt.PADDING*2)
style sprt_copy_button_text:
    is sprt_text
    text_align 0.5 align (0.5, 0.5)
    outlines [(1, "#000a")]
    hover_color sprt.CREAM

style sprt_small_hbox:
    spacing sprt.PADDING*3
style sprt_small_frame:
    background sprt.construct_frame(sprt.RED, sprt.BLUE, sprt.PADDING)
    padding (sprt.PADDING*3, sprt.PADDING*3)
style sprt_small_button:
    background sprt.construct_frame(sprt.DARKER_ORANGE, sprt.DARK_ORANGE, sprt.PADDING)
    hover_background sprt.construct_frame(sprt.DARK_ORANGE, sprt.ORANGE, sprt.PADDING)
    insensitive_background sprt.construct_frame(Transform(sprt.DARK_ORANGE, alpha=0.4),
        sprt.DARK_ORANGE, sprt.PADDING)
    padding (sprt.PADDING*2, sprt.PADDING*2)
    align (0.5, 0.5)
style sprt_small_button_text:
    is sprt_text
    align (0.5, 0.5)
    hover_color sprt.CREAM
    insensitive_color sprt.YELLOW
    outlines [(1, "#000")]
    insensitive_outlines [(1, sprt.DARK_ORANGE)]
style sprt_small_label:
    background None
style sprt_small_label_text:
    is sprt_text

style sprt_zoom_vbox:
    align (0.0, 1.0) xoffset sprt.SPACER
style sprt_zoom_text:
    is sprt_text
    yalign 0.5 xalign 0.5 layout "subtitle" text_align 0.5
    outlines [(2, "#000")]
    xmaximum config.screen_width-int(config.screen_width/2.2)-100
style sprt_zoom_hbox:
    xmaximum config.screen_width-int(config.screen_width/2.2)-100
    spacing sprt.PADDING*3
style sprt_zoom_button:
    is sprt_small_button
style sprt_zoom_button_text:
    is sprt_small_button_text
style sprt_zoom_fixed:
    fit_first True
style sprt_zoom_bar:
    xalign 0.5 yalign 0.5
    ysize int(sprt.SPACER*1.5)
    base_bar sprt.construct_frame(sprt.BLUE, sprt.MAROON, sprt.PADDING)
    thumb sprt.construct_frame(sprt.BLUE, sprt.RED, sprt.PADDING)

init python in sprt:
    if above_version((7, 7, 0)):
        text_properties = dict(prefer_emoji=False)
    else:
        text_properties = dict()

style sprt_text:
    is empty
    font "DejaVuSans.ttf"
    size sprt.MED_TEXT
    color sprt.WHITE
    hover_color sprt.WHITE
    insensitive_color sprt.WHITE
    selected_color sprt.WHITE
    ## Optionally applies the prefer_emoji property
    properties sprt.text_properties

style hamburger_frame:
    background sprt.BLUE
    xminimum (config.screen_width//4)
    padding (sprt.SPACER, sprt.SPACER)
    yfill True
style hamburger_vbox:
    xminimum (config.screen_width//4)-sprt.SPACER*2
    spacing sprt.PADDING*2
style hamburger_button:
    background None
    selected_background sprt.MAROON
    foreground Transform("#fff2", ysize=max(1, config.screen_height//300),
        yalign=1.0)
    size_group 'hamburger_btn'
    xsize (config.screen_width//4)-sprt.SPACER*2
    bottom_padding max(1, config.screen_height//300)*4
    top_padding sprt.SPACER
    xpadding sprt.PADDING
style hamburger_button_text:
    is sprt_text
    selected_color sprt.WHITE
    color sprt.YELLOW
    hover_color sprt.CREAM

style sprt_drag_frame:
    xalign 1.0 yalign 0.5 xsize int(config.screen_width/2.2)
    padding (sprt.PADDING, sprt.PADDING, sprt.PADDING, sprt.PADDING*2)
    background sprt.construct_frame(sprt.RED, Transform(sprt.GRAY, alpha=0.93),
        sprt.PADDING)
    ymaximum config.screen_height-sprt.SPACER*4
style sprt_drag_vbox:
    spacing sprt.SPACER
style sprt_drag_label:
    background sprt.RED ysize sprt.SPACER*2 xfill True
style sprt_drag_text:
    is sprt_text
    xalign 1.0 yalign 0.5
    outlines [(1, "#000")]
style sprt_drag_hbox:
    spacing sprt.PADDING*3 yalign 0.5
style sprt_drag_button:
    is sprt_small_button
    background sprt.construct_frame(sprt.GRAY, sprt.MAROON, sprt.PADDING)
    hover_background sprt.construct_frame(sprt.DARK_ORANGE, sprt.ORANGE, sprt.PADDING)
    selected_background sprt.construct_frame(sprt.MAROON, sprt.ORANGE, sprt.PADDING)
style sprt_drag_button_text:
    is sprt_small_button_text

style sprt_input_button:
    background sprt.CREAM align (0.5, 0.5)
    hover_background sprt.YELLOW
    selected_background sprt.construct_frame(sprt.RED, sprt.CREAM, sprt.PADDING)
    xsize sprt.SPACER*7
    padding (sprt.PADDING*2, sprt.PADDING*2)
style sprt_input_button_text:
    is sprt_text
    align (0.5, 0.5)
style sprt_input_input:
    is sprt_text
    align (0.5, 0.5)
    color "#000"

style sprt_drop_frame:
    is sprt_small_frame
    align (0.0, 0.0)
    yoffset 15
style sprt_drop_hbox:
    spacing sprt.SPACER
style sprt_drop_vbox:
    spacing sprt.PADDING
style sprt_drop_button:
    is sprt_small_button
    size_group 'tag_drop' xmaximum sprt.SPACER*16
style sprt_drop_button_text:
    is sprt_small_button_text
style sprt_drop_viewport:
    xfit True xfill False yfill False
style sprt_drop_vscrollbar:
    base_bar sprt.MAROON
    thumb sprt.RED xsize sprt.PADDING*4
    unscrollable "hide"
style sprt_drop_side:
    align (0.5, 0.5)
    spacing sprt.XSPACER

style clear_window:
    is empty
    padding (0, 0)
    offset (0, 0) pos (0, 0)

style sprt_tut_side:
    align (0.5, 0.5)
style sprt_tut_viewport:
    align (0.5, 0.5)
style sprt_tut_vscrollbar:
    base_bar sprt.MAROON
    thumb sprt.RED xsize sprt.PADDING*4
    unscrollable "hide"
style sprt_tut_frame:
    background "#0008"
    xsize config.screen_width - int(config.screen_width/2.2)
    xalign 0.0 yalign 0.5
    ymaximum int(config.screen_height*4.0/5.0)
    padding (sprt.PADDING*2, sprt.PADDING*2)
style sprt_tut_fixed:
    xsize (config.screen_width - int(config.screen_width/2.2))-sprt.PADDING*8
    yminimum int(config.screen_height*4.0/5.0)-sprt.PADDING*4
    align (0.5, 0.5)
style sprt_tut_vbox:
    spacing sprt.SPACER
    yalign 0.5 xalign 0.5
style sprt_tut_label:
    padding (sprt.PADDING*2, sprt.PADDING*2)
    align (0.5, 0.5)
style sprt_tut_label_text:
    is sprt_text
    size sprt.BIG_TEXT
    bold True text_align 0.5
    outlines [(3, "#000")]
    color sprt.YELLOW
    layout "subtitle"
style sprt_hyperlink_text:
    is sprt_text
    color sprt.RED hover_color sprt.ORANGE
    hover_underline True
style sprt_tut_text:
    is sprt_text
    align (0.5, 0.5) text_align 0.5
    layout "subtitle"
    outlines [(2, "#000")]
    hyperlink_functions (lambda x : style.sprt_hyperlink_text, hyperlink_function, None, hyperlink_sensitive)
style sprt_temp_tut_frame:
    padding (0, 0)
    xysize (None, None)
    xalign 0.5
    background None

style image_tools_hbox:
    spacing sprt.SPACER*2 xmaximum config.screen_width-sprt.SPACER*3
    align (0.5, 0.5) box_wrap True box_wrap_spacing sprt.SPACER*2
style image_tools_button:
    background sprt.construct_frame(sprt.RED, sprt.BLUE, sprt.PADDING)
    hover_background sprt.construct_frame(sprt.ORANGE, sprt.GRAY, sprt.PADDING)
    xsize int(config.screen_width/5.0)
    ysize int(config.screen_height/5.0)
    padding (sprt.SPACER, sprt.SPACER)
style image_tools_button_text:
    is sprt_text
    align (0.5, 0.5)
    text_align 0.5

################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**image_tool_common.rpy", None)
    build.classify("**image_tool_common.rpyc", "archive")
################################################################################