from transportation_on_vacation import rental_car_cost
import random

def test_fixed():
    print("\nFixed Tests")
    assert rental_car_cost(1) == 40
    assert rental_car_cost(4) == 140
    assert rental_car_cost(7) == 230
    assert rental_car_cost(8) == 270
    assert rental_car_cost(0) == 0
    assert rental_car_cost(3) == 100
    assert rental_car_cost(6) == 220

def test_random():
    print("\nRandom Tests")
    for _ in range(40):
        d = random.randint(0, 5000)
        if d >= 7:
            expected = d * 40 - 50
        elif d >= 3:
            expected = d * 40 - 20
        else:
            expected = d * 40
        print(f"testing for rental_car_cost({d})")
        result = rental_car_cost(d)
        assert result == expected, f"{result!r} should equal {expected!r}"
        #pytest