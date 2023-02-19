def print_greeting(message):
    print(
        message,
    )


if __name__ == "__main__":
    message = "Hi there! this repo is set up to test GitHub Actions workflows"
    message = (
        "Second message to test that only unit and integration tests",
        " are run through Actions when it's a pull request to develop",
        " or main branches",
    )
    print_greeting(message)
