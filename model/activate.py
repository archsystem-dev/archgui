def activate(model, monitor, id, title, location=None, size=None, alpha_channel=None, force_toplevel=None):

    model.monitor = monitor
    model.id = id
    model.title = title

    # -----------------------------------------------------------------

    model.wageo = model.windows.wageo[model.monitor]
    model.window_location = [0, 0]
    model.window_size = [0, 0]

    # -----------------------------------------------------------------

    if model.parameters["full-screen"]:

        no_titlebar = True
        keep_on_top = True

        model.window_location = [
            model.wageo["screen_x_min"],
            model.wageo["screen_x_min"]
        ]

        model.window_size = [
            model.wageo["screen_width"],
            model.wageo["screen_height"]
        ]

    else:

        no_titlebar = False
        keep_on_top = False

        location_loaded = False
        if location is not None:
            if isinstance(location, list) and len(location) == 2:
                if isinstance(location[0], int) and isinstance(location[1], int):
                    model.window_location = [int(location[0]), int(location[1])]
                    location_loaded = True

        if not location_loaded:
            if not model.set_location_x():
                return False
            if not model.set_location_y():
                return False

        size_loaded = False
        if size is not None:
            if isinstance(size, list) and len(size) == 2:
                if isinstance(size[0], int) and isinstance(size[1], int):
                    model.window_size = [int(size[0]), int(size[1])]
                    size_loaded = True

        if not size_loaded:
            if not model.set_size_width():
                return False
            if not model.set_size_height():
                return False

    # -----------------------------------------------------------------

    model.layout, model.items_list = model.interpreter.create_layout(model.items)
    model.window = model.fsg.Window(model.title, model.layout,
                                    location=model.list_to_tuple(model.window_location),
                                    size=model.list_to_tuple(model.window_size),
                                    margins=(0, 0),
                                    element_padding=(0, 0),
                                    no_titlebar=no_titlebar,
                                    keep_on_top=keep_on_top,
                                    alpha_channel=alpha_channel,
                                    force_toplevel=force_toplevel,
                                    enable_close_attempted_event=True,
                                    finalize=True)

    model.window_size = model.window.current_size_accurate()

    # relocation = False
    # if model.reperc.match(str(model.parameters["location_x"])) and not isinstance(model.parameters["width"], int):
    #     percent = int(model.parameters["location_x"].split("%")[0])
    #     model.window_location[0] = model.wageo["x_min"]
    #     model.window_location[0] += int((model.wageo["width"] / 100) * percent)
    #     model.window_location[0] -= int(model.window_size[0] / 2)
    #     relocation = True

    # if model.reperc.match(str(model.parameters["location_y"])) and not isinstance(model.parameters["height"], int):
    #     percent = int(model.parameters["location_y"].split("%")[0])
    #     model.window_location[1] = model.wageo["y_min"]
    #     model.window_location[1] += int((model.wageo["height"] / 100) * percent)
    #     model.window_location[1] -= int(model.window_size[1] / 2)
    #     relocation = True

    # if relocation:
    #     geometry = str(model.window_size[0]) + "x"
    #     geometry += str(model.window_size[1]) + "+"
    #     geometry += str(model.window_location[0]) + "+"
    #     geometry += str(model.window_location[1])

    #     model.window.TKroot.wm_geometry(newGeometry=geometry)
    #     model.window.TKroot.update()

    # model.window_dpi = model.window.TKroot.winfo_fpixels('1i')

    # -----------------------------------------------------------------

    return model.window