import pytest
from burger import Burger
from unittest.mock import MagicMock

class TestBurgerSetBuns:
    def test_set_buns_assigns_bun_correctly(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun


class TestBurgerPrice:
    @pytest.mark.parametrize("bun_price, expected_total", [
        (50.0, 100.0),
        (100.0, 200.0),
        (0.0, 0.0)
    ])
    def test_get_price_with_different_buns(self, mock_bun, bun_price, expected_total):
        mock_bun.get_price.return_value = bun_price
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_price() == expected_total

    def test_add_ingredient_increases_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        
        mock_bun.get_price.return_value = 50.0
        mock_ingredient.get_name.return_value = "Cheese"
        mock_ingredient.get_price.return_value = 30.0
        mock_ingredient.get_type.return_value = "filling"
        
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 130.0

    def test_remove_ingredient_decreases_price(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_bun.get_price.return_value = 50.0

        ing1 = MagicMock()
        ing1.get_name.return_value = "Cheese"
        ing1.get_price.return_value = 30.0
        ing1.get_type.return_value = "filling"

        ing2 = MagicMock()
        ing2.get_name.return_value = "Tomato"
        ing2.get_price.return_value = 10.0
        ing2.get_type.return_value = "filling"

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        burger.remove_ingredient(0)
        
        assert burger.get_price() == 110.0


class TestBurgerReceipt:
    def test_get_receipt_full_match(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        
        mock_bun.get_name.return_value = "Sesame Bun"
        mock_bun.get_price.return_value = 50.0

        ing_mock = MagicMock()
        ing_mock.get_name.return_value = "Cheese"
        ing_mock.get_price.return_value = 30.0
        ing_mock.get_type.return_value = "filling"
        
        burger.add_ingredient(ing_mock)
        
        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= filling Cheese =\n"
            "(==== Sesame Bun ====)\n\n"
            "Price: 130.0"
        )
        
        assert burger.get_receipt() == expected_receipt