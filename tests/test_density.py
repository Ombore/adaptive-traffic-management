from src.density import TrafficDensity


def test_low_density():

    class MockResult:

        class Boxes:
            id = [1, 2, 3, 4, 5]

        boxes = Boxes()

    count, density = TrafficDensity().calculate_density(
        MockResult()
    )

    assert count == 5
    assert density == "LOW"


def test_medium_density():

    class MockResult:

        class Boxes:
            id = list(range(15))

        boxes = Boxes()

    count, density = TrafficDensity().calculate_density(
        MockResult()
    )

    assert count == 15
    assert density == "MEDIUM"


def test_high_density():

    class MockResult:

        class Boxes:
            id = list(range(25))

        boxes = Boxes()

    count, density = TrafficDensity().calculate_density(
        MockResult()
    )

    assert count == 25
    assert density == "HIGH"