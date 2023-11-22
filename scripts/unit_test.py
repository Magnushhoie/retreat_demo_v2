# Import the functions you want to test here
# Or simply paste them in this script for examples sake - Do not do this in practice!


def some_function(input: str) -> str:
    """Tthe function you want to test."""
    return f"output_{input.split('_')[-1]}"


def test_some_function(
        inputs: list = ["input_1", "input_2", "input_3"],
        expected_outputs: list = ["output_1", "output_2", "output_3"],
) -> None:
    """Modify this function to test your functions."""
    for input, expected_output in zip(inputs, expected_outputs):
        assert some_function(input) == expected_output


def main() -> None:
    """Execute tests."""
    test_some_function()
    print("All tests passed")


if __name__ == "__main__":
    main()

print("Nice meeting you all")
