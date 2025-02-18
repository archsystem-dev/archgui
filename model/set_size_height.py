def set_size_height(model):

    if model.pisnt_null(model.parameters["height_equal"]):

        rel = model.parameters["height_equal"]
        if rel["uniqid"] is not None and rel["uniqid"] in model.windows.wds_uniqid:
            size = model.windows.wds_uniqid[rel["uniqid"]].get_size()
        else:
            size = model.windows.wds_windows[rel["interpreter"]][rel["wid"]].get_size()

        model.window_size[1] = size[1]

    elif model.parameters["height"] is None:
        if model.parameters["width"] is None and not model.pisnt_null(model.parameters["width_equal"]):
            model.window_size[1] = None

    elif model.parameters["height"] == 0 or model.parameters["height"] == "100%":
        model.window_size[1] = model.wageo["height"]
        model.window_size[1] -= model.window_location[1]
        model.window_size[1] -= 5

    elif isinstance(model.parameters["height"], int):
        model.window_size[1] = model.parameters["height"]

    elif model.reperc.match(str(model.parameters["height"])):
        percent = int(model.parameters["height"].split("%")[0])
        model.window_size[1] = (model.wageo["height"] / 100) * percent

    else:
        model.window_size[1] = 0

    if model.window_size[1] is not None:
        model.window_size[1] = int(model.window_size[1])

    return True