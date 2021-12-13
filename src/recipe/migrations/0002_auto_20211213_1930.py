# Generated by Django 3.0 on 2021-12-13 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.SharecipeUser'),
        ),
        migrations.AddField(
            model_name='review',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='recipextheme',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='recipextheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Theme'),
        ),
        migrations.AddField(
            model_name='recipexmethod',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Method'),
        ),
        migrations.AddField(
            model_name='recipexmethod',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='recipexingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipexingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.SharecipeUser'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipe.RecipeXIngredient', to='recipe.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='methods',
            field=models.ManyToManyField(through='recipe.RecipeXMethod', to='recipe.Method'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='themes',
            field=models.ManyToManyField(through='recipe.RecipeXTheme', to='recipe.Theme'),
        ),
    ]
