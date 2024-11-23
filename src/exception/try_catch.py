def test_exception():
    try:
        y = 3 / 0
    except NameError as ne:
        print(f"Have some NameError: {ne}")
    except Exception as e:
        print(f"Have some exception: {e}")


test_exception()
