from enum import Enum
from datetime import datetime
from os import getcwd, path, makedirs

class MessageLevel(Enum):
    INFORMATION = "INFO"
    WARNING = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"

class Logger():
    def __init__(self):
        self.path = path.join('..', 'logs')
        self.history = []
        pass

    def log(self, message: str="--", error: Exception=None, level: MessageLevel= MessageLevel.INFORMATION):
        message_str = ""
        log_message = ""
        if error:
            message_str = f"{type(error).__name__}\n{error}"
        else:
            message_str = message
        
        log_message = f"[{level.value}] {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}: {message_str}"

        print(log_message)
        self.history.append(log_message)
        return {"level": level.value, "message": message_str}
        

    def create_log_file(self):
        if not path.isdir(self.path):
            makedirs(self.path)

        with open(f"{self.path}/log-{datetime.today().strftime('%Y-%m-%d-%H-%M-%S')}.txt", "w") as file:
            for message in self.history:
                file.write(f"{message}\n")

logger = Logger()