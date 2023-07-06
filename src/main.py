import pyray


def main() -> None:
    pyray.init_window(800, 600, "py_rpg")
    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.WHITE)
        pyray.draw_text("py_rpg", 100, 100, 24, pyray.BLACK)
        pyray.end_drawing()
    pyray.close_window()


if __name__ == "__main__":
    main()
