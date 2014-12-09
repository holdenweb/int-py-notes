#
# Now with size() method that does nothing
#
class Widget:
    def __init__(self, title, size=(50, 50)):
        self.title = title
        self._size = size
    def size(self):
        return self._size