# test_navigationbar.py
"""
Tests for NavigationBar module.
"""

import unittest
from navigationbar import NavigationBar

class TestNavigationBar(unittest.TestCase):
    """Test cases for NavigationBar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NavigationBar()
        self.assertIsInstance(instance, NavigationBar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NavigationBar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
