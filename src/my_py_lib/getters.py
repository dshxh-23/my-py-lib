"""
Uses the following modules
    re
    getpass

Contains the following functions:
    get_int
    get_positive_int
    get_float
    get_positive_float
    get_choice
    pet_pwd

Planned additions:
    get_hyperlink
    get_email
    get_fname
    get_lname
    get_full_name
"""

import re
import getpass

def _get_number(parse_func, prompt, min_value, max_value, positive_only=False, value_type_name="number"):
    """
    Internal helper to prompt the user for a number, with error checking and bounds.
    """
    while True:
        try:
            ip = input(prompt)
            num = parse_func(ip)
            if positive_only and num <= 0:
                print(f"Input must be a positive {value_type_name}.")
                continue
            if num < min_value:
                print(f"Input should be greater than or equal to {min_value}.")
                continue
            if num > max_value:
                print(f"Input should be less than or equal to {max_value}.")
                continue
            return num
        except ValueError:
            print(f"Please enter a valid {value_type_name}.")


def get_int(prompt: str = "Input: ", min_value: int = -999_999_999, max_value: int = 999_999_999) -> int:
    """
    Prompt the user for an integer between min_value and max_value (inclusive).

    :param prompt: The prompt to display to the user.
    :param min_value: Minimum allowed value (inclusive).
    :param max_value: Maximum allowed value (inclusive).
    :return: The validated integer input.
    """
    return _get_number(int, prompt, min_value, max_value, value_type_name="integer")


def get_positive_int(prompt: str = "Input: ", max_value: int = 999_999_999) -> int:
    """
    Prompt the user for a positive integer up to max_value (inclusive).

    :param prompt: The prompt to display to the user.
    :param max_value: Maximum allowed value (inclusive).
    :return: The validated positive integer input.
    """
    return _get_number(int, prompt, 1, max_value, positive_only=True, value_type_name="integer")


def get_float(prompt: str = "Input: ", min_value: float = -999_999_999.0, max_value: float = 999_999_999.0) -> float:
    """
    Prompt the user for a float between min_value and max_value (inclusive).

    :param prompt: The prompt to display to the user.
    :param min_value: Minimum allowed value (inclusive).
    :param max_value: Maximum allowed value (inclusive).
    :return: The validated float input.
    """
    return _get_number(float, prompt, min_value, max_value, value_type_name="float")


def get_positive_float(prompt: str = "Input: ", max_value: float = 999_999_999.0) -> float:
    """
    Prompt the user for a positive float up to max_value (inclusive).

    :param prompt: The prompt to display to the user.
    :param max_value: Maximum allowed value (inclusive).
    :return: The validated positive float input.
    """
    return _get_number(float, prompt, 0.0, max_value, positive_only=True, value_type_name="float")


def get_choice(*choices: str, prompt: str = "Input: ", exact_match: bool = False) -> str:
    """
    Prompt the user to select from a list of choices.

    :param choices: Allowed choices (as positional arguments).
    :param prompt: The prompt to display to the user.
    :param exact_match: If True, match case and whitespace exactly. If False, match case-insensitively and ignore leading/trailing whitespace.
    :return: The validated choice as entered by the user.
    """
    if not choices:
        raise ValueError("At least one choice must be provided.")
    choices_display = ', '.join(choices)
    while True:
        user_input = input(f"{prompt} ({choices_display}): ")
        if exact_match:
            if user_input in choices:
                return user_input
        else:
            normalized_choices = [c.strip().casefold() for c in choices]
            if user_input.strip().casefold() in normalized_choices:
                # Return the original choice as defined in choices
                idx = normalized_choices.index(user_input.strip().casefold())
                return choices[idx]
        print(f"Please enter one of the following: {choices_display}")

def get_pwd(prompt: str = "Password: ") -> str:
    """
    Prompt the user for a password securely (input is hidden) and validate its syntax.
    Requirements:
        - At least 8 characters
        - At least 1 uppercase letter
        - At least 1 lowercase letter
        - At least 1 digit
        - At least 1 special character (non-alphanumeric)
    Prompts again if the password does not meet requirements.
    :param prompt: The prompt to display to the user.
    :return: The validated password as a string.
    """
    
    try:
        get_input = getpass.getpass
    except ImportError:
        print("Warning: Could not securely hide input. Falling back to visible input.")
        get_input = input

    pattern = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,}$"
    )
    requirements = [
        (lambda s: len(s) >= 8, "Password must be at least 8 characters."),
        (lambda s: any(c.isupper() for c in s), "Password must contain at least one uppercase letter."),
        (lambda s: any(c.islower() for c in s), "Password must contain at least one lowercase letter."),
        (lambda s: any(c.isdigit() for c in s), "Password must contain at least one digit."),
        (lambda s: any(not c.isalnum() for c in s), "Password must contain at least one special character."),
    ]
    while True:
        pwd = get_input(prompt)
        faults = [msg for check, msg in requirements if not check(pwd)]
        if faults:
            for msg in faults:
                print(msg)
            continue
        if not pattern.match(pwd):
            print("Password does not meet the required syntax.")
            continue
        return pwd