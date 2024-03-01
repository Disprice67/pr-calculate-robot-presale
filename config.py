from os import getcwd, getenv, path

from dotenv import load_dotenv

load_dotenv()


# Main_dir
ROOT_DIR = path.join(getcwd(), 'SupportFile')
# Inbox_dirs
INPUT_DIR = path.join(ROOT_DIR, 'Входящий')
OUTPUT_DIR = path.join(ROOT_DIR, 'Исходящий')
ERROR_DIR = path.join(ROOT_DIR, 'Ошибки')
# Other_dir
STATUS_DIR = path.join(ROOT_DIR, 'Статусы')
PURCHASE_ONE_DIR = path.join(ROOT_DIR, 'Закупка')
PURCHASE_TWO_DIR = path.join(ROOT_DIR, 'Закупка2')
CATEGORIZER_ONE_DIR = path.join(ROOT_DIR, 'Категоризатор1')
CATEGORIZER_TWO_DIR = path.join(ROOT_DIR, 'Категоризатор2')
COLLISION_DIR = path.join(ROOT_DIR, 'Коллизии')
ARCH_DIR = path.join(ROOT_DIR, 'Свод')
ARCHIVE_DIR = path.join(ROOT_DIR, 'Архив')
SHASSI_DIR = path.join(ROOT_DIR, 'Шасси')
AGREEMENT_DIR = path.join(ROOT_DIR, 'Договора')
SAMPLE_DIR = path.join(ROOT_DIR, 'Шаблон')
# DB
DATABASE = getenv('DATABASE')
DATABASE_TEST = getenv('DATABASE_TEST')
# Ebay
API_KEY = getenv('API_KEY')
CERT_ID = getenv('CERT_ID')
DEV_ID = getenv('DEV_ID')
TOKEN = getenv('TOKEN')
# Sql
ARCHIVE = getenv('ARCHIVE')
SQL_ARCHIVE = getenv('SQL_ARCHIVE')
SQL_ARCHIVE_IN = getenv('SQL_ARCHIVE_IN')
SQL_ARCHIVE_OUT = getenv('SQL_ARCHIVE_OUT')
SQL_COLLISION = getenv('SQL_COLLISION')
SQL_CATEGORY = getenv('SQL_CATEGORY')
SQL_CORPUSE = getenv('SQL_CORPUSE')
SQL_CORPUSE_IN = getenv('SQL_CORPUSE_IN')
SQL_CORPUSE_OUT = getenv('SQL_CORPUSE_OUT') 
SQL_PURCHASE = getenv('SQL_PURCHASE')
SQL_PURCHASE_IN = getenv('SQL_PURCHASE_IN')
SQL_PURCHASE_OUT = getenv('SQL_PURCHASE_OUT')
SQL_PURCHASE_TWO = getenv('SQL_PURCHASE_TWO')
SQL_PURCHASE_TWO_IN = getenv('SQL_PURCHASE_TWO_IN')
SQL_PURCHASE_TWO_OUT = getenv('SQL_PURCHASE_TWO_OUT')
SQL_SHASSIS_IN = getenv('SQL_SHASSIS_IN')
# Credentials
USERNAME_OUTLOOK_CROC = getenv('USERNAME_OUTLOOK_CROC')
PASSWORD_OUTLOOK_CROC = getenv('PASSWORD_OUTLOOK_CROC')
# Mail_outlook
CONST_MAIL = getenv('CONST_MAIL')
# Parser
URL_HUAWEI = getenv('URL_HUAWEI')
USER_AGENT = getenv('USER_AGENT')
