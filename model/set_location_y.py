def set_location_y(model):

    if model.pisnt_null(model.parameters["location_y_relative"]):

        if not isinstance(model.window_location[1], int):
            model.window_location[1] = model.wageo["y_min"]

        rel = model.parameters["location_y_relative"]
        if rel["uniqid"] is not None and rel["uniqid"] in model.windows.wds_uniqid:
            size = model.windows.wds_uniqid[rel["uniqid"]].get_size()
            location = model.windows.wds_uniqid[rel["uniqid"]].get_location()
        else:
            size = model.windows.wds_windows[rel["interpreter"]][rel["wid"]].get_size()
            location = model.windows.wds_windows[rel["interpreter"]][rel["wid"]].get_location()

        model.window_location[1] += size[1] + location[1]

    elif model.pisnt_null(model.parameters["location_y_equal"]):

        rel = model.parameters["location_y_equal"]
        if rel["uniqid"] is not None and rel["uniqid"] in model.windows.wds_uniqid:
            location = model.windows.wds_uniqid[rel["uniqid"]].get_location()
        else:
            location = model.windows.wds_windows[rel["interpreter"]][rel["wid"]].get_location()

        model.window_location[1] = location[1]

    elif model.parameters["location_y"] == 0 or model.parameters["location_y"] is None:
        model.window_location[1] = model.wageo["y_min"]

    elif isinstance(model.parameters["location_y"], int):
        model.window_location[1] = model.wageo["y_min"] + model.parameters["location_y"]

    elif model.reperc.match(str(model.parameters["location_y"])) and isinstance(model.parameters["height"], int):
        percent = int(model.parameters["location_y"].split("%")[0])
        model.window_location[1] = model.wageo["y_min"]
        model.window_location[1] += int((model.wageo["height"] / 100) * percent)
        model.window_location[1] -= int(model.parameters["height"] / 2)

    else:
        model.window_location[1] = 0

    return True