# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('pass_field', models.CharField(max_length=16, db_column=b'pass')),
                ('passwd', models.CharField(max_length=16)),
                ('t', models.IntegerField(default=b'0')),
                ('u', models.BigIntegerField(default=b'0')),
                ('d', models.BigIntegerField(default=b'0')),
                ('transfer_enable', models.BigIntegerField(default=b'0')),
                ('port', models.IntegerField(default=b'10000')),
                ('switch', models.IntegerField(default=b'0')),
                ('enable', models.IntegerField(default=b'0')),
                ('type', models.IntegerField(default=b'0')),
                ('last_get_gift_time', models.IntegerField(default=b'0')),
                ('last_rest_pass_time', models.IntegerField(default=b'0')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
                'verbose_name': 'ss\u7528\u6237',
                'verbose_name_plural': 'ss\u7528\u6237',
            },
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_name', models.CharField(max_length=128, verbose_name='\u670d\u52a1\u5668\u540d')),
                ('node_type', models.IntegerField(verbose_name='\u7c7b\u578b')),
                ('node_ip', models.CharField(max_length=128, verbose_name='ip')),
                ('node_method', models.CharField(max_length=64, verbose_name='\u52a0\u5bc6\u7801\u65b9\u5f0f')),
                ('node_info', models.CharField(max_length=128, verbose_name='\u4fe1\u606f')),
                ('node_status', models.CharField(max_length=128, verbose_name='\u72b6\u6001')),
                ('node_order', models.IntegerField(verbose_name='\u6392\u5e8f')),
            ],
            options={
                'verbose_name': '\u4ee3\u7406\u8282\u70b9',
                'verbose_name_plural': '\u4ee3\u7406\u8282\u70b9',
            },
        ),
        migrations.CreateModel(
            name='Prder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_number', models.CharField(max_length=128, verbose_name='\u8ba2\u5355\u53f7')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('activate', models.CharField(default=b'no', max_length=128, verbose_name='\u662f\u5426\u5df2\u4ed8\u6b3e')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=128, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('description', models.TextField(verbose_name='\u4ea7\u54c1\u8bf4\u660e')),
                ('price', models.DecimalField(verbose_name='\u4ef7\u683c', max_digits=8, decimal_places=2)),
                ('date_available', models.DateField(verbose_name='\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1',
                'verbose_name_plural': '\u4ea7\u54c1',
            },
        ),
        migrations.AddField(
            model_name='prder',
            name='order_product',
            field=models.ForeignKey(verbose_name='\u5bf9\u5e94\u4ea7\u54c1', to='ss.Product'),
        ),
        migrations.AddField(
            model_name='prder',
            name='order_user',
            field=models.ForeignKey(verbose_name='\u5bf9\u5e94\u7528\u6237', to=settings.AUTH_USER_MODEL),
        ),
    ]
