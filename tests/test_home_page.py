class TestHomePage:
    def test_home_page_is_loaded(self, automationexercise_ui):
        home_page = automationexercise_ui.home_tab

        assert home_page.nav_bar_is_visible
