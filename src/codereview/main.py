#!/usr/bin/env python
import sys
from unittest import result
import warnings
from dotenv import load_dotenv
from datetime import datetime

try:
    from .crew import Codereview
except ImportError:
    from crew import Codereview

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(code: str):
    """
    Run the Codereview crew.
    """
    load_dotenv()
    inputs = {
        'code': code,
    }
    print("--------------------------start--------------------------")
    result = Codereview().crew().kickoff(inputs=inputs)

    print("--------------------------end--------------------------")
    return result

if __name__ == "__main__":
    # This main file is intended to be a way for you to run your
    # crew locally, so refrain from adding unnecessary logic into this file.
    # Replace with inputs you want to test with, it will automatically
    # interpolate any tasks and agents information
    code = """
def find_duplicates(nums):
    seen = set()
    duplicates = []

    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates

numbers = [1, 2, 3, 4, 2, 5, 6, 1]
print(find_duplicates(numbers))
"""
    run(code)