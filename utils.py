def search_dramas(drama_name, dramas):
    for drama in dramas:
        if drama['drama_name'].lower() == drama_name.lower():
            return drama
    return None


def get_drama_name(drama_name, dramas):
    for i, drama in enumerate(dramas):
        if drama['drama_name'] == drama_name:
            return i
    return -1