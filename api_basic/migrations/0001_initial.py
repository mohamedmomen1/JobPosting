# Generated by Django 3.2.6 on 2021-08-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jid', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('applyDate', models.DateTimeField(auto_now_add=True)),
                ('resumee', models.CharField(max_length=100)),
                ('univ', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=100)),
                ('gpa', models.CharField(max_length=100)),
                ('standing', models.CharField(max_length=100)),
                ('numDays', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesForInterShipApps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciaid', models.CharField(max_length=100)),
                ('jid', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employment_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginDate', models.DateTimeField(auto_now_add=True)),
                ('endDate', models.DateTimeField(auto_now_add=True)),
                ('position', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('cid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('passwrd', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('military_service_stat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Eu_emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Eu_employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('comp_cid', models.CharField(max_length=100)),
                ('beginDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='hRRs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('passwrd', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('endUser_username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InternshipJobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jid', models.CharField(max_length=100)),
                ('minnumDays', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job_posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jid', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('numOpenings', models.CharField(max_length=100)),
                ('hrr_username', models.CharField(max_length=100)),
                ('openingdate', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('comp_cid', models.CharField(max_length=100)),
                ('is_manOrIntern', models.CharField(max_length=100)),
                ('contract_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manager_job_posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jid', models.CharField(max_length=100)),
                ('deptName', models.CharField(max_length=100)),
                ('deptSize', models.CharField(max_length=100)),
            ],
        ),
    ]
