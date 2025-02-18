from io import BytesIO

def graph_draw_image(model, graph: str, location: list, image=None):

    figure = None

    if graph in list(model.items_list.keys()):
        with BytesIO() as output:
            image.save(output, format="PNG")
            image_data = output.getvalue()

        figure = model.window[graph].draw_image(data=image_data, location=location)

    if figure is None:
        return False
    else:
        return figure