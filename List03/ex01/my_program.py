from local_lib import path


def use_path():
    path.Path("test_very_crazy/").rmtree(ignore_errors=True)
    folder = path.Path("test_very_crazy/")
    folder.mkdir(mode= 0o777)
    file_path  = folder / "File_crazy.test"
    file_path.write_text("crazy bitch !!!!!!!!")
    print(file_path.read_text())


if __name__ == "__main__":
    try:
        use_path()
    except Exception as e:
        print(e.with_traceback(), "\n\t", e)