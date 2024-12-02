# contracts/utils.py

from PIL import Image

def handle_webp_upload(uploaded_file):
    try:
        # 打开上传的文件
        with Image.open(uploaded_file) as img:
            # 检查文件格式是否为 WebP 或 JPEG
            if img.format not in ('WEBP', 'JPEG'):
                raise ValueError("上传的文件不是 WebP 或 JPEG 格式")

            # 获取图片的宽度和高度
            width, height = img.size

            # 获取图片的文件大小（字节）
            file_size = uploaded_file.size
            # 获取文件格式
            file_format = img.format
            # 输出宽、高、大小和文件类型
            print(f"宽度: {width}px, 高度: {height}px, 文件大小: {file_size / 1024:.2f}KB, 文件类型: {file_format}")

            return {
                'width': width,
                'height': height,
                'size': file_size,
                'format': file_format,
            }
    except Exception as e:
        print(f"处理图片时发生错误: {e}")
        return None