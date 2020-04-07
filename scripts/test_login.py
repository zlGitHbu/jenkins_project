import allure
import pytest
class TestLogin:
    @allure.step("测试步骤1")
    def test_a(self):
        allure.attach("关键字","：123",allure.attach_type.TEXT)
        print(1)

    @allure.step("测试步骤2")
    def test_b(self, test_c):
        print(2)

    @pytest.fixture()
    def test_c(self):
        print(111)

if __name__ == '__main__':
    TestLogin().test_a()