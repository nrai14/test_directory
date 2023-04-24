from lib.gratitudes import *

def test_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("github")
    result = gratitude.format()

    assert result == "Be grateful for: github"

def test_multiple_gratitude():
    gratitude = Gratitudes()
    gratitude.add("git")
    gratitude.add("snack breaks")
    gratitude.add("makers")
    result = gratitude.format()


    assert result == "Be grateful for: git, snack breaks, makers"