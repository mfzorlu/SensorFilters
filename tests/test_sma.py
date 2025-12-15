from SensorFilters.sma import SMAFilter

def test_sma_basic():
    f = SMAFilter(window_size=3)
    data = [1, 2, 3, 4]
    results = [f.update(x) for x in data]

    assert results[0] == 1
    assert results[1] == 1.5
    assert results[2] == 2
    assert results[3] == 3

def test_reset():
    f = SMAFilter(2)
    f.update(10)
    f.update(20)
    f.reset()
    assert f.get_current_average() is None
