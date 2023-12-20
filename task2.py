# Задание 2
# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.
# Оценивается:
# 1. Полнота и качество реализации
# 2. Оформление кода
# 3. Наличие сравнения и пояснения по быстродействию

from collections import deque

class DequeFifo():
    """Релаизация циклического буфера FIFO с помощью deque"""

    def __init__(self, size):
        self.data = deque(maxlen=size)

    def __len__(self):
        return len(self.data)

    def insert(self, value):
        """Добавление элемента в конец очередь"""
        self.data.append(value)
    
    def pop(self):
        """Извлекает элемент из начала очереди"""
        if self.data:
            return self.data.popleft()
        else:
            raise IndexError('DequeFifo is empty')
    
    def clear(self):
        """Очистить очередь"""
        self.data.clear()

class ListFifo():
    """Релаизация циклического буфера FIFO с помощью списка"""

    def __init__(self, size):
        self.data = []
        self.size = size

    def __len__(self):
        return len(self.data)
    
    def insert(self, value):
        """Добавление элемента в конец очередь"""
        self.data.append(value)
        if self.size < len(self.data):
            self.data.pop(0)

    def pop(self):
        """Извлекает элемент из начала очереди"""
        if self.data:
            return self.data.pop(0)
        else:
            raise IndexError('ListFifo is empty')
    
    def clear(self):
        """Очистить очередь"""
        self.data[:] = []

# Реализация буфера на базе спсика является наименее эффективной, т.к. при добавлении или удалении
# элементов будет постоянно изменяться размер списка. deque оптимизирован для регулярного
# добавления и удаления элементов, поэтому реализация буфера на его основе будет более эффективной. 
