# Generated by Django 3.1.1 on 2021-06-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apis',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('base_url', models.TextField()),
                ('request_type', models.TextField()),
                ('headers', models.TextField()),
                ('auth', models.TextField()),
                ('body', models.TextField()),
                ('module', models.TextField()),
                ('class_field', models.TextField(db_column='class')),
                ('single_run', models.SmallIntegerField()),
                ('hour_minute', models.TextField()),
                ('day_of_week', models.TextField()),
                ('day_of_month', models.TextField()),
                ('month', models.TextField()),
                ('running_date_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('parameters', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'apis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('slug', models.TextField()),
                ('province', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('neighborhood', models.CharField(max_length=30)),
                ('shop', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=10)),
                ('take_status', models.CharField(max_length=20)),
                ('pure_seller', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'channels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'companies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyReportGroupHasChannels',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.SmallIntegerField()),
                ('alias', models.CharField(max_length=50)),
                ('channel_group', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'company_report_group_has_channels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyReportGroupHasCrawlers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'company_report_group_has_crawlers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyReportGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('status', models.SmallIntegerField(default=1)),
                ('excel_types', models.IntegerField()),
                ('excel_names', models.IntegerField()),
                ('report_type', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'company_report_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CrawlerHasCrawlerLogFiles',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'crawler_has_crawler_log_files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CrawlerLinks',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_url', models.CharField(max_length=3000, unique=True)),
                ('status', models.CharField(choices=[(1, 'Aktif'), (0, 'Pasif')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'crawler_links',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CrawlerLogFiles',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('path', models.TextField()),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'crawler_log_files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Crawlers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('spider_name', models.TextField(blank=True, null=True)),
                ('rule', models.TextField(blank=True, null=True)),
                ('single_run', models.SmallIntegerField()),
                ('hour_minute', models.TextField(blank=True, null=True)),
                ('day_of_week', models.TextField(blank=True, null=True)),
                ('day_of_month', models.TextField(blank=True, null=True)),
                ('month', models.TextField(blank=True, null=True)),
                ('running_date_time', models.DateTimeField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('province', models.TextField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('neighborhood', models.TextField(blank=True, null=True)),
                ('session', models.TextField(blank=True, null=True)),
                ('user_name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('phone_number', models.TextField(blank=True, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('cookie', models.TextField(blank=True, null=True)),
                ('stay_login_status', models.SmallIntegerField()),
                ('stay_login_url', models.TextField(blank=True, null=True)),
                ('stay_login_xpath', models.TextField(blank=True, null=True)),
                ('stay_location_xpath', models.TextField(blank=True, null=True)),
                ('headers', models.TextField(blank=True, null=True)),
                ('custom_settings', models.TextField(blank=True, null=True)),
                ('is_running', models.SmallIntegerField(blank=True, null=True)),
                ('auto_start', models.SmallIntegerField(blank=True, null=True)),
                ('take_status', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('shop', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'crawlers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=191)),
                ('slug', models.CharField(max_length=191)),
                ('status', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'currencies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=15)),
                ('port', models.CharField(max_length=2)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=25)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'settings',
                'managed': False,
            },
        ),
    ]