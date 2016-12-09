from flask import Blueprint, render_template, abort, request, flash, url_for, redirect
from indigolog_app import db
from jinja2 import TemplateNotFound
from .forms import ArticleForm
from .model import Article

article_blueprint = Blueprint(
    'post_article',
    __name__,
    template_folder='templates'
)


@article_blueprint.route('/article', methods=['GET', 'POST'])
def article():
    form = ArticleForm()
    if request.method == 'POST':
        blog = Article(title=form.data['title'])
        db.session.add(blog)
        db.session.commit()
        # flash(gettext('Your post is now live!'))
        return redirect(url_for('main.index'))

    try:
        return render_template(
            'article.html',
            form=form
        )
    except TemplateNotFound:
        abort(404)
