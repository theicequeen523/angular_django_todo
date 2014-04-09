# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'Recipe.instruction'
        db.add_column(u'public_recipe', 'instruction',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['public.Instruction'],
                                                                               unique=True),
                      keep_default=False)

        # Adding field 'Recipe.time'
        db.add_column(u'public_recipe', 'time',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['public.Time'],
                                                                               unique=True),
                      keep_default=False)

        # Removing M2M table for field time on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_time'))

        # Removing M2M table for field instruction on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_instruction'))


        # Changing field 'Tag.name'
        db.alter_column(u'public_tag', 'name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

    def backwards(self, orm):
        # Deleting field 'Recipe.instruction'
        db.delete_column(u'public_recipe', 'instruction_id')

        # Deleting field 'Recipe.time'
        db.delete_column(u'public_recipe', 'time_id')

        # Adding M2M table for field time on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_time')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('time', models.ForeignKey(orm[u'public.time'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'time_id'])

        # Adding M2M table for field instruction on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_instruction')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('instruction', models.ForeignKey(orm[u'public.instruction'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'instruction_id'])


        # Changing field 'Tag.name'
        db.alter_column(u'public_tag', 'name',
                        self.gf('django.db.models.fields.CharField')(default='default', max_length=30))

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
        u'public.instruction': {
            'Meta': {'object_name': 'Instruction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prep_time': (
            'django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'temp': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Time']"})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ingredient': ('django.db.models.fields.related.ManyToManyField', [],
                           {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'instruction': ('django.db.models.fields.related.OneToOneField', [],
                            {'to': u"orm['public.Instruction']", 'unique': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'serv_size': (
            'django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [],
                    {'to': u"orm['public.Tag']", 'symmetrical': 'False'}),
            'time': (
            'django.db.models.fields.related.OneToOneField', [], {'to': u"orm['public.Time']", 'unique': 'True'})
        },
        u'public.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'public.time': {
            'Meta': {'object_name': 'Time'},
            'hour': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min': ('django.db.models.fields.IntegerField', [], {}),
            'sec': ('django.db.models.fields.IntegerField', [], {})
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