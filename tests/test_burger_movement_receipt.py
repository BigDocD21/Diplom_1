import pytest
from burger import Burger
from unittest.mock import MagicMock

class TestBurgerMovement:
    def test_move_ingredient_updates_order_and_price(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_bun.get_price.return_value = 50.0

        cheese = MagicMock()
        cheese.get_name.return_value = "Cheese"
        cheese.get_price.return_value = 30.0
        cheese.get_type.return_value = "filling"

        tomato = MagicMock()
        tomato.get_name.return_value = "Tomato"
        tomato.get_price.return_value = 10.0
        tomato.get_type.return_value = "filling"

        burger.add_ingredient(cheese)
        burger.add_ingredient(tomato)

        burger.move_ingredient(1, 0)
        
        expected_order = ["Tomato", "Cheese"]
        actual_order = [ing.get_name() for ing in burger.ingredients]
        
        assert actual_order == expected_order and burger.get_price() == 140.0


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
        
        receipt = burger.get_receipt()
        
        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= filling Cheese =\n"
            "(==== Sesame Bun ====)\n\n"
            "Price: 130.0"
        )

        assert receipt == expected_receipt