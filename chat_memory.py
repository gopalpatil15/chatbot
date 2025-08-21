class ChatMemory:
    def __init__(self, max_turns=5):
        self.max_turns = max_turns
        self.history = []

    def add(self, speaker, text):
        self.history.append(f"{speaker}: {text}")
        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-self.max_turns * 2:]

    def get_context(self):
        return "\n".join(self.history)