from gendiff.engine import generate_diffdef test_gendiff():    timeout_result = generate_diff("tests/fixtures/old_timeout.json",                                   "tests/fixtures/new_timeout.json")    timeout_expect = "{\n+ timeout: 50\n- timeout: 20\n}"    recursion_result = generate_diff("tests/fixtures/old_recur.json",                                     "tests/fixtures/new_recur.json")    recursion_expect = "{\n  recursion: {a: 42}\n}"    assert timeout_result == timeout_expect    assert recursion_result == recursion_expect