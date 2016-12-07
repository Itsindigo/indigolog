from flask import Blueprint

article_blueprint = Blueprint(
    'post_article',
    __name__,
    template_folder='templates'
)


@article_blueprint.route('/article', methods=['GET', 'POST'])
def article():
    return 'Hello Article page.'
    # if request.method == 'POST':
    # pass
