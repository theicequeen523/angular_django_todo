# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Removing unique constraint on 'Recipe', fields ['time']
        db.delete_unique(u'public_recipe', ['time_id'])

        # Removing unique constraint on 'Recipe', fields ['instruction']
        db.delete_unique(u'public_recipe', ['instruction_id'])

        # Deleting model 'Time'
        db.delete_table(u'public_time')

        # Deleting model 'Instruction'
        db.delete_table(u'public_instruction')

        # Adding field 'Recipe.prep_time'
        db.add_column(u'public_recipe', 'prep_time',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Recipe.temp'
        db.add_column(u'public_recipe', 'temp',
                      self.gf('django.db.models.fields.CharField')(default='null', max_length=10),
                      keep_default=False)


        # Renaming column for 'Recipe.instruction' to match new field type.
        db.rename_column(u'public_recipe', 'instruction_id', 'instruction')
        # Changing field 'Recipe.instruction'
        db.alter_column(u'public_recipe', 'instruction',
                        self.gf('django.db.models.fields.CharField')(max_length=2000, null=True))
        # Removing index on 'Recipe', fields ['instruction']
        #db.delete_index(u'public_recipe', ['instruction_id'])


        # Renaming column for 'Recipe.time' to match new field type.
        db.rename_column(u'public_recipe', 'time_id', 'time')
        # Changing field 'Recipe.time'
        db.alter_column(u'public_recipe', 'time', self.gf('django.db.models.fields.CharField')(max_length=10))
        # Removing index on 'Recipe', fields ['time']
        #db.delete_index(u'public_recipe', ['time_id'])


    def backwards(self, orm):
        # Adding index on 'Recipe', fields ['time']
        db.create_index(u'public_recipe', ['time_id'])

        # Adding index on 'Recipe', fields ['instruction']
        db.create_index(u'public_recipe', ['instruction_id'])

        # Adding model 'Time'
        db.create_table(u'public_time', (
            ('sec', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hour', self.gf('django.db.models.fields.IntegerField')()),
            ('min', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'public', ['Time'])

        # Adding model 'Instruction'
        db.create_table(u'public_instruction', (
            ('temp', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('prep_time', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Time'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Instruction'])

        # Deleting field 'Recipe.prep_time'
        db.delete_column(u'public_recipe', 'prep_time')

        # Deleting field 'Recipe.temp'
        db.delete_column(u'public_recipe', 'temp')


        # Renaming column for 'Recipe.instruction' to match new field type.
        db.rename_column(u'public_recipe', 'instruction', 'instruction_id')
        # Changing field 'Recipe.instruction'
        db.alter_column(u'public_recipe', 'instruction_id',
                        self.gf('django.db.models.fields.related.OneToOneField')(default='default',
                                                                                 to=orm['public.Instruction'],
                                                                                 unique=True))
        # Adding unique constraint on 'Recipe', fields ['instruction']
        db.create_unique(u'public_recipe', ['instruction_id'])


        # Renaming column for 'Recipe.time' to match new field type.
        db.rename_column(u'public_recipe', 'time', 'time_id')
        # Changing field 'Recipe.time'
        db.alter_column(u'public_recipe', 'time_id',
                        self.gf('django.db.models.fields.related.OneToOneField')(to=orm['public.Time'], unique=True))
        # Adding unique constraint on 'Recipe', fields ['time']
        db.create_unique(u'public_recipe', ['time_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [],
                            {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')",
                     'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': (
            'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True',
                        'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True',
                                  'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'flavor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'glyc_index': (
            'django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': (
            'django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tag': (
            'django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Tag']", 'symmetrical': 'False'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        u'public.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'public.todo': {
            'Meta': {'object_name': 'Todo'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['public']