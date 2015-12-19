from base import BasePage
from base import InvalidPageException
from createpostmodal import CreatePostModal

class ProfilePage(BasePage):
    """
    Page object for Profile Page
    It will represents the API for the profile page. Available methods
    create_post - will open the post modal
    endorse product - will open the endorse product modal (it is not working)
    edit_profile - will open the edit profile page
    """

    _create_post_locator = '.createNewPostButton'

    @property
    def _create_post(self):
        return self.driver.find_element_by_css_selector(self._create_post_locator)

    def __init__(self, driver):
        super(ProfilePage, self).__init__(driver)

    def create_post(self, headline, media, mediaLocation, adType, description):
        self._create_post.click()
        createPostModal =  CreatePostModal(self.driver)
        createPostModal.create_post(headline, media, \
                                    mediaLocation, adType, description)

    def _validate_page(self, driver):
        if not driver.title == 'Envygram - Profile':
            raise InvalidPageException('Error - Not in Profile Page')
