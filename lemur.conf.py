import os.path
import random
import string
from celery.schedules import crontab

import base64

_basedir = os.path.abspath(os.path.dirname(__file__))

# See the Lemur docs (https://lemur.readthedocs.org) for more information on configuration

LOG_LEVEL = str(os.environ.get('LOG_LEVEL', 'DEBUG'))
LOG_FILE = str(os.environ.get('LOG_FILE', '/home/lemur/.lemur/lemur.log'))
LOG_JSON = True

CORS = os.environ.get("CORS") == "True"
debug = os.environ.get("DEBUG") == "True"


def get_random_secret(length):
    secret_key = ''.join(random.choice(string.ascii_uppercase) for x in range(round(length / 4)))
    secret_key = secret_key + ''.join(random.choice("~!@#$%^&*()_+") for x in range(round(length / 4)))
    secret_key = secret_key + ''.join(random.choice(string.ascii_lowercase) for x in range(round(length / 4)))
    return secret_key + ''.join(random.choice(string.digits) for x in range(round(length / 4)))


# This is the secret key used by Flask session management
SECRET_KEY = repr(os.environ.get('SECRET_KEY', get_random_secret(32).encode('utf8')))

# You should consider storing these separately from your config
LEMUR_TOKEN_SECRET = repr(os.environ.get('LEMUR_TOKEN_SECRET',
                                         base64.b64encode(get_random_secret(32).encode('utf8'))))
# This must match the key for whichever DB the container is using - this could be a dump of dev or test, or a unique key
LEMUR_ENCRYPTION_KEYS = repr(os.environ.get('LEMUR_ENCRYPTION_KEYS',
                                            base64.b64encode(get_random_secret(32).encode('utf8')).decode('utf8')))

REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}'
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'
CELERY_IMPORTS = ('lemur.common.celery')
CELERYBEAT_SCHEDULE = {
    # All tasks are disabled by default. Enable any tasks you wish to run.
    # 'fetch_all_pending_acme_certs': {
    #     'task': 'lemur.common.celery.fetch_all_pending_acme_certs',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(minute="*"),
    # },
    # 'remove_old_acme_certs': {
    #     'task': 'lemur.common.celery.remove_old_acme_certs',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour=8, minute=0, day_of_week=5),
    # },
    # 'clean_all_sources': {
    #     'task': 'lemur.common.celery.clean_all_sources',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour=5, minute=0, day_of_week=5),
    # },
    # 'sync_all_sources': {
    #     'task': 'lemur.common.celery.sync_all_sources',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour="*/2", minute=0),
    #     # this job is running 30min before endpoints_expire which deletes endpoints which were not updated
    # },
    # 'sync_source_destination': {
    #     'task': 'lemur.common.celery.sync_source_destination',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour="*/2", minute=15),
    # },
    # 'report_celery_last_success_metrics': {
    #     'task': 'lemur.common.celery.report_celery_last_success_metrics',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(minute="*"),
    # },
    # 'certificate_reissue': {
    #     'task': 'lemur.common.celery.certificate_reissue',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour=9, minute=0),
    # },
    # 'certificate_rotate': {
    #     'task': 'lemur.common.celery.certificate_rotate',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour=10, minute=0),
    # },
    # 'endpoints_expire': {
    #     'task': 'lemur.common.celery.endpoints_expire',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour="*/2", minute=30),
    #     # this job is running 30min after sync_all_sources which updates endpoints
    # },
    # 'get_all_zones': {
    #     'task': 'lemur.common.celery.get_all_zones',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(minute="*/30"),
    # },
    # 'check_revoked': {
    #     'task': 'lemur.common.celery.check_revoked',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour=10, minute=0),
    # }
    # 'enable_autorotate_for_certs_attached_to_endpoint': {
    #     'task': 'lemur.common.celery.enable_autorotate_for_certs_attached_to_endpoint',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour=10, minute=0),
    # }
    # 'notify_expirations': {
    #     'task': 'lemur.common.celery.notify_expirations',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour=10, minute=0),
    #  },
    # 'notify_authority_expirations': {
    #     'task': 'lemur.common.celery.notify_authority_expirations',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour=10, minute=0),
    # },
    # 'send_security_expiration_summary': {
    #     'task': 'lemur.common.celery.send_security_expiration_summary',
    #     'options': {
    #         'expires': 180
    #     },
    #     'schedule': crontab(hour=10, minute=0, day_of_week='mon-fri'),
    # }
}
CELERY_TIMEZONE = 'UTC'

SQLALCHEMY_ENABLE_FLASK_REPLICATED = False
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://lemur:lemur@localhost:5432/lemur')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_RECYCLE = 499
SQLALCHEMY_POOL_TIMEOUT = 20

LEMUR_EMAIL = 'lemur@example.com'
LEMUR_SECURITY_TEAM_EMAIL = ['security@example.com']
LEMUR_SECURITY_TEAM_EMAIL_INTERVALS = [15, 2]
LEMUR_DEFAULT_EXPIRATION_NOTIFICATION_INTERVALS = [30, 15, 2]
LEMUR_EMAIL_SENDER = 'smtp'

# mail configuration
# MAIL_SERVER = 'mail.example.com'

PUBLIC_CA_MAX_VALIDITY_DAYS = 397
DEFAULT_VALIDITY_DAYS = 365

LEMUR_OWNER_EMAIL_IN_SUBJECT = False

LEMUR_DEFAULT_COUNTRY = str(os.environ.get('LEMUR_DEFAULT_COUNTRY', 'US'))
LEMUR_DEFAULT_STATE = str(os.environ.get('LEMUR_DEFAULT_STATE', 'California'))
LEMUR_DEFAULT_LOCATION = str(os.environ.get('LEMUR_DEFAULT_LOCATION', 'Los Gatos'))
LEMUR_DEFAULT_ORGANIZATION = str(os.environ.get('LEMUR_DEFAULT_ORGANIZATION', 'Example, Inc.'))
LEMUR_DEFAULT_ORGANIZATIONAL_UNIT = str(os.environ.get('LEMUR_DEFAULT_ORGANIZATIONAL_UNIT', ''))

LEMUR_DEFAULT_AUTHORITY = str(os.environ.get('LEMUR_DEFAULT_AUTHORITY', 'ExampleCa'))

LEMUR_DEFAULT_ROLE = 'operator'

ACTIVE_PROVIDERS = []
METRIC_PROVIDERS = []

# Authority Settings - These will change depending on which authorities you are
# using
current_path = os.path.dirname(os.path.realpath(__file__))

# DNS Settings

# exclude logging missing SAN, since we can have certs from private CAs with only cn, prod parity
LOG_SSL_SUBJ_ALT_NAME_ERRORS = False

ACME_DNS_PROVIDER_TYPES = {"items": [
    {
        'name': 'route53',
        'requirements': [
            {
                'name': 'account_id',
                'type': 'int',
                'required': True,
                'helpMessage': 'AWS Account number'
            },
        ]
    },
    {
        'name': 'cloudflare',
        'requirements': [
            {
                'name': 'email',
                'type': 'str',
                'required': True,
                'helpMessage': 'Cloudflare Email'
            },
            {
                'name': 'key',
                'type': 'str',
                'required': True,
                'helpMessage': 'Cloudflare Key'
            },
        ]
    },
    {
        'name': 'dyn',
    },
    {
        'name': 'ultradns',
    },
]}

# Authority plugins which support revocation
SUPPORTED_REVOCATION_AUTHORITY_PLUGINS = ['acme-issuer']

CFSSL_URL ="http://cfssl:8888"
CFSSL_ROOT ="""-----BEGIN CERTIFICATE-----
MIICFDCCAbqgAwIBAgIUCt8+6XoqIk1sIF+4J4MZqa3IcK4wCgYIKoZIzj0EAwIw
ZzELMAkGA1UEBhMCSVQxETAPBgNVBAcTCEFjaXJlYWxlMRkwFwYDVQQKExBMdWNh
IFN0ZWNjYW5lbGxhMQwwCgYDVQQLEwNDU0QxHDAaBgNVBAMTE1BhcGVyRHJhZ29u
IFJvb3QgQ0EwIBcNMjQxMTA4MDMyMDAwWhgPMjA1NDExMDEwMzIwMDBaMGcxCzAJ
BgNVBAYTAklUMREwDwYDVQQHEwhBY2lyZWFsZTEZMBcGA1UEChMQTHVjYSBTdGVj
Y2FuZWxsYTEMMAoGA1UECxMDQ1NEMRwwGgYDVQQDExNQYXBlckRyYWdvbiBSb290
IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAECIwS0PGlszabh1Q9WoFrav9K
yqKKQmcGTFXyBYPIXHSz0MNcNUFLmktxG4K+3l6P8e6g+aPdG81/otsUeoDBL6NC
MEAwDgYDVR0PAQH/BAQDAgEGMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFL87
z1XHlMPG313RlYFDRYRgbr76MAoGCCqGSM49BAMCA0gAMEUCIDA8V2hVG0hkrTf4
47EwruspYYhzwaGNghEdwQzHEUm9AiEA3UyuSx0DXSCcs0L0tnVSHnET7nZMSwot
rZmgEKWy3mE=
-----END CERTIFICATE-----"""
CFSSL_INTERMEDIATE ="""-----BEGIN CERTIFICATE-----
MIIClDCCAjqgAwIBAgIUOU+6H/2wa1Ep6Epmhi23/ExTmGQwCgYIKoZIzj0EAwIw
ZzELMAkGA1UEBhMCSVQxETAPBgNVBAcTCEFjaXJlYWxlMRkwFwYDVQQKExBMdWNh
IFN0ZWNjYW5lbGxhMQwwCgYDVQQLEwNDU0QxHDAaBgNVBAMTE1BhcGVyRHJhZ29u
IFJvb3QgQ0EwHhcNMjQxMTA4MDMyMDAwWhcNMjcxMTA4MDMyMDAwWjBoMQswCQYD
VQQGEwJJVDERMA8GA1UEBxMIQWNpcmVhbGUxGTAXBgNVBAoTEEx1Y2EgU3RlY2Nh
bmVsbGExDDAKBgNVBAsTA0NTRDEdMBsGA1UEAxMUU3RlYyBJbnRlcm1lZGlhdGUg
Q0EwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAR2ZuAXmIYaD0vQDROJweIVL9Zy
QgciCacYfNrF+gxcBpGGTdnmGvRQRIrySu/QtFPQ/swygyP8h0aIZzBAdu4Uo4HC
MIG/MA4GA1UdDwEB/wQEAwIBBjASBgNVHRMBAf8ECDAGAQH/AgEAMB0GA1UdDgQW
BBT6T0ytWnX4XkYujzn1uLZEVslfbjAfBgNVHSMEGDAWgBS/O89Vx5TDxt9d0ZWB
Q0WEYG6++jAvBggrBgEFBQcBAQQjMCEwHwYIKwYBBQUHMAGGE2h0dHA6Ly8wLjAu
MC4wOjg4ODkwKAYDVR0fBCEwHzAdoBugGYYXaHR0cDovLzAuMC4wLjA6ODg4OC9j
cmwwCgYIKoZIzj0EAwIDSAAwRQIhANgFGSIqB3m+OMJ1Kz2q7fbbl68ByhpL0thC
9sv19Dm9AiAfyprzlo3MlKx4VsurUwa0uiSt+uN2Yo/7ITrqvAjRBQ==
-----END CERTIFICATE-----"""

