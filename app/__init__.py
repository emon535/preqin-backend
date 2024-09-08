# This file can be used to initialize the app package, include global imports, or setup tasks.

# For example, you might initialize logging here, or import crucial modules:
import logging

# Configure logging (if needed)
logging.basicConfig(level=logging.INFO)

# Import and set up other components if necessary
# e.g., import your main app instance
from .main import app

# Optionally expose important components
__all__ = ["app"]
