import unittest
from unittest.mock import patch
from feed_parser.feed.service import FeedService
import xmltodict
import os


def example_xml_input():
    with open(os.getcwd() + "/tests/resources/input.xml") as f:
        return f.read()


class TestXmlParsing(unittest.TestCase):

    feed_service = FeedService()

    @patch("feed_parser.feed.service.db")
    def test_parse_feed(self, mock_db):
        feed_id = self.feed_service.parse_feed(xmltodict.parse(example_xml_input()))

        self.assertIsNotNone(feed_id)
        self.assertTrue(mock_db.session.add.called)
        self.assertTrue(mock_db.session.commit.called)
