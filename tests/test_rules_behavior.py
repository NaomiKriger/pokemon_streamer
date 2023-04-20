import unittest
from unittest import TestCase


class TestMatchedRules(TestCase):
    @unittest.skip("Not implemented")
    def test_match_rule_1(self):  # return expected destination
        pass

    @unittest.skip("Not implemented")
    def test_match_rule_2(self):  # return expected destination
        pass

    @unittest.skip("Not implemented")
    def test_no_rule_matched(self):  # no destination is returned
        pass


class TestRulesConfigValidity(TestCase):
    @unittest.skip("Not implemented")
    def test_config_file_exists(self):
        pass

    @unittest.skip("Not implemented")
    def test_config_file_content_is_empty(self):
        pass

    @unittest.skip("Not implemented")
    def test_config_file_path_not_found(self):
        pass

    @unittest.skip("Not implemented")
    def test_config_file_content_not_of_expected_type(self):  # not json / string
        pass

    @unittest.skip("Not implemented")
    def test_config_file_content_has_no_rules(self):
        pass

    @unittest.skip("Not implemented")
    def test_rules_in_config_are_of_invalid_format(self):  # e.g. no operators
        pass

    @unittest.skip("Not implemented")
    def test_rule_with_no_url(self):
        pass

    @unittest.skip("Not implemented")
    def test_rule_with_invalid_url(self):  # e.g. not a URL format, not a string
        pass

    @unittest.skip("Not implemented")
    def test_rule_with_no_reason(self):
        pass
