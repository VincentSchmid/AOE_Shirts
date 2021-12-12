from .State import State


class SettingBackground(State):
    def document_received(self, document):
        self.background = document
        self.model.events.background_set()

    def stateInit(self):
        self.model.clear_data()
        self.send_message("Send Background Image")
        