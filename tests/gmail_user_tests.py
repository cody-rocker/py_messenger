from nose.tools import eq_

class TestGmailUser(object):

    def test_set_user(self):
        # setup the test
        from messenger.gmail_user import User
        user = User()
        username_bak = user.username
        # run the test
        user.set_user('test_user@email.com')
        eq_(user.username, 'test_user@email.com')
        # teardown the test
        user.set_user(username_bak)

    def test_load_user_settings(self):
        # setup the test
        from messenger.gmail_user import User
        user = User()
        # run the test
        assert user.config_mgr != None
        assert user.settings != None
