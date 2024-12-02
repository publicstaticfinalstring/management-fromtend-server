from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from .models import Contract, Customer


def update_customer_stats(customer):
    """更新客户的合同数量和总金额"""
    contract_stats = Contract.objects.filter(customer=customer).aggregate(
        total_amount=Sum('contract_amount')
    )
    customer.contract_count = Contract.objects.filter(customer=customer).count()
    customer.total_contract_amount = contract_stats['total_amount'] or 0.00
    customer.save()


@receiver(post_save, sender=Contract)
def contract_post_save(sender, instance, **kwargs):
    """在合同保存后更新客户的合同数量和总金额"""
    update_customer_stats(instance.customer)


@receiver(post_delete, sender=Contract)
def contract_post_delete(sender, instance, **kwargs):
    """在合同删除后更新客户的合同数量和总金额"""
    update_customer_stats(instance.customer)
