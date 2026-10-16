
APP_NAME = "ERP Release Testing"
VERSION = "2.0.0"


def get_version():
    return VERSION


def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")
    return price * quantity


def main():
    print("=== ERP CI/CD TEST ===")
    print(f"Application: {APP_NAME}")
    print(f"Version: {get_version()}")
    print(f"Total: {calculate_total(100, 3)}")
    print("Release 2.0.0 is ready!")


if __name__ == "__main__":
    main()
