from .integration_test_case import IntegrationTestCase


class TestEventsAPI(IntegrationTestCase):

    def test_get_events_streamed(self):
        resp = self.client.get_events()
        events = resp.iter_lines()
        assert next(events)
