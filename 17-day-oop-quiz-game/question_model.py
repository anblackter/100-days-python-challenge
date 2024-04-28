class Question:
    """Model the question object"""

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer
