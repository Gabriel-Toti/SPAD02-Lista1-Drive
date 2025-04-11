from main_controller import MainController
from main_view import MainView

print("Hello, World!")


if __name__ == "__main__":
    controller = MainController()
    print(controller.get_all_orders()[0])
    controller.create_order()