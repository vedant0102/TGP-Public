from django.db import models
import datetime
from slugify import slugify

# Create your models here.

class Content( models.Model):
    content_for = models.CharField( verbose_name='Content For', max_length=100)
    content = models.TextField( verbose_name='Content')

    def __str__(self):
        return self.content_for


class TeamMember( models.Model ):
    first_name = models.CharField( verbose_name='First Name', max_length=40 )
    last_name = models.CharField( verbose_name='Last Name', max_length=40 )
    title = models.CharField(verbose_name='Job Title', max_length=60)
    degree = models.TextField(verbose_name='Degree and Stream')
    college = models.CharField(verbose_name="College", max_length=200, default='')
    profile_photo = models.ImageField( verbose_name='Profile Photo', upload_to='team/profilepics' )
    second_photo = models.ImageField( verbose_name='Background Photo', upload_to='team/backgroundpics' )
    quote = models.TextField(verbose_name='Quote or a line about yourself', max_length=300)
    skills = models.TextField(verbose_name='Skills',max_length=300)
    email = models.EmailField( verbose_name='Email address' )
    instagram_url = models.URLField( verbose_name='Instagram URL' ,blank=True)
    facebook_url = models.URLField( verbose_name='Facebook URL' ,blank=True)
    linkedin_url = models.URLField( verbose_name='Linkedin URL',blank=True)
    twitter_url = models.URLField( verbose_name='Twitter URL' ,blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Email( models.Model ):
    name = models.CharField(verbose_name='Name',max_length=60)
    email = models.EmailField(verbose_name='Email Address')

    def __str__(self):
        return self.email

class Message( models.Model):
    first_name = models.CharField( verbose_name="First Name",max_length=100 )
    last_name = models.CharField( verbose_name="Last Name", max_length=100)
    email = models.EmailField( verbose_name='Email address' )
    message = models.TextField( verbose_name='Message' )
    timestamp = models.DateTimeField( verbose_name="Timestamp", auto_now_add=True )

    def __str__(self):
        return self.first_name + " " + self.last_name


class Author( models.Model ):
    first_name = models.CharField(verbose_name='First Name',max_length=40)
    last_name = models.CharField(verbose_name='Last Name',max_length=40)
    pen_name = models.CharField( verbose_name='Pen name', max_length=40,default='',blank=True ,help_text="Only fill if you are not going to use real name")
    photo = models.ImageField(verbose_name='Profile Photo',upload_to='authors/profilepics')
    desc = models.TextField(verbose_name='Something about yourself', max_length=200)
    email = models.EmailField(verbose_name='Email address')
    instagram_url = models.URLField( verbose_name='Instagram URL',blank=True )
    facebook_url = models.URLField( verbose_name='Facebook URL',blank=True )
    linkedin_url = models.URLField( verbose_name='Linkedin URL',blank=True )
    twitter_url = models.URLField( verbose_name='Twitter URL',blank=True )
    profile_redirect_url = models.URLField( verbose_name='Profile page URL', help_text='Personal blog page URL or any main social media URL',blank=True)

    def __str__(self):
        if self.pen_name:
            return self.pen_name
        else:
            return self.first_name + " " + self.last_name

class Section( models.Model ):
    name = models.CharField( verbose_name='Name', max_length=20, primary_key=True )
    color = models.CharField( max_length=7, help_text="Hexcode for color. eg:- #ffffff" )
    desc = models.TextField( verbose_name='Description',max_length=200)
    service = models.BooleanField( verbose_name='Service?', default=False )
    def __str__(self):
        return self.name


class CustomTag( models.Model ):
    tag = models.CharField(verbose_name='Name',max_length=20,primary_key=True)

    def __str__(self):
        return self.tag
    def get_blogs(self):
        return self.blogpost_set.all()


class BlogPost( models.Model ) :
    post_title = models.CharField( verbose_name='Title', max_length=200, primary_key=True )
    post_slug = models.SlugField( verbose_name='Slug', max_length=200 )
    post_desc = models.TextField( verbose_name='Description', max_length=300 )
    post_text = models.TextField( verbose_name='Story')
    post_date = models.DateField( verbose_name='Date published' )
    post_img = models.ImageField( verbose_name='Thumbnail',null=True )
    author = models.ForeignKey( Author, on_delete=models.CASCADE, default=1 )
    post_section = models.ManyToManyField( Section )
    custom_tag = models.ManyToManyField(CustomTag)
    featured = models.BooleanField( default=False )
    popular = models.BooleanField( default=True )
    preview = models.BooleanField( default=True)

    def __str__(self) :
        return self.post_title

    def get_sections(self):
        return self.post_section.all()

    def get_tag_color(self) :
        return self.post_category.color

    def arrange_row_wise(cards_per_row) :
        latest_blogs = BlogPost.objects.order_by( '-post_date' )[:10]
        row_wise_blogs = []
        for i in range( 0, len( latest_blogs ), cards_per_row ) :
            if len( latest_blogs ) - i >= cards_per_row :
                row_wise_blogs.append( latest_blogs[i :i + cards_per_row] )
            else :
                row_wise_blogs.append( latest_blogs[i : len( latest_blogs )] )
        return row_wise_blogs

    def get_text_timestamp(self) :
        timestamp = self.post_date.strftime( "%d %b, %Y" )
        text_timestamp = "Posted on " + timestamp
        return text_timestamp

    def get_posts_in_section(section) :
        matching_blogs = BlogPost.objects.filter( post_section=section )

        return matching_blogs

    def save(self, *args, **kwargs) :
        self.post_slug = slugify( self.post_title )
        super( BlogPost, self ).save( *args, **kwargs )