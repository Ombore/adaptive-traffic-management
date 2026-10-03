from src.signal_optimizer import SignalOptimizer


def test_low_density_green_time():

    optimizer = SignalOptimizer()

    assert optimizer.calculate_green_time("LOW") == 20


def test_medium_density_green_time():

    optimizer = SignalOptimizer()

    assert optimizer.calculate_green_time("MEDIUM") == 40


def test_high_density_green_time():

    optimizer = SignalOptimizer()

    assert optimizer.calculate_green_time("HIGH") == 60


def test_unknown_density_green_time():

    optimizer = SignalOptimizer()

    assert optimizer.calculate_green_time("UNKNOWN") == 30