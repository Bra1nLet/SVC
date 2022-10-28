# Generated by Django 4.0.6 on 2022-10-28 10:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_lesson', models.DateTimeField()),
                ('end_lesson', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=100, validators=[django.core.validators.MaxLengthValidator(100, 'Слишком большое значение')])),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('First_name', models.CharField(max_length=40, validators=[django.core.validators.MaxLengthValidator(40, 'Слишком большое значение')])),
                ('Last_name', models.CharField(max_length=40, validators=[django.core.validators.MaxLengthValidator(40, 'Слишком большое значение')])),
                ('About_me', models.TextField(blank=True, max_length=600)),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lessons', models.ManyToManyField(related_name='Lessons', through='appsch.LessonDate', to=settings.AUTH_USER_MODEL)),
                ('stat', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='appsch.status')),
            ],
        ),
        migrations.AddField(
            model_name='lessondate',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsch.userinfo'),
        ),
        migrations.AddField(
            model_name='lessondate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
