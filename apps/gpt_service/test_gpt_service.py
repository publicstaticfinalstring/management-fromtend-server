import unittest
from unittest.mock import patch, MagicMock
from apps.gpt_service.gpt_service import analyze_data  # 导入你要测试的函数
import django
from django.conf import settings
import os

# 配置 Django 的 settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chances_pear.settings')
django.setup()

class TestGenerateReport(unittest.TestCase):

    @patch('apps.gpt_service.gpt_service.OpenAI')  # 使用 mock 对象来替换 OpenAI 客户端
    def test_generate_report(self, MockOpenAI):
        # 创建一个模拟的 OpenAI 客户端实例
        mock_client = MockOpenAI.return_value

        # 配置模拟的聊天响应
        mock_completion = MagicMock()
        mock_completion.choices = [
            MagicMock(message={'content': '这是一个测试响应。'})
        ]
        mock_client.chat.completions.create.return_value = mock_completion

        # 调用函数，传入测试的 prompt
        prompt = "请根据这些数据生成一个测试报告。"
        try:
            result = analyze_data(prompt)

            # 断言返回值是否符合预期
            self.assertEqual(result, '这是一个测试响应。')
        except Exception as e:
            print(f"测试中发生错误：{e}")
            self.fail(f"generate_report 方法测试失败，错误信息：{e}")

if __name__ == '__main__':
    unittest.main()
