def create_parameters(interpreter, item):

    parameters = {}
    if "k" in item[0]:
        parameters["t"] = item[0]["t"]

    for parameter in interpreter.config[item[0]["t"]]:
        if parameter in interpreter.config["parameters"]:

            parameters[parameter] = interpreter.config[item[0]["t"]][parameter]

            if parameter in item[0]:
                parameters[parameter] = item[0][parameter]

            if isinstance(parameters[parameter], list):
                parameters[parameter] = interpreter.list_to_tuple(parameters[parameter])

    return parameters