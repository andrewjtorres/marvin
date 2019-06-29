from typing import Any

from ai import main


def test_ai(capfd: Any) -> None:
    main()

    out, err = capfd.readouterr()

    assert out == "Call your main application code here\n"
