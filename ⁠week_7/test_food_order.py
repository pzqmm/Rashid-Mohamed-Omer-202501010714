from food_order import calculate_total

def test_order1():
    # test if total food order is equal to 20
    assert calculate_total(10, 2) == 20

    # test if total food order is equal to 30
    assert calculate_total(15, 2) == 30

    # test if total food order is equal to 100
    assert calculate_total(20, 5) == 100

    # test if total food order is equal to 10
    assert calculate_total(5, 2) == 10

    # test if total food order is equal to "invalid price"
    assert calculate_total(-5, 2) == "invalid price"

    # test if total food order is equal to "invalid quantity"
    assert calculate_total(10, 0) == "invalid quantity"
