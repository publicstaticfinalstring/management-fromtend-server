import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_report_from_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个专业的数据分析助手。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.5,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        raise e
