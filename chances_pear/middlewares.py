import re
from decimal import Decimal, InvalidOperation

class ThousandSeparatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if 'text/html' in response.get('Content-Type', ''):
            response.content = self.process_html_content(response.content)
        return response

    def process_html_content(self, content):
        """
        处理HTML响应内容，将符合条件的数字加上千分号
        """
        content_str = content.decode('utf-8')

        # 使用正则表达式找到5位数及以上的整数和小数，并为其添加千分号
        content_str = self.add_thousand_separator(content_str)

        return content_str.encode('utf-8')

    def add_thousand_separator(self, content_str):
        """
        为5位数及以上的整数和小数加千分号
        """
        def format_number(match):
            number_str = match.group(0)
            try:
                if '.' in number_str:
                    # 小数处理为 Decimal 并加千分号，保留两位小数
                    number = Decimal(number_str)
                    if number >= 10000:  # 5位数及以上的小数
                        return '{:,.2f}'.format(number)
                    else:
                        return '{:.2f}'.format(number)
                else:
                    # 整数处理加千分号
                    number = int(number_str)
                    if number >= 10000:  # 5位数及以上的整数
                        return '{:}'.format(number)
                    else:
                        return number_str
            except (ValueError, InvalidOperation):
                # 如果解析失败，返回原始字符串
                return number_str

        # 匹配整数和小数的正则表达式
        content_str = re.sub(r'(?<!\d)(\d{5,})(\.\d{1,2})?', format_number, content_str)

        return content_str


class SetJavaScriptContentTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # 检查是否是 js 请求，并设置 Content-Type
        if request.path.endswith('.js') or 'jsi18n' in request.path:
            response['Content-Type'] = 'application/javascript'

        return response
