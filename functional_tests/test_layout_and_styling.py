from .base import FunctionalTest
from unittest import skip


class LayoutAndStylingTest(FunctionalTest):
    """тест макета и стилевого оформления"""
    # @skip()
    def test_layout_and_styling(self):
        """тест макета и стилевого оформления"""
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1920,1080)
        # мы видим что заголовок сайта и список новостей аккуратно отцентрированны
        header_h1 = self.browser.find_element_by_tag_name('h1')

        self.assertAlmostEqual(
            header_h1.location['x'] + header_h1.size['width'] / 2,
            960,
            delta=20
        )



