# Generated by Django 3.2 on 2021-12-31 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='订单编号')),
                ('customer', models.CharField(max_length=128, verbose_name='客户名称')),
                ('remark', models.CharField(blank=True, max_length=512, null=True, verbose_name='附加说明')),
                ('sales', models.CharField(max_length=16, verbose_name='经手业务')),
                ('order_date', models.CharField(blank=True, max_length=16, null=True, verbose_name='订单建立时间')),
                ('delivery_time', models.CharField(blank=True, max_length=64, null=True, verbose_name='预计发货时间')),
                ('status', models.SmallIntegerField(choices=[(1, '备料'), (2, '配单'), (3, '待生产'), (4, '生产中'), (5, '生产完成'), (6, '物流上传'), (7, '订单完成')], default=1, verbose_name='生产进度')),
                ('produce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL, verbose_name='生产人员')),
            ],
            options={
                'verbose_name': '所有订单',
                'verbose_name_plural': '所有订单',
                'db_table': 'order',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='物料编号')),
                ('material', models.CharField(max_length=256, verbose_name='物料名称')),
                ('number', models.IntegerField(verbose_name='数量')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_order', to='order.order', verbose_name='订单编号')),
            ],
            options={
                'verbose_name': '物料信息',
                'verbose_name_plural': '物料信息',
                'db_table': 'material',
                'ordering': ['-id'],
            },
        ),
    ]
