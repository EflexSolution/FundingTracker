# test_fundingtracker.py
"""
Tests for FundingTracker module.
"""

import unittest
from fundingtracker import FundingTracker

class TestFundingTracker(unittest.TestCase):
    """Test cases for FundingTracker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FundingTracker()
        self.assertIsInstance(instance, FundingTracker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FundingTracker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
