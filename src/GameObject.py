from abc import ABC
from pydispatch import Dispatcher
from uuid import uuid4


class GameObject(ABC, Dispatcher):
    """A base class for all game objects within the environment.

    Attributes:
        id (uuid): The uuid of this game object.
        name (str): The name of this game object.
        description (str): The description of this game object.
    """

    def __init__(self, name, description, id=None):
        self.id = uuid4() if id is None else id
        self.name = name
        self.description = description
