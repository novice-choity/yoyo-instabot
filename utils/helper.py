# function that helps to handle getting object
def get_obj_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except Exception:
        # debug error
        return None
