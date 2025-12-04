from ui import PaintUI

__version__ = "1.0.0"


def main():
    print(f"Paint Calculator v{__version__}")
    ui = PaintUI()
    ui.run()


if __name__ == "__main__":
    main()
