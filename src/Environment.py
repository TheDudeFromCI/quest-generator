class Environment:
    """A collection of objects that make of the realm in which quests can be constructed and executed.

    Attributes:
        items (List[Item]): A list of items in this environment. Read only.
        locations (List[Location]): A list of locations in this environment. Read only.
        entities (List[Entity]): A list of entities in this environment. Read only.
    """

    def __init__(self):
        """Creates a new, empty environment.
        """

        self.items = []
        self.locations = []
        self.entities = []

    def add_item(self, item):
        """Adds a new item instance to this environment.

        Args:
            item (Item): The item instance to add.
        """

        self.items.append(item)

    def add_location(self, location):
        """Adds a new location instance to this environment.

        Args:
            location (Location): The location to add.
        """

        self.locations.append(location)

    def add_entity(self, entity):
        """Adds a new entity instance to this environment.

        Args:
            entity (Entity): The entity instance to add.
        """

        self.entities.append(entity)
