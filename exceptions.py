class NegativeTitlesError(Exception):
    def __init__(self, message="titles cannot be negative") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidYearCupError(Exception):
    def __init__(self, message="there was no world cup this year") -> None:
        self.message = message
        super().__init__(self.message)


class ImpossibleTitlesError(Exception):
    def __init__(
        self, message="impossible to have more titles than disputed cups"
    ) -> None:
        self.message = message
        super().__init__(self.message)
