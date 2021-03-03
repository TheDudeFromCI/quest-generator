from GameObject import GameObject


class Item(GameObject):
    """An item instance within the environment.

    Attributes:
        id (uuid): The uuid of this item.
        name (str): The name of this item.
        description (str): The description text for this item.
        unique (bool): Whether or not this item is a unique item.
    """

    unique = False

    def clone_new_instance(self):
        """Clones this item as a new item instance with the same properties.

        Returns:
            Item: A new instance of this item.
        """

        item = Item(self.name, self.description)
        item.unique = self.unique
        return item
