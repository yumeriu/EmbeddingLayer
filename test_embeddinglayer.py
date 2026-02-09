# test_embeddinglayer.py
"""
Tests for EmbeddingLayer module.
"""

import unittest
from embeddinglayer import EmbeddingLayer

class TestEmbeddingLayer(unittest.TestCase):
    """Test cases for EmbeddingLayer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EmbeddingLayer()
        self.assertIsInstance(instance, EmbeddingLayer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EmbeddingLayer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
