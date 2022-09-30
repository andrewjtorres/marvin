import pytest

import ai


def test_ai(capfd: pytest.CaptureFixture[str]) -> None:
    ai.main()

    out, _ = capfd.readouterr()

    assert out == "Call your main application code here\n"
