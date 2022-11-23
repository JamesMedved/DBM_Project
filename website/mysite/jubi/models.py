# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Disney(models.Model):
    show_id = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    date_added = models.TextField(blank=True, null=True)
    release_year = models.BigIntegerField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    listed_in = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disney'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Hulu(models.Model):
    show_id = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    date_added = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    duration = models.BigIntegerField(blank=True, null=True)
    listed_in = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hulu'


class Netflix(models.Model):
    show_id = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    date_added = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    listed_in = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'netflix'


class Prime(models.Model):
    show_id = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    date_added = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    listed_in = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prime'


class Streaming(models.Model):
    title = models.OneToOneField('Titles', models.DO_NOTHING, primary_key=True)
    provider = models.CharField(db_column='Provider', max_length=20)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=512, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.CharField(db_column='DateAdded', max_length=45, blank=True, null=True)  # Field name made lowercase.
    listedin = models.CharField(db_column='ListedIn', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'streaming'
        unique_together = (('title', 'provider'),)


class Titles(models.Model):
    title_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    cast = models.CharField(max_length=2048, blank=True, null=True)
    director = models.CharField(max_length=1024, blank=True, null=True)
    rating = models.CharField(max_length=45, blank=True, null=True)
    image = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titles'


class WatchLater(models.Model):
    title = models.OneToOneField(Titles, models.DO_NOTHING, primary_key=True)
    user_id = models.IntegerField()
    priority = models.IntegerField(blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watch_later'
        unique_together = (('title', 'user_id'),)


class Watched(models.Model):
    title = models.OneToOneField(Titles, models.DO_NOTHING, primary_key=True)
    user_id = models.IntegerField()
    rating = models.IntegerField(blank=True, null=True)
    finished = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watched'
        unique_together = (('title', 'user_id'),)