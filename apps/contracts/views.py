from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContractForm
from .utils import handle_webp_upload  # handle_webp_upload 函数放在 utils.py 中


def upload_contract_image(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['contract_image']

            # 调用处理 WebP 图片的函数
            image_info = handle_webp_upload(uploaded_file)

            if image_info:
                # 将处理后的信息返回前端
                return JsonResponse({
                    'message': '上传成功',
                    'width': image_info['width'],
                    'height': image_info['height'],
                    'size': image_info['size'],
                    'format': image_info['file_format'],

                })
            else:
                return JsonResponse({'error': '处理 WebP 图片时出现问题'}, status=400)
        else:
            return JsonResponse({'error': '无效的表单数据'}, status=400)

    # 如果是 GET 请求，返回上传页面
    form = ContractForm()
    return render(request, 'upload.html', {'form': form})
