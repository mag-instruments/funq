from funq.testcase import MultiFunqTestCase

print("STARTING....")

class TestFocusCycling(MultiFunqTestCase):
    __app_config_names__ = ['app_test', 'app_test_2']
    print("STARTED....")

    # def _get_active_window_path(self, funq_client):
    #     print ("internal function")
    #     result = funq_client.active_widget()
    #     return result.path

    def test_cycle_focus_between_two_apps(self):
        print("Starting test")
        app1 = self.funq['app_test']
        print("app 1 get")
        app2 = self.funq['app_test_2']

        for _ in range(10):
            w1 = app1.active_widget()
            self.assertIsNotNone(w1, "app1 should have an active window")

            w2 = app2.active_widget()
            self.assertIsNotNone(w2, "app2 should have an active window")
