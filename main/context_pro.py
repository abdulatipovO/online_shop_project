from .models import Category

def get_category_objects(request):
    categorys = Category.objects.all()
    return {"categorys":categorys}