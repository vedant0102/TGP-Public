from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import BlogPost, CustomTag, Section, Author, Email, TeamMember, Content, Message
# Register your models here.

class CustomTagInline(admin.TabularInline):
    model = BlogPost.custom_tag.through
    verbose_name = 'Tag'
    verbose_name_plural = 'Custom Tags'
    extra = 3

class SectionInline(admin.TabularInline):
    model = BlogPost.post_section.through
    verbose_name = 'Section'
    verbose_name_plural = 'Sections'

class BlogPostAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display = ('post_title','author','is_featured','is_popular','status')
    list_filter = ('featured','popular','preview')
    summernote_fields = ('post_text',)
    inlines = [SectionInline, CustomTagInline, ]
    #prepopulated_fields = {"post_slug" : ("post_title",)}
    fieldsets = (
        (None, {'fields': ['post_title',] }),
        ('Content', {'fields': ['post_desc','post_text','post_img']}),
        ('Other Information', {'fields': ['author','post_date','featured','popular','preview']})
    )

    def get_queryset(self,request):
        queryset=super(BlogPostAdmin,self).get_queryset(request)
        queryset=queryset.order_by('author')
        return queryset

    def status(self,obj):
        if obj.preview:
            return format_html("<b style='color:red;'>Preview</b")
        else:
            return format_html("<b style='color:green;'>Live</b")
    def is_popular(self,obj):
        if obj.popular:
            return format_html("<b style='color:orange;'>Popular</b")
        else:
            return ''
    def is_featured(self,obj):
        if obj.featured:
            return format_html("<b style='color:purple;'>Featured</b")
        else:
            return ''

    is_popular.short_description = 'POPULAR'
    is_featured.short_description = 'FEATURED'
    status.short_description='STATUS'

class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp','message','first_name','last_name','email')
    fieldsets = (
        (None, {'fields' : ['message', ]}),
        ('Contact Information', {'fields' : ['first_name', 'last_name', 'email']}),
        (None, {'fields' : ['timestamp' ]})
    )
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Section)
admin.site.register(CustomTag)
admin.site.register(Author)
admin.site.register(Email)
admin.site.register(TeamMember)
admin.site.register(Content)
admin.site.register(Message, MessageAdmin)