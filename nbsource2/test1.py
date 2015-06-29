import unittest
from widget import Widget

class WidgetSizeTestCase(unittest.TestCase):
    def test_creation(self):
        widget = Widget("My Widget")
        self.assertEqual(widget.size(), (50, 50),
                     "Initial size is not (50, 50)")
if __name__ == "__main__":
    unittest.main()