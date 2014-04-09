# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting model 'Todo'
        db.delete_table(u'public_todo')

        # Adding model 'RecipeImage'
        db.create_table(u'public_recipeimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Recipe'])),
        ))
        db.send_create_signal(u'public', ['RecipeImage'])

        # Adding model 'IngredientImage'
        db.create_table(u'public_ingredientimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Ingredient'])),
        ))
        db.send_create_signal(u'public', ['IngredientImage'])

        # Deleting field 'Recipe.img'
        db.delete_column(u'public_recipe', 'img')

        # Deleting field 'Ingredient.img'
        db.delete_column(u'public_ingredient', 'img')


    def backwards(self, orm):
        # Adding model 'Todo'
        db.create_table(u'public_todo', (
            ('create_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Todo'])

        # Deleting model 'RecipeImage'
        db.delete_table(u'public_recipeimage')

        # Deleting model 'IngredientImage'
        db.delete_table(u'public_ingredientimage')

        # Adding field 'Recipe.img'
        db.add_column(u'public_recipe', 'img',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ingredient.img'
        db.add_column(u'public_ingredient', 'img',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'flavor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'glyc_index': (
            'django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': (
            'django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tag': (
            'django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Tag']", 'symmetrical': 'False'})
        },
        u'public.ingredientimage': {
            'Meta': {'object_name': 'IngredientImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Ingredient']"})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ManyToManyField', [],
                           {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'instruction': (
            'django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prep_time': (
            'django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'serv_size': (
            'django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [],
                    {'to': u"orm['public.Tag']", 'symmetrical': 'False'}),
            'temp': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'public.recipeimage': {
            'Meta': {'object_name': 'RecipeImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Recipe']"})
        },
        u'public.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['public']