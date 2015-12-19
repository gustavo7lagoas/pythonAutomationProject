from base import BasePage
from base import InvalidPageException
import time

class CreatePostModal(BasePage):

    _modal_locator = 'createNewPostDialog'
    _headline_locator = '#PostCreate input[name="PostCreate[header]"]'
    _description_locator = '#PostCreate textarea[name="PostCreate[description]"]'
    _media_selector_locator = '#createNewPostDialog .mediaDropdown'
    _create_envygram_locator = 'createNewPost'
    _ad_type_selector_locator = '#createNewPostDialog select[name="PostCreate[adType]"]'

    @property
    def _headline(self):
        return self.driver.find_element_by_css_selector(self._headline_locator)

    @property
    def _description(self):
        return self.driver.find_element_by_css_selector(self._description_locator)

    @property
    def _media_selector(self):
        return self.driver.find_element_by_css_selector(self._media_selector_locator)

    @property
    def _create_envygram(self):
        return self.driver.find_element_by_id(self._create_envygram_locator)

    @property
    def _ad_type_selector(self):
        return self.driver.find_element_by_css_selector(self._ad_type_selector_locator)

    def __init__(self, driver):
        super(CreatePostModal, self).__init__(driver)

    def create_post(self, headline, media, mediaLocation, \
                    adType, description):
        self._headline.clear()
        self._headline.send_keys(headline)
        self._description.clear()
        self._description.send_keys(description)
        self._select_media_type(media)
        self._set_media_type_location(media, mediaLocation)
        self._select_adType(adType)
        time.sleep(2)
        self._create_envygram.click()

    def _select_media_type(self, mediaType):
        self._media_selector.click()
        self.driver.find_element_by_link_text(mediaType).click()

    def _set_media_type_location(self, media, mediaLocation):
        # missing "Image from computer option"
        if media == 'Image From Internet':
            input_locator = '#uploadFromWebsiteDialog input[name="PostCreate[source]"]'
            save_btn_locator = '#uploadFromWebsiteDialog .saveButton'
        elif media == 'Envygram Link':
            input_locator = '#uploadFromEnvygramDialog input[name="PostCreate[source]"]'
            save_btn_locator = '#uploadFromEnvygramDialog .saveButton'
        elif media == 'Video Link':
            input_locator = '#uploadFromEmbedcodeDialog textarea[name="PostCreate[source]"]'
            save_btn_locator = '#uploadFromEmbedcodeDialog .saveButton'
        self.driver.find_element_by_css_selector( \
        input_locator).clear()
        self.driver.find_element_by_css_selector( \
            input_locator).send_keys(mediaLocation)
        self.driver.find_element_by_css_selector(save_btn_locator).click()

    def _select_adType(self, adType):
        adTypeSelect = self.Select(self._ad_type_selector)
        adTypeSelect.select_by_visible_text(adType)


    def _validate_page(self, driver):
        try:
            driver.find_element_by_css_selector(self._headline_locator)
        except:
            raise InvalidPageException('Error - Create Post Modal was'\
                                       + ' not displayed')
