from GameObject import GameObject


class Location(GameObject):
    """An location instance within the environment.

    Attributes:
        id (uuid): The uuid of this location.
        name (str): The name of this location.
        description (str): The description text for this location.
        parent_location (Location): The parent of this location, if this location exists within another location.
    """

    parent_location = None
