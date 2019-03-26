from ai import main


def test_ai(capfd):
    main()

    out, err = capfd.readouterr()

    assert out == "Call your main application code here\n"
