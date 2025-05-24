class ZeroQuantityError(Exception):
    def __init__(self, message=None):
        """инициализатор объектов класса кастомной ошибки. Для перехвата и вывода всяких сообщений"""
        super().__init__(message)
