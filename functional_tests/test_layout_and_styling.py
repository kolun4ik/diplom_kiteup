from .base import FunctionalTest
from unittest import skip


class LayoutAndStylingTest(FunctionalTest):
    """тест макета и стилевого оформления"""
    @skip
    def test_layout_and_styling(self):
        """тест макета и стилевого оформления"""
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1920,1080)
        # мы видим что заголовок сайта и список новостей аккуратно отцентрированны
        title = self.browser.find_element_by_id('id_item_news')

        self.assertAlmostEqual(
            title.location['x'] + title.size['width'] / 2,
            960,
            delta=20
        )
