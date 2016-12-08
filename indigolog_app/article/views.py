from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from .forms import ArticleForm

article_blueprint = Blueprint(
    'post_article',
    __name__,
    template_folder='templates'
)


@article_blueprint.route('/article', methods=['GET', 'POST'])
def article():
    form = ArticleForm()

    try:
        return render_template(
            'article.html',
            form=form
        )
    except TemplateNotFound:
        abort(404)

    # if request.method == 'POST':
    # pass
