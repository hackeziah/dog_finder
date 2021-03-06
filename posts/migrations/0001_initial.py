# Generated by Django 3.2.4 on 2021-09-27 16:44

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import posts.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=62, null=True)),
                ('height', models.CharField(blank=True, max_length=62, null=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=64)),
                ('image', models.ImageField(upload_to=posts.models.upload_to_image)),
                ('is_done', models.BooleanField(default=False)),
                ('is_found', models.BooleanField(default=False)),
                ('qr_no', models.CharField(blank=True, max_length=255, null=True)),
                ('qr_image', models.ImageField(upload_to=posts.models.upload_to_image_qr)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('address', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=168)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TypeofPet',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=62)),
                ('description', models.CharField(blank=True, max_length=62, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PostLost',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=255)),
                ('pet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.pet')),
                ('profile_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostFound',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('found_by', models.CharField(max_length=255, verbose_name='Full Name')),
                ('contact_no', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('pet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.pet')),
                ('profile_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pet',
            name='type_of_pet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.typeofpet'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=255)),
                ('post_found', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.postfound')),
                ('post_lost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.postlost')),
                ('profile_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
