# -*- coding: utf-8 -*-

import unittest
from arch.raise_for_restful_exception import RestfulException, convert_exception


class Test(unittest.TestCase):
    """
    测试
    """

    def test_hello(self):
        e = RestfulException('参数错误')
        e = convert_exception(e)
        print(e.errorMsg)

        self.assertEqual(RestfulException, type(e))


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
