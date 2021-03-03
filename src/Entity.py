from GameObject import GameObject


class Entity(GameObject):
    """An entity instance within the environment.

    Attributes:
        id (uuid): The uuid of this entity.
        name (str): The name of this entity.
        description (str): The description text for this entity.
        quests (List[Quest]): A list of quests for this entity. Read only.
    """

    quests = []

    def clone_new_instance(self):
        """Clones this entity as a new entity instance with the same properties.

        Returns:
            Entity: A new instance of this entity.
        """

        entity = Entity(self.name, self.description)
        entity.quests = self.quests.copy()
        return entity

    def add_quest(self, quest):
        self.quests.append(quest)
