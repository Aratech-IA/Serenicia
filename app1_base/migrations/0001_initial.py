# Generated by Django 3.2.13 on 2023-04-02 16:00

import app1_base.models
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import secrets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknow', max_length=20)),
                ('brand', models.CharField(default='unknow', max_length=20)),
                ('model', models.CharField(default='unknow', max_length=100)),
                ('serial_number', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('active_automatic', models.BooleanField(default=True)),
                ('ip', models.GenericIPAddressField(null=True)),
                ('port_onvif', models.IntegerField(default=80)),
                ('auth_type', models.CharField(choices=[('B', 'Basic'), ('D', 'Digest')], default='B', max_length=1)),
                ('username', models.CharField(blank=True, max_length=20)),
                ('password', models.CharField(blank=True, max_length=20)),
                ('stream', models.BooleanField(default=False, help_text='Check this box if you want to use the rtsp of the camera')),
                ('threshold', models.FloatField(default=0.9, validators=[django.core.validators.MinValueValidator(0.2), django.core.validators.MaxValueValidator(0.99)])),
                ('gap', models.IntegerField(default=95, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('max_width_rtime', models.IntegerField(default=320)),
                ('max_width_rtime_HD', models.IntegerField(default=1280)),
                ('reso', models.BooleanField(default=False)),
                ('width', models.IntegerField(default=1280)),
                ('height', models.IntegerField(default=720)),
                ('image_rotation', models.IntegerField(default=0)),
                ('pos_sensivity', models.IntegerField(default=30)),
                ('wait_for_set', models.BooleanField(default=True)),
                ('from_client', models.BooleanField(default=False, help_text='Define if the camera has been detected or not')),
                ('on_camera_LD', models.BooleanField(default=False)),
                ('on_camera_HD', models.BooleanField(default=False)),
                ('on_rec', models.BooleanField(default=False)),
                ('max_object_area_detection', models.IntegerField(default=100)),
                ('update', models.BooleanField(default=True)),
                ('change', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CameraSetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=256, verbose_name='Location')),
                ('room', models.CharField(max_length=150, verbose_name='Room')),
                ('ip_identification', models.GenericIPAddressField(protocol='IPv4', verbose_name='IP Identification')),
                ('mac_identification', models.CharField(max_length=17, verbose_name='Mac Identification')),
                ('state', models.CharField(choices=[('working', 'working'), ('in_progress_installing', 'in progress installing'), ('to_install', 'to install'), ('in_default', 'in default'), ('not_equipped', 'not equipped')], default='working', max_length=30, verbose_name='State')),
                ('video_quality', models.CharField(choices=[('380p', '380p'), ('480p', '480p'), ('720p', '720p'), ('1080p', '1080p'), ('unknown', 'unknown')], default='380p', max_length=10, verbose_name='Video Quality')),
            ],
            options={
                'verbose_name': 'Camera Setup',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_lieu', models.CharField(blank=True, max_length=200)),
                ('adress', models.CharField(blank=True, max_length=200)),
                ('cp', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('key', models.CharField(default=secrets.token_hex, max_length=200)),
                ('folder', models.CharField(default=secrets.token_urlsafe, max_length=200)),
                ('rec', models.BooleanField(default=False)),
                ('start_rec', models.DateTimeField(default=datetime.datetime(2500, 1, 1, 0, 0, tzinfo=utc))),
                ('change', models.BooleanField(default=False)),
                ('update_camera', models.BooleanField(default=False)),
                ('wait_before_detection', models.IntegerField(default=20)),
                ('wait_before_cancel_alert', models.DurationField(default=datetime.timedelta(seconds=600))),
                ('dataset_test', models.BooleanField(default=False)),
                ('space_allowed', models.IntegerField(default=1000)),
                ('image_panel_max_width', models.IntegerField(default=400)),
                ('image_panel_max_hight', models.IntegerField(default=400)),
                ('logo_perso', models.CharField(blank=True, max_length=20, null=True)),
                ('stop_thread', models.CharField(default=secrets.token_hex, max_length=200)),
                ('video_authorize', models.BooleanField(default=True)),
                ('token_video', models.CharField(default=secrets.token_urlsafe, max_length=200)),
                ('token_video_time', models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0))),
                ('time_zone', models.CharField(choices=[('Asia/Bangkok', 'Asia/Bangkok'), ('Europe/Amsterdam', 'Europe/Amsterdam'), ('Europe/Andorra', 'Europe/Andorra'), ('Europe/Astrakhan', 'Europe/Astrakhan'), ('Europe/Athens', 'Europe/Athens'), ('Europe/Belgrade', 'Europe/Belgrade'), ('Europe/Berlin', 'Europe/Berlin'), ('Europe/Bratislava', 'Europe/Bratislava'), ('Europe/Brussels', 'Europe/Brussels'), ('Europe/Bucharest', 'Europe/Bucharest'), ('Europe/Budapest', 'Europe/Budapest'), ('Europe/Busingen', 'Europe/Busingen'), ('Europe/Chisinau', 'Europe/Chisinau'), ('Europe/Copenhagen', 'Europe/Copenhagen'), ('Europe/Dublin', 'Europe/Dublin'), ('Europe/Gibraltar', 'Europe/Gibraltar'), ('Europe/Guernsey', 'Europe/Guernsey'), ('Europe/Helsinki', 'Europe/Helsinki'), ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'), ('Europe/Istanbul', 'Europe/Istanbul'), ('Europe/Jersey', 'Europe/Jersey'), ('Europe/Kaliningrad', 'Europe/Kaliningrad'), ('Europe/Kirov', 'Europe/Kirov'), ('Europe/Kyiv', 'Europe/Kyiv'), ('Europe/Lisbon', 'Europe/Lisbon'), ('Europe/Ljubljana', 'Europe/Ljubljana'), ('Europe/London', 'Europe/London'), ('Europe/Luxembourg', 'Europe/Luxembourg'), ('Europe/Madrid', 'Europe/Madrid'), ('Europe/Malta', 'Europe/Malta'), ('Europe/Mariehamn', 'Europe/Mariehamn'), ('Europe/Minsk', 'Europe/Minsk'), ('Europe/Monaco', 'Europe/Monaco'), ('Europe/Moscow', 'Europe/Moscow'), ('Europe/Oslo', 'Europe/Oslo'), ('Europe/Paris', 'Europe/Paris'), ('Europe/Podgorica', 'Europe/Podgorica'), ('Europe/Prague', 'Europe/Prague'), ('Europe/Riga', 'Europe/Riga'), ('Europe/Rome', 'Europe/Rome'), ('Europe/Samara', 'Europe/Samara'), ('Europe/San_Marino', 'Europe/San_Marino'), ('Europe/Sarajevo', 'Europe/Sarajevo'), ('Europe/Saratov', 'Europe/Saratov'), ('Europe/Simferopol', 'Europe/Simferopol'), ('Europe/Skopje', 'Europe/Skopje'), ('Europe/Sofia', 'Europe/Sofia'), ('Europe/Stockholm', 'Europe/Stockholm'), ('Europe/Tallinn', 'Europe/Tallinn'), ('Europe/Tirane', 'Europe/Tirane'), ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'), ('Europe/Vaduz', 'Europe/Vaduz'), ('Europe/Vatican', 'Europe/Vatican'), ('Europe/Vienna', 'Europe/Vienna'), ('Europe/Vilnius', 'Europe/Vilnius'), ('Europe/Volgograd', 'Europe/Volgograd'), ('Europe/Warsaw', 'Europe/Warsaw'), ('Europe/Zagreb', 'Europe/Zagreb'), ('Europe/Zurich', 'Europe/Zurich')], default='Europe/Paris', max_length=30)),
                ('actif', models.BooleanField(default=False)),
                ('external_key', models.CharField(default='no external', max_length=200)),
                ('room_number', models.IntegerField(blank=True, default=False, null=True)),
                ('type', models.CharField(choices=[('jo', 'serenicia'), ('se', 'security')], default='jo', max_length=2)),
                ('informations', models.TextField(blank=True, null=True)),
                ('shower', models.CharField(choices=[('no', 'Standard'), ('fi', 'Filter')], default='no', max_length=30)),
                ('helper', models.CharField(choices=[('no', 'No'), ('il', 'Integralift'), ('cr', 'Ceiling Rail')], default='no', max_length=30)),
                ('bed', models.CharField(choices=[('stand', 'Standard'), ('alzhei', 'Alzheimer'), ('xxl', 'XXL')], default='stand', max_length=20)),
                ('price', models.CharField(default='0', max_length=10, verbose_name='Price')),
                ('captch', models.BooleanField(default=False, help_text='Check if the room sensor is installed')),
                ('captsdb', models.BooleanField(default=False, help_text='Check if the bathroom sensor is installed')),
                ('alexa_device_id', models.CharField(default='not set up', max_length=250)),
                ('scan_camera', models.IntegerField(default=0, help_text='0 if you want a broadcast discovery of onvif camera, port number between 0 and 65000 if you want a full scan of area network')),
                ('scan', models.BooleanField(default=False, help_text='Check if you want a periodic scan of the network to find the camera')),
                ('automatic_launch_from_scan', models.BooleanField(default=True, help_text='Uncheck when client is only to scan and retrieve the URI')),
                ('tunnel_port', models.IntegerField(blank=True, default=app1_base.models.get_default_tunnel_port, null=True, unique=True, validators=[django.core.validators.MaxValueValidator(40999), django.core.validators.MinValueValidator(40000)])),
                ('reboot', models.BooleanField(default=False)),
                ('docker_version', models.FloatField(choices=[(1.0, 1.0), (1.1, 1.1), (1.13, 1.13), (1.2, 1.2), (1.3, 1.3), (1.4, 1.4), (1.5, 1.5), (1.6, 1.6), (2.0, 2.0), (2.1, 2.1), (2.2, 2.2), (2.3, 2.3), (2.4, 2.4)], default=1.2)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0))),
            ],
            options={
                'verbose_name': 'Residence',
                'ordering': ('cp',),
            },
        ),
        migrations.CreateModel(
            name='MachineID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=200, unique=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('future_user', models.CharField(blank=True, max_length=200, null=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(1999, 12, 31, 23, 51, tzinfo=utc))),
                ('tunnel_port', models.IntegerField(blank=True, default=app1_base.models.get_default_tunnel_port, null=True, unique=True, validators=[django.core.validators.MaxValueValidator(40999), django.core.validators.MinValueValidator(40000)])),
                ('reboot', models.BooleanField(default=False)),
                ('docker_version', models.FloatField(choices=[(1.0, 1.0), (1.1, 1.1), (1.13, 1.13), (1.2, 1.2), (1.3, 1.3), (1.4, 1.4), (1.5, 1.5), (1.6, 1.6), (2.0, 2.0), (2.1, 2.1), (2.2, 2.2), (2.3, 2.3), (2.4, 2.4)], default=2.0)),
                ('change', models.BooleanField(default=False)),
                ('multi_client', models.BooleanField(default=False, help_text='Check if the nnvission neural network server can accept more than one client. So you can change the association between clientand machine_ID in the admin')),
            ],
            options={
                'verbose_name_plural': 'Security Box',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_latitude', models.CharField(blank=True, max_length=50)),
                ('adress_longitude', models.CharField(blank=True, max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=app1_base.models.path_and_rename_profile, verbose_name='Photo')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')], verbose_name='Phone number')),
                ('civility', models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs')], default=' ', max_length=20, null=True, verbose_name='Civility')),
                ('telegram_token', models.CharField(default=app1_base.models.get_token_telegram, max_length=64)),
                ('subscribe_emails', models.BooleanField(default='True')),
                ('alert', models.BooleanField(default='True')),
                ('language', models.CharField(choices=[('en', 'English'), ('fr', 'French')], default='fr', max_length=2)),
                ('adress', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adress')),
                ('cp', models.CharField(blank=True, max_length=200, null=True, verbose_name='postcode')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='City')),
                ('department_number', models.CharField(blank=True, max_length=2, null=True, verbose_name='Department number')),
                ('phonetic_firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('phonetic_lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('video_ready', models.BooleanField(default=False)),
                ('welcoming_sent', models.BooleanField(default=False)),
                ('display_adress', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('mailer_daemon', models.BooleanField(default=False)),
                ('advanced_user', models.BooleanField(default=False)),
                ('portal_token', models.CharField(blank=True, max_length=200, null=True)),
                ('email_0', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('email_1', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('email_2', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('email_3', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('email_4', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('email_5', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('email_6', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('email_7', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('email_8', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('email_9', models.CharField(blank=True, max_length=30, validators=[django.core.validators.EmailValidator])),
                ('phone_number_0', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('phone_number_1', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('phone_number_2', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('phone_number_3', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('phone_number_4', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('phone_number_5', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('phone_number_6', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('phone_number_7', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('phone_number_8', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('phone_number_9', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:                                            '+999999999'. Up to 15 digits allowed.", regex='^[\\+\\d]\\d{9,11}$')])),
                ('tracking_number', models.CharField(blank=True, default='', max_length=30)),
                ('tracking_site', models.URLField(blank=True, default='')),
                ('created_by', models.CharField(default='admin', max_length=30)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1_base.client')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TimelineConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(choices=[('car', 'Car'), ('person', 'Person'), ('cat', 'Cat'), ('dog', 'Dog')], max_length=10)),
                ('inactivity_time', models.PositiveIntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='UpdateId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(default=0)),
                ('already_call', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
            ],
            options={
                'verbose_name': 'User',
                'ordering': ['last_name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Telegram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(null=True)),
                ('chat_id_char', models.CharField(default=None, max_length=64, null=True)),
                ('name', models.CharField(default='unknow', max_length=64)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_base.profile')),
            ],
        ),
        migrations.CreateModel(
            name='SubSector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('is_UP', models.BooleanField(default=False)),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1_base.sector')),
            ],
            options={
                'verbose_name': 'Sub sector',
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(default='detect', max_length=100)),
                ('video', models.CharField(default='None', max_length=100)),
                ('video_time', models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0))),
                ('time', models.DateTimeField(auto_now=True)),
                ('brut', models.TextField(default='')),
                ('alert', models.BooleanField(default=False)),
                ('correction', models.BooleanField(default=False)),
                ('force_send', models.BooleanField(default=False)),
                ('face_check', models.BooleanField(default=False)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_base.camera')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileSecurity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ManyToManyField(blank=True, help_text='Select the residence you want to access the interface <br>', to='app1_base.Client')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ManyToManyField(blank=True, help_text='Select the residence you want to have the warnings <br>', to='app1_base.Client')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_all_new_msg', models.BooleanField(default=True, verbose_name='Receive incoming message notification')),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1_base.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_object', models.CharField(default='', max_length=20)),
                ('result_prob', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('result_loc1', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('result_loc2', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('result_loc3', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('result_loc4', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('result_option1', models.CharField(default='normal', max_length=20)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_base.result')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='machine_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1_base.machineid'),
        ),
        migrations.AddField(
            model_name='client',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1_base.subsector'),
        ),
        migrations.AddField(
            model_name='camera',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_base.client'),
        ),
        migrations.CreateModel(
            name='AlertStuffsChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuffs', models.CharField(max_length=100, unique=True)),
                ('client', models.ManyToManyField(to='app1_base.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Alert_when',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what', models.CharField(choices=[('mail', 'mail'), ('sms', 'sms'), ('telegram', 'telegram'), ('mass_alarm', 'mass_alarm'), ('call', 'call'), ('alarm', 'alarm'), ('adam', 'adam'), ('patrol', 'patrol')], max_length=10)),
                ('action', models.IntegerField(default=1)),
                ('stuffs', models.IntegerField(default=1)),
                ('when', models.DateTimeField(auto_now=True)),
                ('who', models.CharField(blank=True, max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_base.client')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('action', models.CharField(default='', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_base.client')),
            ],
        ),
        migrations.CreateModel(
            name='CameraUri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.BooleanField(default=False)),
                ('index_uri', models.IntegerField(default=0)),
                ('http', models.URLField(blank=True, default='http://0.0.0.0')),
                ('rtsp', models.CharField(blank=True, default='rtsp://0.0.0.0', max_length=200, validators=[django.core.validators.URLValidator(schemes=('rtsp',))])),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_base.camera')),
            ],
            options={
                'unique_together': {('camera', 'index_uri')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='camera',
            unique_together={('client', 'serial_number'), ('client', 'ip')},
        ),
        migrations.CreateModel(
            name='Alert_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed', models.CharField(choices=[('mail', 'mail'), ('sms', 'sms'), ('telegram', 'telegram'), ('mass_alarm', 'mass_alarm'), ('call', 'call'), ('alarm', 'alarm'), ('adam', 'adam'), ('patrol', 'patrol')], max_length=10)),
                ('priority', models.IntegerField(default=1)),
                ('delay', models.DurationField(default=datetime.timedelta(0))),
                ('resent', models.DurationField(default=datetime.timedelta(seconds=300))),
                ('post_wait', models.DurationField(default=datetime.timedelta(seconds=60))),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_base.client')),
            ],
            options={
                'unique_together': {('client', 'allowed')},
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actions_char', models.CharField(choices=[('appear', 'appear'), ('disappear', 'disappear'), ('present', 'present')], default='present', max_length=100)),
                ('stuffs', models.IntegerField(choices=[(1, 'person'), (2, 'bicycle'), (3, 'car'), (4, 'motorbike'), (5, 'cat'), (6, 'dog'), (7, 'aeroplane'), (8, 'bus'), (9, 'train'), (10, 'truck'), (11, 'boat'), (12, 'bird'), (13, 'backpack'), (14, 'umbrella'), (15, 'chair'), (16, 'sofa'), (17, 'tvmonitor'), (18, 'laptop'), (19, 'mouse'), (20, 'keyboard'), (21, 'book'), (22, 'clock'), (23, 'face'), (24, 'vehicle'), (25, 'falling'), (26, 'masque'), (27, 'incorrect_mask'), (28, 'no_mask'), (29, 'toothbrush')], default=1)),
                ('actions', models.IntegerField(choices=[(1, 'appear'), (2, 'disappear'), (3, 'present')], default=1)),
                ('mail', models.BooleanField(default=True)),
                ('sms', models.BooleanField(default=False)),
                ('telegram', models.BooleanField(default=False)),
                ('call', models.BooleanField(default=False)),
                ('alarm', models.BooleanField(default=False)),
                ('mass_alarm', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('when', models.DateTimeField(default=datetime.datetime(1999, 12, 31, 23, 51, tzinfo=utc))),
                ('last', models.DateTimeField(default=datetime.datetime(1999, 12, 31, 23, 51, tzinfo=utc))),
                ('key', models.CharField(blank=True, default='', max_length=10)),
                ('img_name', models.CharField(blank=True, default='', max_length=100)),
                ('camera', models.ManyToManyField(blank=True, to='app1_base.Camera')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1_base.client')),
                ('stuffs_char_foreign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1_base.alertstuffschoice')),
            ],
            options={
                'unique_together': {('client', 'stuffs_char_foreign', 'actions_char')},
            },
        ),
    ]
