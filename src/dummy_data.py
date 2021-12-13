from recipe.models import Recipe, Review, Ingredient, Method, Theme
from user.models import SharecipeUser


def refresh_data():
    SharecipeUser.objects.all().delete()
    Ingredient.objects.all().delete()
    Method.objects.all().delete()
    Theme.objects.all().delete()
    Recipe.objects.all().delete()
    Review.objects.all().delete()

    SharecipeUser.objects.create_user(
        username="junhcha",
        email="junhcha@example.com",
        address="dormitory",
        password="123123",
        is_staff=True,
    )
    SharecipeUser.objects.create_user(
        username="kmlee78",
        email="kmlee78@example.com",
        address="dormitory",
        password="123123",
    )
    SharecipeUser.objects.create_user(
        username="drg1021",
        email="drg1021@example.com",
        address="house",
        password="123123",
    )
    Ingredient.objects.bulk_create(
        [
            Ingredient(name="carrot"),
            Ingredient(name="onion"),
            Ingredient(name="potato"),
            Ingredient(name="tomato"),
            Ingredient(name="brocoli"),
            Ingredient(name="mushroom"),
            Ingredient(name="garlic"),
            Ingredient(name="leek"),
            Ingredient(name="cabbage"),
            Ingredient(name="bean"),
            Ingredient(name="kimchi"),
            Ingredient(name="egg"),
            Ingredient(name="beef"),
            Ingredient(name="chicken"),
            Ingredient(name="pork"),
            Ingredient(name="fish"),
            Ingredient(name="sausage"),
            Ingredient(name="salt"),
            Ingredient(name="sugar"),
            Ingredient(name="vinegar"),
            Ingredient(name="soy sauce"),
            Ingredient(name="oil"),
            Ingredient(name="pepper"),
            Ingredient(name="noodle"),
            Ingredient(name="rice"),
            Ingredient(name="bread"),
            Ingredient(name="flour"),
            Ingredient(name="water"),
            Ingredient(name="milk"),
            Ingredient(name="cheese"),
        ]
    )
    Method.objects.bulk_create(
        [
            Method(name="boil"),
            Method(name="roast"),
            Method(name="steam"),
            Method(name="fry"),
            Method(name="bake"),
            Method(name="dry"),
            Method(name="torch"),
            Method(name="freeze"),
        ]
    )
    Theme.objects.bulk_create(
        [
            Theme(name="party"),
            Theme(name="meal"),
            Theme(name="entertainment"),
            Theme(name="nurse"),
            Theme(name="snack"),
            Theme(name="supper"),
            Theme(name="exercise"),
            Theme(name="diet"),
        ]
    )

    author = SharecipeUser.objects.get(username="kmlee78")
    recipe = Recipe.objects.create(
        title="Cup Ramen",
        content="1. Boil water.\n 2. Pour water into Cup Ramen.\n 3. wait 4 minutes. \n 4. Eat.",
        author=author,
    )
    ingredients = Ingredient.objects.filter(name__in=["water"])
    methods = Method.objects.filter(name__in=["boil"])
    themes = Theme.objects.filter(name__in=["party"])
    recipe.ingredients.set(ingredients)
    recipe.methods.set(methods)
    recipe.themes.set(themes)

    author = SharecipeUser.objects.get(username="drg1021")
    recipe = Recipe.objects.get(title="Cup Ramen")
    Review.objects.create(
        title="Good!", content="I love Ramen.", author=author, recipe=recipe
    )
