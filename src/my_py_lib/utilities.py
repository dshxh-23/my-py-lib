"""
Utility functions for my_py_lib.

Contains:
    chk_pwd
"""

from my_py_lib.getters import get_pwd

def chk_pwd(pwd: str, prompt: str = "Password: ", attempts: int = 2) -> bool:
    """
    Prompt the user to enter a password and check it against the provided password.

    Args:
        pwd (str): The password to check against.
        prompt (str): The prompt to display to the user. Default is "Password: ".
        attempts (int): Number of allowed attempts. Default is 2.

    Returns:
        bool: True if the user enters the correct password within the allowed attempts, False otherwise.
    """
    if attempts < 1:
        raise ValueError("Number of attempts must be at least 1.")
    for i in range(attempts):
        u_pwd = get_pwd(prompt)
        if u_pwd == pwd:
            return True
        print(f"Wrong password. Attempts remaining: {attempts-(i+1)}")
    return False