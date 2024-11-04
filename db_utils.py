def search_dramas(name, dramas):
    try:
        for drama in dramas:
            if 'Name' in drama and drama['Name'].lower() == name.lower():
                return drama
        return None
    except Exception as e:
        print(f"😢An error occurred while searching for dramas: {e}")
        return None
    finally:
        print("You came to the end!.")


def get_drama_name(name, dramas):
    for i, drama in enumerate(dramas):
        if drama['Name'] == name:
            return i
    return -1