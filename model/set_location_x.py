def set_location_x(model):

    if model.pisnt_null(model.parameters["location_x_relative"]):

        if not isinstance(model.window_location[0], int):
            model.window_location[0] = model.wageo["x_min"]

        rel = model.parameters["location_x_relative"]
        if rel["uniqid"] is not None and rel["uniqid"] in model.windows.wds_uniqid:
            size = model.windows.wds_uniqid[rel["uniqid"]].get_size()
            location = model.windows.wds_uniqid[rel["uniqid"]].get_location()
        else:
            size = model.windows.wds_windows[rel["interpreter"]][rel["wid"]].get_size()
            location = model.windows.wds_windows[rel["interpreter"]][rel["wid"]].get_location()

        model.window_location[0] += size[0] + location[0]

    elif model.pisnt_null(model.parameters["location_x_equal"]):

        rel = model.parameters["location_x_equal"]
        if rel["uniqid"] is not None and rel["uniqid"] in model.windows.wds_uniqid:
            location = model.windows.wds_uniqid[rel["uniqid"]].get_location()
        else:
            location = model.windows.wds_windows[rel["interpreter"]][rel["wid"]].get_location()

        model.window_location[0] = location[0]

    elif model.parameters["location_x"] == 0 or model.parameters["location_x"] is None:
        model.window_location[0] = model.wageo["x_min"]

    elif isinstance(model.parameters["location_x"], int):
        model.window_location[0] = model.wageo["x_min"] + model.parameters["location_x"]

    elif model.reperc.match(str(model.parameters["location_x"])) and isinstance(model.parameters["width"], int):
        percent = int(model.parameters["location_x"].split("%")[0])
        model.window_location[0] = model.wageo["x_min"]
        model.window_location[0] += int((model.wageo["width"] / 100) * percent)
        model.window_location[0] -= int(model.parameters["width"] / 2)

    else:
        model.window_location[0] = 0

    return True