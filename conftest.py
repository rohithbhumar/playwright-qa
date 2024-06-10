# conftest.py
import logging

def pytest_configure(config):
    logging.basicConfig(level=logging.INFO, format='\n%(asctime)s - %(levelname)s - %(message)s')
