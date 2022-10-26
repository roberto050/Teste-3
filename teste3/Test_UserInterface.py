from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order


def test_get_total_price():
    menu_repository = MenuRepository()
    lanche = Menu(1, "Hot dog", 4.00)
    menu_repository.set_menu_item(lanche)

    order = Order(1, 5)
    assert (order.quantity * lanche.price) == 20
       