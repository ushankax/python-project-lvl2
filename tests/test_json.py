from gendiff.engine import generate_diff


def test_gendiff():
    result = generate_diff("before.json", "after.json")
    expect = "{\n  host: hexlet.io\n+ timeout: 20\n- timeout: 50\n+ proxy: 123.234.53.22\n- verbose: True\n}"

    assert result == expect
