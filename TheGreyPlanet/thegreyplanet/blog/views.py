from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import BlogPost, CustomTag, Section, Email, TeamMember, Message

# Create your views here.
def index(request):
    email = newsletter(request)
    sections = Section.objects.all()
    popular_blogs=BlogPost.objects.filter(popular=True,preview=False).order_by('-post_date')
    blogs=BlogPost.objects.filter(preview=False).order_by( '-post_date' )
    featured_blogs=BlogPost.objects.filter(featured=True,preview=False)
    featured_blog_first=featured_blogs[0]
    featured_blog_rest=featured_blogs[1:]
    context={
        'blogs': blogs,
        'featured_blog_first': featured_blog_first,
        'featured_blog_rest': featured_blog_rest,
        'sections' : sections,
        'email': email,
        'popular_blogs':popular_blogs,
             }

    return render(request, 'blog/newindex.html', context)


def post(request, post_title):
    email = newsletter( request )
    sections = Section.objects.all()
    popular_blogs=BlogPost.objects.filter(preview=False).order_by( '-post_date' )[:2]
    related_blogs=BlogPost.objects.filter(popular=True,preview=False)[:4]
    blog=BlogPost.objects.get(post_slug=post_title,preview=False)
    context={
        'blog': blog,
        'related_blogs': related_blogs,
        'popular_blogs': popular_blogs,
        'sections': sections,
        'email' : email,
    }
    return render( request, 'blog/newpost.html', context )

def donate(request) :
    return render(request,'blog/donate.html',{})

def about(request) :
    email = newsletter( request )
    sections = Section.objects.all()
    members = TeamMember.objects.all()
    context = {
        'members' : members,
        'sections' : sections,
        'email' : email,
    }
    return render( request, 'blog/newabout.html', context )

def section(request,section):
    email = newsletter( request )
    sections = Section.objects.all()
    section_blogs=BlogPost.get_posts_in_section(section)
    section = Section.objects.get(name=section)
    context={
        'blogs': section_blogs,
        'section': section,
        'sections' : sections,
        'email' : email,
    }
    return render( request, 'blog/newsection.html', context )

def search(request):
    email = newsletter( request )
    sections = Section.objects.all()
    if request.GET:
        search_string=str(request.GET.get('search',None))

    search_query=search_string.split(' ')
    results=[]
    for query in search_query:
        try:
            query_matches = CustomTag.objects.filter(tag__iexact=query)
            for match in query_matches:
                results.extend( match.get_blogs() )
        except:
            continue

    context={
        'search_string': search_string,
        'blogs': results,
        'sections' : sections,
        'email' : email,
    }
    return render(request,'blog/newsearch.html',context)

def contact(request):
    email = newsletter( request )
    sections = Section.objects.all()
    context = {
        'sections' : sections,
        'email' : email,
    }
    if request.POST:
        fname = str(request.POST.get("fname",""))
        lname = str( request.POST.get( "lname", "" ) )
        email = str( request.POST.get( "contact-email", "" ) )
        message = str( request.POST.get( "message", "" ) )
        if fname and lname and email and message:
            feedback = Message.objects.create(first_name=fname,last_name=lname,email=email,message=message)
            context['message']=feedback

    return render( request, 'blog/newcontact.html', context )


def preview_posts(request, post_title):
    email = newsletter( request )
    sections = Section.objects.all()
    popular_blogs=BlogPost.objects.filter(preview=True).order_by( '-post_date' )[:2]
    related_blogs=BlogPost.objects.filter(popular=True,preview=True)[:4]
    blog=BlogPost.objects.get(post_slug=post_title,preview=True)
    context={
        'blog': blog,
        'related_blogs': related_blogs,
        'popular_blogs': popular_blogs,
        'sections': sections,
        'email' : email,
    }
    return render( request, 'blog/previewpost.html', context )

def preview(request):
    email = newsletter(request)
    sections = Section.objects.all()
    blogs=BlogPost.objects.filter(preview=True).order_by( '-post_date' )[:10]
    featured_blogs=BlogPost.objects.filter(featured=True,preview=True)
    featured_blog_first=featured_blogs[0]
    featured_blog_rest=featured_blogs[1:]
    context={
        'blogs': blogs,
        'featured_blog_first': featured_blog_first,
        'featured_blog_rest': featured_blog_rest,
        'sections' : sections,
        'email': email,
             }

    return render(request, 'blog/previewindex.html', context)




def newsletter(request):
    if request.POST:
        name = str(request.POST.get("name",""))
        email = str( request.POST.get( "email", "" ) )
        if email=="":
            return None
        elif Email.objects.filter(email=email).count() != 0:
            return "exists"
        else:
            obj = Email.objects.create(name=name,email=email)
            return obj
    else:
        return None

def handler404(request, exception):
    return render(request, 'blog/custom404.html', status=404)

def handler500(request):
    return render(request, 'blog/custom404.html', status=500)
