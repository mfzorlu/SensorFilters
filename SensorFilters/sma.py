"""
Simple Moving Average (SMA) Filter for sensor data filtering.

This module provides a memory-efficient SMA filter implementation
using circular buffer for real-time sensor data processing.
"""

from typing import Optional


class SMAFilter:
    """
    Simple Moving Average (SMA) Filter for sensor data filtering.
    Uses a circular buffer for memory efficiency.
    """
    
    def __init__(self, window_size: int = 5) -> None:
        """
        Initialize the SMA filter.
        
        Args:
            window_size (int): Number of samples to average (default: 5)
            
        Raises:
            ValueError: If window_size is not positive
        """
        if window_size <= 0:
            raise ValueError("window_size must be > 0")
        
        self.window_size = window_size
        self.buffer = [0.0] * window_size  # Pre-allocate buffer
        self.sum = 0.0
        self.index = 0
        self.count = 0  # Track number of samples received
    
    def update(self, new_value: float) -> float:
        """
        Add a new sensor reading and return the filtered value.
        
        Args:
            new_value (float): New sensor reading
            
        Returns:
            float: Filtered value (moving average)
        """
        if self.count < self.window_size:
            # Buffer is still filling up
            self.buffer[self.index] = new_value
            self.sum += new_value
            self.count += 1
            self.index = (self.index + 1) % self.window_size
            
            return self.sum / self.count
        else:
            # Buffer is full, use circular buffer approach
            old_value = self.buffer[self.index]
            self.buffer[self.index] = new_value
            
            # Update sum efficiently
            self.sum = self.sum - old_value + new_value
            
            # Move to next position in circular buffer
            self.index = (self.index + 1) % self.window_size
            
            return self.sum / self.window_size
    
    def reset(self) -> None:
        """Reset the filter to initial state."""
        self.buffer = [0.0] * self.window_size
        self.sum = 0.0
        self.index = 0
        self.count = 0
    
    def get_current_average(self) -> Optional[float]:
        """
        Get the current average without adding new data.
        
        Returns:
            float: Current average, or None if no data
        """
        if self.count == 0:
            return None
        return self.sum / min(self.count, self.window_size)
    
    def __repr__(self) -> str:
        """Return a string representation of the filter."""
        return f"SMAFilter(window_size={self.window_size})"