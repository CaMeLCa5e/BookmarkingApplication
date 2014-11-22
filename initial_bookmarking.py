* -*- coding utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db import models, migrations
import django.utils.timezone
import django.core.validators

class Migration(migrations.Migration):

	dependencies = [
		('auth', 'initial_bookmarking'),
		]

		operations = [ 
			migrations.CreateModel(
				name = 'MookmarkUser'
				fields = [
					('id', models.AutoField(verbose_name = 'ID', serialize = False, )
					('password', models.CharField(max_length = 128, verbose_name='password)')
					('last_login', models.DateTimeField(default = ))
					('is_superuser', models.BooleanField)
					('username', models.CharField)
					('first_name', models.CharField)
					('last_name', models.CharField)
					('email', models.email)
					('date_joined'models.DateTimeField)
					






				])]