
import unittest
from utils.HTMLTestRunner import HTMLTestRunner


# 收集测试用例
t = unittest.defaultTestLoader.discover("F:/newpro/testpro\wawhtest\case", "test_*.py")

# 运行所有的case并生成测试报告
title = "测试报告"
descr = "这是第一次测试报告"
file_path = "F:/newpro/testpro/wawhtest/report/report.html"

with open(file_path, "wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(t)
