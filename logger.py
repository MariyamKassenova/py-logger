class Logger:
    def __init__(self):
        # Словарь для хранения времени последней записи для каждого сообщения
        self.message_time = {}
        # Максимальный размер лога
        self.max_size = 100

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Проверка, существует ли сообщение и не прошло ли 10 секунд
        if message in self.message_time and timestamp < self.message_time[message]:
            return False

        # Обновление времени следующего допустимого вывода сообщения
        self.message_time[message] = timestamp + 10

        # Если размер словаря превышает максимальный размер, очистка логов
        if len(self.message_time) > self.max_size:
            self.clean(timestamp)

        return True

    def clean(self, timestamp: int) -> bool:
        # Очистка сообщений, которые можно удалить
        messages_to_remove = [msg for msg, end_time in self.message_time.items() if end_time <= timestamp]

        if len(messages_to_remove) == len(self.message_time):
            # Если все сообщения устарели, очистка возможна
            self.message_time.clear()
            return True

        # Удаление устаревших сообщений
        for msg in messages_to_remove:
            del self.message_time[msg]

        return len(messages_to_remove) > 0

    def loggerSize(self) -> int:
        return len(self.message_time)


# Пример использования класса Logger
if __name__ == "__main__":
    logger = Logger()

    print(logger.shouldPrintMessage(1, "foo"))  # return True
    print(logger.shouldPrintMessage(2, "bar"))  # return True
    print(logger.shouldPrintMessage(3, "foo"))  # return False
    print(logger.shouldPrintMessage(8, "bar"))  # return False
    print(logger.shouldPrintMessage(10, "foo"))  # return False
    print(logger.shouldPrintMessage(11, "foo"))  # return True
    print(logger.loggerSize())  # return 2
    print(logger.clean(11))  # return False
    print(logger.clean(12))  # return True
