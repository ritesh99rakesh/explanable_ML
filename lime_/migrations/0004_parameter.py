# Generated by Django 2.1.3 on 2018-12-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lime_', '0003_classname_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explainer', models.CharField(choices=[('LIME', 'LIME'), ('A-LIME', 'A-LIME')], max_length=10)),
                ('classifier', models.CharField(choices=[('Nearest Neighbour', 'Nearest Neighbour'), ('Linear SVM', 'Linear SVM'), ('RBF SVM', 'RBF SVM'), ('Gaussian Process', 'Gaussian Process'), ('Decision Tree', 'Decision Tree'), ('Random Forest', 'Random Forest'), ('Neural Net', 'Neural Net'), ('Naive Bayes', 'Naive Bayes'), ('AdaBoost', 'AdaBoost'), ('QDA', 'QDA')], max_length=50)),
                ('number_of_top_features', models.IntegerField()),
                ('example_number_explain', models.IntegerField()),
            ],
        ),
    ]
