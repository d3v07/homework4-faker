import pytest
import sys
from io import StringIO
from app.calculator import Calculator


def run_calculator_with_input(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))

    captured_output = StringIO()
    sys.stdout = captured_output
    Calculator.repl_calculator()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


def test_main_menu(monkeypatch):
    inputs = ["quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "WELCOME TO THE REPL CALCULATOR" in output
    assert "Goodbye!" in output


def test_addition(monkeypatch):
    inputs = ["+", "5", "3", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 8.0" in output


def test_subtraction(monkeypatch):
    inputs = ["-", "10", "4", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 6.0" in output


def test_multiplication(monkeypatch):
    inputs = ["*", "6", "7", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 42.0" in output


def test_division(monkeypatch):
    inputs = ["/", "20", "5", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 4.0" in output


def test_division_by_zero(monkeypatch):
    inputs = ["/", "5", "0", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "division by zero" in output.lower()


def test_invalid_operator(monkeypatch):
    inputs = ["%", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid choice. Please enter one of: +, -, *, /, history, clear." in output


def test_view_history(monkeypatch):
    inputs = ["+", "4", "2", "history", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "4.0 + 2.0 = 6.0" in output


def test_clear_history(monkeypatch):
    inputs = ["+", "2", "2", "clear", "history", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "History has been erased." in output
    assert "No calculations yet." in output


def test_exit_anytime(monkeypatch):
    inputs = ["quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Goodbye!" in output

def test_invalid_operation(monkeypatch):
    inputs = ["invalid", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid choice. Please enter one of: +, -, *, /, history, clear." in output

"""The tests below are added using the AI(chatgpt) as I was getting only 90% coverage and was confused about how to approach the remaining 10%"""
def test_none_values_in_get_numbers(monkeypatch):
    inputs = ["1", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Goodbye!" in output  # Should exit correctly


def test_division_by_zero_in_perform_calculation(monkeypatch):
    inputs = ["/", "10", "0", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "division by zero" in output.lower()


def test_empty_history(monkeypatch):
    inputs = ["history", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "No calculations yet." in output


def test_clear_history_then_check(monkeypatch):
    inputs = ["+", "2", "2", "clear", "history", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "History has been erased." in output
    assert "No calculations yet." in output
def test_continue_on_invalid_operation(monkeypatch):
    """Ensure 'continue' is triggered on invalid operation"""
    inputs = ["invalid", "+", "2", "2", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid choice. Please enter one of: +, -, *, /, history, clear." in output
    assert "Result: 4.0" in output  # Ensuring it continues correctly after retry


def test_return_none_on_quit_in_get_numbers(monkeypatch):
    """Ensure 'get_numbers()' returns None, None when second number is 'quit'"""
    inputs = ["+", "5", "quit", "quit"]  # Enter valid first number, then quit for second
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Goodbye!" in output

def test_return_none_on_invalid_input_in_get_numbers(monkeypatch):
    """Ensure 'get_numbers()' returns None, None on invalid input"""
    inputs = ["+", "abc", "xyz", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input. Please enter numeric values." in output


def test_valueerror_handling_in_get_numbers(monkeypatch):
    """Ensure ValueError is handled inside get_numbers()"""
    inputs = ["+", "not_a_number", "2", "quit"]  # Added valid number after invalid input
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input. Please enter numeric values." in output

def test_return_none_on_quit_for_first_number(monkeypatch):
    """Ensure 'get_numbers()' returns None, None when first number is 'quit'"""
    inputs = ["+", "quit", "quit"]  # Choose operation, then quit at first number
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Goodbye!" in output
