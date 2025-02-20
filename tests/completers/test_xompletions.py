import pytest


@pytest.mark.parametrize(
    "args, prefix, exp",
    [
        (
            "xonfig",
            "-",
            {"-h", "--help"},
        ),
        (
            "xonfig colors",
            "b",
            {"blue", "brown"},
        ),
    ],
)
def test_xonfig(args, prefix, exp, xsh_with_aliases, monkeypatch, check_completer):
    from xonsh import xonfig

    monkeypatch.setattr(xonfig, "color_style_names", lambda: ["blue", "brown", "other"])
    assert check_completer(args, prefix=prefix) == exp


@pytest.mark.parametrize(
    "args, prefix, exp, exp_part",
    [
        (
            "xontrib",
            "l",
            {"list", "load"},
            None,
        ),
        (
            "xontrib load",
            "",
            None,
            {
                # the list may vary wrt the env. so testing only part of the coreutils.
                "abbrevs",
                "pdb",
                "bashisms",
                "coreutils",
            },
        ),
    ],
)
def test_xontrib(args, prefix, exp, exp_part, xsh_with_aliases, check_completer):
    result = check_completer(args, prefix=prefix)
    if exp:
        assert result == exp
    if exp_part:
        assert result.issuperset(exp_part), f"{result} doesn't contain {exp_part} "
