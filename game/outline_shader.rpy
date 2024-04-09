################################################################################
##
## Outline Shader for Ren'Py
##
################################################################################
## This file includes a shader and transform for an outline effect in
## Ren'Py.
##
## You do not need to read through nor understand the shader! Examples of how
## to use the outline shader are near the top of this file, in the outline_test
## label and sample_outline_screen screen. If you'd like to read up more on how
## it all works, the shader and transforms have been documented below.
##
## If you use this code in your project,
## please credit me as Feniks @ feniksdev.com
## Also consider tossing me a ko-fi @ https://ko-fi.com/fen
################################################################################

########################################################################
## Example script use
########################################################################
## You can remove this label and the accompanying screen & images if you don't
## need them.
## Sample images; you can remove these if you don't need them.
image small_outline = Window(Transform(Placeholder(), crop=(0.0, 0.08, 1.0, 0.4)), style='empty', padding=(25, 25))
image big_outline = Window(Transform(Placeholder(), crop=(0.0, 0.08, 1.0, 1.0)), style='empty', padding=(25, 25))

label outline_test:
    scene expression "#4e4e64"
    "Start."
    show small_outline at truecenter, glow_outline(25, "#fff", num_passes=30)
    "Example 1 - a glowing outline."
    scene expression "#4e4e64"
    show small_outline at truecenter, animated_demonstration()
    "Example 2 - an animated outline."
    scene expression "#4e4e64"
    show small_outline as s2 at truecenter, outline_transform(15, "#fff", 10.0, num_passes=3)
    "Example 3 - a thick outline with multiple passes."
    show small_outline as s3 at truecenter, outline_transform(2, "#dd90ec", 4.0):
        xoffset 500
    "Example 4 - a thin outline."
    show small_outline at truecenter, drop_shadow():
        xoffset -500
    "Example 5 - a drop shadow."
    scene expression "#4e4e64"
    call screen sample_outline_screen()
    "End of demonstration."
    jump outline_test

################################################################################
## Example screen use
################################################################################
screen sample_outline_screen():

    add "#21212d"

    text "Click any item to close this screen." xalign 0.5 ypos 40 bold True:
        ## You can also apply outlines to text! Typically it's simpler to use
        ## the outline property, unless you want to animate it in some way
        ## as is done here. This outline changes colour from red to orange
        ## and back over 2 seconds.
        at transform:
            outline_transform(3, "#ff8335", mesh_pad=True)
            ease 1.0 outline_transform(3, "#f93c3e", mesh_pad=True)
            ease 1.0 outline_transform(3, "#ff8335", mesh_pad=True)
            repeat

    grid 2 2:
        align (0.5, 0.5) spacing 5
        for i in range(4):
            button:
                background "#75533f"
                xysize (400, 400)
                ## By aligning the image, we make sure it appears in the same
                ## location even when there's an outline around it.
                foreground Transform("small_outline", align=(0.5, 0.5), xsize=400, fit='contain')
                ## This At(img, outline_transform(...)) wrapper lets us apply
                ## the outline to a displayable for use in something like a
                ## button.
                hover_foreground At(Transform("small_outline", align=(0.5, 0.5), xsize=400, fit='contain'),
                    outline_transform(8, "#fff", 3.0, num_passes=8.0))
                action Return()

    ## Another demonstration on how you might use a different outline
    ## on a hover state. This one uses a glow outline.
    imagebutton:
        idle At('small_outline', outline_transform(25, "#f005", 10.0, "#f000"))
        hover At('small_outline', outline_transform(25, "#f009", 10.0, "#f000"))
        xcenter 0.15 ycenter 0.3
        focus_mask True
        action Return()

    ## This is another way you might include outlines on idle/hover.
    ## This is especially useful to apply to buttons which include
    ## animations or multiple parts.
    button:
        xcenter 0.15 ycenter 0.7
        focus_mask True
        action Return()
        ## This transform, applied to the whole button, adds the outlines.
        at transform:
            outline_transform(3, "#fff", 3.0)
            on idle:
                ## This animates the outline increasing/decreasing in size,
                ## but you can omit the `ease 0.1` part also for no animation.
                ease 0.1 outline_transform(3, "#fff", 3.0)
            on hover:
                ease 0.1 outline_transform(8, "#fff", 3.0, num_passes=8)
        add 'small_outline'

    ## Here's an example transform which animates the drop shadow to
    ## appear from behind the character and move down and right.
    add "big_outline" yalign 1.0:
        at transform:
            xcenter 0.5
            parallel:
                easein_back 0.5 xcenter 0.85
            parallel:
                outline_transform(0, "#0000", 8.0, offset=(0, 0))
                pause 0.4
                easein_back 0.5 outline_transform(0, "#0e8379", 8.0, offset=(25, 20))


################################################################################
## TRANSFORMS (You probably don't want to remove these, but you may modify them)
################################################################################
## This is the most flexible transform, with all the arguments available for
## modification. Several variations are also declared below with some of the
## arguments already filled out. You can modify this however you like, though
## it's designed so you can pass it in arguments to make it do whatever you
## like. If you have a specific sort of outline you want to use, see the next
## two examples for ways of simplifying this transform.
##
## width : int
##      Width of the outline in pixels. Default: 1
## color : str
##      Color of the outline, as a hex code string. Default: "#fff"
## smoothing : float
##      How much to smooth the outline. Default: 1.0. This means it will check
##      8 different angles around the initial origin point. For smoother rounded
##      corners, increase this value. Larger numbers require more GPU usage.
## end_color : str
##      Color of the outline at the end. Default: None. If None, the outline
##      will be a solid color provided by `color` earlier. Most useful if you'd
##      like the outline to fade out at the end for a glow effect; provide
##      a transparent colour like #0000 for this.
## num_passes : int
##      The number of passes the shader makes when creating the outline. By
##      default, it will only make one pass. If the outline is thick and there
##      are isolated pixels in the image, you may need to increase this value
##      so you don't get a "hole" around the pixels. Default: 1. Increasing
##      this value will increase GPU usage.
## gradient_smoothing : float
##      Similar to `smoothing`, but specifically to help blend the gradient
##      between the `color` and `end_color`. Default: None. If None, it will
##      use the same value as `smoothing`. Larger numbers require more GPU usage.
## is_mesh : bool
##      Whether to turn the child into a mesh. This is True by default so that
##      outlines apply to the image as a whole, rather than individual parts
##      (e.g. if you applied the outline to a layered image, is_mesh=False would
##      mean the eyes, brows, mouth, etc. would all have their own outlines).
##      Default: True
## mesh_pad : bool
##      Whether to pad the mesh to make room for the outline. If your image does
##      not have enough transparent space around it to fit the outline, you can
##      set this to True.
## drawable_res : bool
##      When using a mesh, by default Ren'Py will render the texture at the same
##      resolution as the window displaying the game. This can cause blurriness
##      when zooming in on the texture, in which case you can set this to False
##      to turn this behaviour off. Default: False
## offset : tuple
##      A tuple of (xoffset, yoffset) to offset the outline. Default: (0, 0)
##      Use this for drop shadows.

transform outline_transform(width=1, color="#fff", smoothing=1.0, end_color=None,
        num_passes=1, gradient_smoothing=None, is_mesh=True, mesh_pad=False,
        drawable_res=False, offset=(0, 0)):
    shader 'feniks.outline'
    mesh is_mesh
    mesh_pad (False if not mesh_pad else (int(width),) * 4)
    gl_drawable_resolution drawable_res

    u_width float(width)
    u_num_passes ((max(float(num_passes), 1.0) if width > 0 else 1.0)
        if end_color is None or num_passes > 1 else float(width))
    u_line_color Color(color).rgba
    u_end_color Color(color if end_color is None else end_color).rgba
    u_has_gradient float(1.0 if end_color is not None else 0.0)
    u_smoothness (float(smoothing) if width > 0 else 1.0)
    u_gradient_smoothness (float(gradient_smoothing if gradient_smoothing is not None else smoothing) if width > 0 else 1.0)
    u_offset (float(offset[0]), float(offset[1]))

## A transform that simplifies some of the properties you'll pass to get a
## glowing outline. Feel free to modify this to adjust what properties are
## passed.
transform glow_outline(width=15, color="#fff", mesh_pad=False, num_passes=None):
    outline_transform(width, color, 20.0, "#0000", (num_passes or width*2.0),
        mesh_pad=mesh_pad)

## A transform that simplifies some of the properties you'll pass to get a drop
## shadow effect. Feel free to modify this to adjust what properties are passed.
transform drop_shadow(color="#0008", offset=(15, 15), mesh_pad=False):
    outline_transform(0, color, 1.0, mesh_pad=mesh_pad, offset=offset)

## This transform demonstrates that you can use ATL to adjust the properties of
## the shader over time, such as by changing the colour, the offset, or the
## line width.
transform animated_demonstration():
    shader 'feniks.outline'
    mesh True mesh_pad (20, 20, 20, 20) gl_drawable_resolution False
    u_num_passes 3.0
    u_smoothness 2.0 u_gradient_smoothness 2.0
    u_has_gradient 0.0
    u_end_color Color("#f00").rgba

    block:
        parallel:
            u_line_color Color("#f00").rgba
            linear 0.5 u_line_color Color("#ff0").rgba
            linear 0.5 u_line_color Color("#0f0").rgba
            linear 0.5 u_line_color Color("#0ff").rgba
            linear 0.5 u_line_color Color("#00f").rgba
            linear 0.5 u_line_color Color("#f0f").rgba
            linear 0.5 u_line_color Color("#f00").rgba
            repeat
        parallel:
            u_width 1.0
            ease 2.0 u_width 6.0
            ease 2.0 u_width 1.0
            repeat
        parallel:
            u_offset (-10, 10)
            ease 1.0 u_offset (10, 10)
            ease 1.0 u_offset (10, -10)
            ease 1.0 u_offset (-10, -10)
            ease 1.0 u_offset (-10, 10)
            repeat

################################################################################
## BACKEND - DO NOT REMOVE FROM HERE DOWN!
################################################################################
## SHADER
################################################################################
init -50 python:
    renpy.register_shader("feniks.outline", variables="""
        uniform float u_width;
        uniform vec4 u_line_color;
        uniform vec4 u_end_color;
        uniform float u_smoothness;
        uniform float u_gradient_smoothness;
        uniform float u_has_gradient;
        uniform float u_num_passes;
        uniform vec2 u_offset;

        uniform vec2 u_model_size;
        varying vec2 v_coords;
    """, vertex_300="""
        v_coords = vec2(a_position.x / u_model_size.x, a_position.y / u_model_size.y);
    """, fragment_300="""
        float pi = 3.1415926535897932384626433832795;
        // We always check in at least 8 directions
        float angle_smooth = 8.0 * u_smoothness;
        float grad_smooth = 8.0 * u_gradient_smoothness;

        // Premultiply the alpha for the line colours (for mixing)
        vec4 line_color = vec4(u_line_color.rgb*u_line_color.a, u_line_color.a);
        vec4 end_color = vec4(u_end_color.rgb*u_end_color.a, u_end_color.a);

        // Figure out the size of one pixel based on the texture size
        vec2 pixel_size = vec2(1.0 / u_model_size.x, 1.0 / u_model_size.y);
        vec2 outline_offset = u_offset * pixel_size * vec2(-1.0);

        // Set up some initial values
        vec4 current_pixel = vec4(0.0);
        float closest_dist = u_width;
        vec4 og_color = texture2D(tex0, v_coords);
        float outline = 0.0;

        // This loop runs for num_passes, slowly getting larger and closer to
        // the final width number. The more passes, the better it handles
        // small pixel areas and sharp curves.
        for (float num=u_width; num>=0.0; num-=max(u_width/u_num_passes,
                min(pixel_size.x, pixel_size.y))) {
            // This loop runs for the number of angles the shader is
            // considering. The more angles, the rounder and smoother the
            // final outline.
            for (float i=0.0; i < angle_smooth; i++) {
                float angle = 2.0 * i * pi / angle_smooth;
                vec2 offset = vec2(cos(angle), sin(angle)) * num * pixel_size;
                current_pixel = texture2D(tex0, v_coords + offset + outline_offset);
                outline += current_pixel.a;
                // Also keep track of approximately how far this pixel is
                // from the main texture, for gradient purposes.
                if (current_pixel.a > 0.0) {
                    closest_dist = num;
                }
            }
        }
        // Make sure the outline doesn't go over 1.0; there can only be
        // 100% outline and 0% original image at most.
        outline = min(outline, 1.0);

        // Smoothstep evens out the gradient a little towards the edges, so
        // the cutoff doesn't look so harsh.
        float closest = smoothstep(0.0, 1.0, min(u_has_gradient, closest_dist/u_width));

        // Mix together the start/end line colours based on how far the pixel
        // is from the main image.
        vec4 blend_line = mix(line_color, end_color, closest);
        // And finally, mix the original image with the outline. This is so
        // the outline appears under translucent parts of the main image too,
        // where applicable.
        gl_FragColor = mix(og_color, blend_line, max(0.0, outline-og_color.a));
    """)

################################################################################
## Code to archive this file for a distributed game. Do not remove.
init python:
    build.classify("**outline_shader.rpy", None)
    build.classify("**outline_shader.rpyc", "archive")
################################################################################