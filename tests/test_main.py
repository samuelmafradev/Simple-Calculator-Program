import io
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch

from CalculatorProgram.main import calculate, run_calculator


class CalculateTests(unittest.TestCase):
    def test_supported_operators(self):
        cases = [
            (7, "+", 3, 10),
            (7, "-", 3, 4),
            (7, "*", 3, 21),
            (6, "/", 3, 2),
        ]

        for first, operator, second, expected in cases:
            with self.subTest(operator=operator):
                self.assertEqual(calculate(first, operator, second), expected)

    def test_division_by_zero_returns_error_message(self):
        self.assertEqual(
            calculate(10, "/", 0),
            "Can NOT be divided by zero.",
        )

    def test_invalid_operator_returns_error_message(self):
        self.assertEqual(calculate(2, "%", 1), "Invalid Operator.")


class RunCalculatorTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["2.5", "*", "4"])
    def test_prints_calculation_result(self, _mock_input):
        with patch("builtins.print") as mock_print:
            run_calculator()

        mock_print.assert_any_call("The result is: 10.0")

    @patch("builtins.input", side_effect=["not-a-number"])
    def test_handles_invalid_numeric_input(self, _mock_input):
        with patch("builtins.print") as mock_print:
            run_calculator()

        mock_print.assert_any_call("Invalid input bro.")


class CalculatorProgramTests(unittest.TestCase):
    def test_main_loop_repeats_until_user_quits(self):
        script_path = (
            Path(__file__).resolve().parents[1] / "CalculatorProgram" / "main.py"
        )
        responses = ["2", "+", "3", "y", "8", "/", "2", "n"]

        with (
            patch("builtins.input", side_effect=responses),
            patch("sys.stdout", new_callable=io.StringIO) as output,
        ):
            runpy.run_path(str(script_path), run_name="__main__")

        self.assertEqual(output.getvalue().count("--- Calculator Program ---"), 2)
        self.assertIn("The result is: 5.0", output.getvalue())
        self.assertIn("The result is: 4.0", output.getvalue())
        self.assertIn("End of the program.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
