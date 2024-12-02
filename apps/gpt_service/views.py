from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .gpt_service import generate_report_from_gpt
from apps.contracts.models import Contract  # 导入合同模型
from apps.customers.models import Customer  # 导入客户模型
@csrf_exempt
@api_view(['POST'])
def analyze_data_view(request):
    try:
        # 获取请求中的数据
        data = request.data
        contracts = list(Contract.objects.values('contract_number', 'contract_name', 'contract_amount', 'signed_date', 'status', 'period'))

        # 组织要发送到 OpenAI 的提示词
        prompt = f"""
        以下是客户和合同管理模块的数据：
        合同信息：{contracts}

        请根据这些数据，生成一个关于客户和合同关系的报告，指出当前的业务状态、存在的潜在风险，以及改进建议。
        """

        # 调用 gpt_service 来生成报告
        report = generate_report_from_gpt(prompt)
        print("Contracts:", contracts)

        return Response({"report": report}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
