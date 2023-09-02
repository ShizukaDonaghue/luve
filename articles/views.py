from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from .models import Article
from .forms import ArticleForm


def all_articles(request):
    """ A view to show all articles which are publised"""
    articles = Article.objects.filter(status=1).order_by('-created_on')
    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)


def article_detail(request, slug):
    """ A view to show individual article details """
    article = get_object_or_404(Article, slug=slug)
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        liked = True
    context = {
        'article': article,
        'liked': liked,
    }

    return render(request, 'articles/article_detail.html', context)


def article_like(request, slug):
    """ Allow the user to like or unlike a article when logged in """
    article = get_object_or_404(Article, slug=slug)

    if request.user.is_authenticated:
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)
    else:
        messages.info(
            request, "Please log in to like this article!"
        )

    return HttpResponseRedirect(
            reverse('article_detail', args=[slug]))


def article_dashboard(request):
    """ A view to show all articles in the dashboard"""
    articles = Article.objects.order_by('-created_on')
    context = {
        'articles': articles,
    }

    return render(request, 'articles/article_dashboard.html', context)


@login_required
def add_article(request):
    """ Add an article """
    if not request.user.is_staff:
        messages.error(
            request, 'Sorry, you are not authorised to post articles.')
        return redirect(reverse('home'))

    else:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.author = request.user
                form.instance.slug = slugify(form.instance.title)
                article = form.save()
                messages.success(
                    request, f'{article.title} has been added successfully!')
                return redirect(reverse('article_detail', args=[article.slug]))
            else:
                messages.error(request, 'Failed to add an article. \
                    Please ensure the form is completed fully and try again!')
        else:
            form = ArticleForm()

    template = 'articles/add_article.html'
    context = {
        'form': form,
        'on_add_article_page': True
    }

    return render(request, template, context)
