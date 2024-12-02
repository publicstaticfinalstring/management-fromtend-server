# contracts/forms.py

from django import forms

class ContractForm(forms.Form):
    contract_image = forms.ImageField(label="合同图片上传")
