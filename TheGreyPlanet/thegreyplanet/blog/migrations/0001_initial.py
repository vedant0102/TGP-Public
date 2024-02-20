# Generated by Django 3.0.3 on 2020-07-18 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last Name')),
                ('pen_name', models.CharField(default='', help_text='Only fill if you are not going to use real name', max_length=40, verbose_name='Pen name')),
                ('photo', models.ImageField(upload_to='authors/profilepics', verbose_name='Profile Photo')),
                ('desc', models.TextField(max_length=100, verbose_name='Something about yourself')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('instagram_url', models.URLField(default='https://www.instagram.com/', verbose_name='Instagram URL')),
                ('facebook_url', models.URLField(default='https://www.facebook.com/', verbose_name='Facebook URL')),
                ('linkedin_url', models.URLField(default='https://www.linkedin.com/', verbose_name='Linkedin URL')),
                ('twitter_url', models.URLField(default='https://twitter.com/', verbose_name='Twitter URL')),
                ('profile_redirect_url', models.URLField(default='https://www.instagram.com/', help_text='Personal blog page URL or any main social media URL', verbose_name='Profile page URL')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_for', models.CharField(max_length=100, verbose_name='Content For')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='CustomTag',
            fields=[
                ('tag', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Name')),
                ('color', models.CharField(help_text='Hexcode for color. eg:- #ffffff', max_length=7)),
                ('desc', models.TextField(max_length=100, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last Name')),
                ('title', models.CharField(max_length=60, verbose_name='Job Title')),
                ('degree', models.TextField(verbose_name='Degree and Stream')),
                ('college', models.CharField(default='', max_length=200, verbose_name='College')),
                ('profile_photo', models.ImageField(upload_to='team/profilepics', verbose_name='Profile Photo')),
                ('second_photo', models.ImageField(upload_to='team/backgroundpics', verbose_name='Background Photo')),
                ('quote', models.TextField(max_length=300, verbose_name='Quote or a line about yourself')),
                ('skills', models.TextField(max_length=300, verbose_name='Skills')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('instagram_url', models.URLField(default='https://www.instagram.com/', verbose_name='Instagram URL')),
                ('facebook_url', models.URLField(default='https://www.facebook.com/', verbose_name='Facebook URL')),
                ('linkedin_url', models.URLField(default='https://www.linkedin.com/', verbose_name='Linkedin URL')),
                ('twitter_url', models.URLField(default='https://twitter.com/', verbose_name='Twitter URL')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('post_title', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Title')),
                ('post_slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('post_desc', models.TextField(max_length=300, verbose_name='Description')),
                ('post_text', models.TextField(verbose_name='Story')),
                ('post_date', models.DateField(verbose_name='Date published')),
                ('post_img', models.ImageField(null=True, upload_to='', verbose_name='Thumbnail')),
                ('featured', models.BooleanField(default=False)),
                ('popular', models.BooleanField(default=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
                ('custom_tag', models.ManyToManyField(to='blog.CustomTag')),
                ('post_section', models.ManyToManyField(to='blog.Section')),
            ],
        ),
    ]
