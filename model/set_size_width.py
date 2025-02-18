def set_size_width(model):

    if model.pisnt_null(model.parameters["width_equal"]):

        rel = model.parameters["width_equal"]
        if rel["uniqid"] is not None and rel["uniqid"] in model.windows.wds_uniqid:
            size = model.windows.wds_uniqid[rel["uniqid"]].get_size()
        else:
            size = model.windows.wds_windows[rel["interpreter"]][rel["wid"]].get_size()

        model.window_size[0] = size[0]

    elif model.parameters["width"] is None:
        if model.parameters["height"] is None and not model.pisnt_null(model.parameters["height_equal"]):
            model.window_size[0] = None

    elif model.parameters["width"] == 0 or model.parameters["width"] == "100%":
        model.window_size[0] = model.wageo["width"]
        model.window_size[0] -= model.window_location[0]

    elif isinstance(model.parameters["width"], int):
        model.window_size[0] = model.parameters["width"]

    elif model.reperc.match(str(model.parameters["width"])):
        percent = int(model.parameters["width"].split("%")[0])
        model.window_size[0] = int((model.wageo["width"] / 100) * percent)

    else:
        model.window_size[0] = 0

    if model.window_size[0] is not None:
        model.window_size[0] = int(model.window_size[0])

    return True