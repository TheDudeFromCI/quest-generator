from pydispatch import Dispatcher


class QuestRequirement(Dispatcher):
    """A base class for a quest requirement. Must be completed to complete a quest.

    Attributes:
        description (str): The description text for this quest requirement.
        is_complete (bool): True if the quest requirement is completed. False otherwise.

    Events:
        completed: Called when the quest requirement is completed.
    """

    _events_ = ['completed']

    def __init__(self, description):
        """Creates a new quest requirement.

        Args:
            description (str): The description text for this quest requirement.
        """

        self.description = description
        self.is_complete = False

    def mark_complete(self):
        """Called to mark this quest requirement as complete.
        """

        self.is_complete = False
        self.emit('completed')


class QuestFailureMethod(Dispatcher):
    """A base class for a quest failure method. If triggered, the quest is instantly failed.

    Attributes:
        description (str): The description text for this quest failure method.
        is_failed (bool): True if the quest has failed. False otherwise.

    Events:
        failed: Called when the quest has failed.
    """

    _events_ = ['failed']

    def __init__(self, description):
        """Creates a new quest failure method.

        Args:
            description (str): The description text for this quest failure method.
        """

        self.description = description
        self.is_failed = False

    def mark_failed(self):
        """Called to mark this quest failure method as failed.
        """

        self.is_failed = True
        self.emit('failed')


class Quest(Dispatcher):
    """A quest instance with a list of requirements and failure methods.

    Attributes:
        name (str): The name of this quest.
        description (str): The description text for this quest.
        requirements (List[QuestRequirement]): A list of requirements for this quest. All must be completed to complete the quest.
        failure_methods (List[QuestFailureMethod]): A list of failure methods for this quest. Failing any of these fails the entire quest.
        is_complete (bool): True if the quest has been completed. False otherwise.
        if_failed (bool): True if the quest is failed. False otherwise.

    Events:
        completed: Called when the quest is completed.
        failed(method: QuestFailureMethod): Called when the quest is failed.
        requirement_met(requirement: QuestRequirement): Called when one of the quest requirements has been met.
    """

    _events_ = ['completed', 'failed', 'requirement_met']

    def __init__(self, name, description, requirements, failure_methods):
        """Creates a new quest instance.

        Args:
            name (str): The name of this quest.
            description (str): The description text for this quest.
            requirements (List[QuestRequirement]): A list of requirements for this quest. All must be completed to complete the quest.
            failure_methods (List[QuestFailureMethod]): A list of failure methods for this quest. Failing any of these fails the entire quest.
        """

        self.name = name
        self.description = description
        self.requirements = requirements
        self.failure_methods = failure_methods
        self.is_complete = False
        self.is_failed = False

        for requirement in self.requirements:
            requirement.bind(complete=lambda r=requirement: self._quest_requirement_met(r))

        for failure in self.failure_methods:
            failure.bind(failure=lambda f=failure: self._quest_failed(f))

    def _quest_requirement_met(self, quest_requirement):
        """Called when a quest requirement is completed. Used to triggers events.

        Args:
            quest_requirement (QuestRequirement): The requirement that was completed.
        """
        all_complete = True
        for requirement in self.requirements:
            all_complete &= requirement.is_complete

        self.is_complete = all_complete
        self.emit('requirement_met', requirement=quest_requirement)

        if all_complete:
            self.emit('completed')

    def _quest_failed(self, failure_method):
        """Called when a quest failure method is triggered. Used to trigger events.

        Args:
            failure_method (QuestFailureMethod): The failure method that was triggered.
        """

        self.is_failed = True
        self.emit('failed', method=failure_method)
