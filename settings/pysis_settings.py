# These are settings specific to PySIS project

import pysis.version
VERSION = pysis.version.version

# We need this to match our css classes
from django.contrib import messages
MESSAGE_TAGS = {
    messages.DEBUG : 'info',
    messages.INFO : 'info',
    messages.SUCCESS : 'done',
    messages.WARNING : 'warning',
    messages.ERROR : 'error',
}

GOOGLE_ANALYTICS_ID = "'UA-15662130-6'"

MY_PROFILE_LANDING_URL = '/myprofile/general/'
STUDENTS_LANDING_URL = '/students/browse/myclassmates/'

LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = MY_PROFILE_LANDING_URL
PASSWORD_CHANGE_URL = 'https://www.google.com/accounts/EditPasswd'

MAIN_MENU_LEFT = [

    # (Name, URL)
    ('Student Profiles', '/students/'),
    ('Attendance', '/attendance/'),
    ('Marks', '/marks/'),
    ('Library', '/library/'),
    ('Knowledge Base', 'http://kb.rmv.ac.in'),
    ('Institutional Repository', 'http://ir.rmv.ac.in'),
]

MAIN_MENU_RIGHT = [

    # (Name, URL)
    ('My Profile', MY_PROFILE_LANDING_URL),
    ('Vidyalaya Mail', 'http://mail.rmv.ac.in'),
]

MY_PROFILE_MENU = [

    # (Name, URL)
    ('General Details', '/myprofile/general/'),
    ('Personal Details', '/myprofile/personal/'),
    ('Family Details', '/myprofile/family/'),
    ('Contact Details', '/myprofile/contact/'),
    ('Education Details', '/myprofile/education/'),
    ('Misc Details', '/myprofile/misc/'),
]


STUDENTS_PROFILE_MENU = [

    # (Name, URL)
    ('My Classmates', '/students/browse/myclassmates/'),
    ('My Seniors', '/students/browse/myseniors/'),
    ('My Juniors', '/students/browse/myjuniors/'),
    ('', ''),
    ('Browse by Batch', '/students/browse/'),
    ('', ''),
    ('All Students', '/students/search/?q=all'),
]

STUDENTS_PROFILE_MENU_URLS =  [x[1] for x in STUDENTS_PROFILE_MENU]

# These fields determine who can see what.
# For the complete list of available fields, see myprofile.views.Profile

PROFILE_PREVIEW_FIELD_LIST = [
    'register_number',
    'course',
    'birth_day',
    'personal_email_id',
    'personal_contact_number',
    ]

PROFILE_FULLVIEW_FIELD_LIST = [
    'full_name',
    'register_number',
    'course',
    'birth_day',
    'personal_email_id',
    'personal_email_id2',
    'vidyalaya_email_id',
    'personal_contact_number',
    'personal_website',
    'orkut_profile_url',
    'facebook_profile_url',
    'linkedin_profile_url',
    ]

GENERAL_DETAILS_FIELD_LIST = [
    'first_name',
    'last_name',
    'register_number',
    'course',
    'year_of_joining',
    ]

PERSONAL_DETAILS_FIELD_LIST = [
    'gender',
    'blood_group',
    'date_of_birth',
    'actual_date_of_birth',
    ]

FAMILY_DETAILS_FIELD_LIST = [
    'father_name',
    'father_profession',
    'family_income',
    'religion',
    'caste',
    'reservation_category',
    ]

CONTACT_DETAILS_FIELD_LIST = [
    'personal_email_id',
    'personal_email_id2',
    'vidyalaya_email_id',
    'personal_contact_number',
    'personal_contact_number2',
    'emergency_contact_number',
    'present_address',
    'permanent_address',
    ]

EDUCATION_DETAILS_FIELD_LIST = [
    'sslc_passed_out_year',
    'sslc_percentage',
    'hslc_passed_out_year',
    'hslc_percentage',
    'hslc_major',
    'ug_passed_out_year',
    'ug_percentage',
    'ug_major',
    'pg_passed_out_year',
    'pg_percentage',
    'pg_major',
    'history_of_arrears',
    ]

MISC_DETAILS_FIELD_LIST = [
    'nss',
    'ncc',
    'sports',
    'hobbies',
    'personal_website',
    'orkut_profile_url',
    'facebook_profile_url',
    'linkedin_profile_url',
    ]
