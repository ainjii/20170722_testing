import unittest

import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Sets up fake browser for testing."""
        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Test the greeting on my party site is working."""
        result = self.client.get("/")
        self.assertIn("I'm having a party", result.data)

    def test_no_rsvp_yet(self):
        """Make sure my friends can see the form if they have not RSVP'd yet."""
        result = self.client.get('/')
        self.assertIn('<form method="POST" action="/rsvp">', result.data)
        self.assertNotIn('123 Magic Unicorn Way', result.data)

    def test_rsvp(self):
        """Ensure my friends can see the party details after they RSVP."""
        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)
        self.assertIn('123 Magic Unicorn Way', result.data)
        self.assertNotIn('<form method="POST" action="/rsvp">', result.data)

    def test_rsvp_mel(self):
        """Under no circumstances give the party details to Mel!!"""
        result = self.client.post("/rsvp",
                                  data={'name': "Mel Melitpolski", 'email': "mel@ubermelon.com"},
                                  follow_redirects=True)
        self.assertNotIn('123 Magic Unicorn Way', result.data)
        self.assertIn('<form method="POST" action="/rsvp">', result.data)


    def test_rsvp_mel_flexible(self):
        """Under no circumstances give the party details to Mel!!"""
        result = self.client.post("/rsvp",
                                  data={'name': "melOn man", 'email': "someoneelse@gmail.com"},
                                  follow_redirects=True)
        self.assertNotIn('123 Magic Unicorn Way', result.data)
        self.assertIn('<form method="POST" action="/rsvp">', result.data)


if __name__ == "__main__":
    unittest.main()