import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash

from app import app

Base = declarative_base()


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return 'Not recorded'
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class CustomerItem(Base):
    """The Customers"""
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    address_code = Column(String(50), nullable=False, unique=True)
    customer_code = Column(String(120), nullable=True)
    customer_name = Column(String(120), nullable=False)
    account_id = Column(String(120), nullable=True)
    account_name = Column(String(90), nullable=False)
    CustomerNote = Column(String(512), nullable=True)
    renewal_date = Column(DateTime(timezone=True))
    contract_type = Column(String(255), nullable=True)
    country_code = Column(String(10), nullable=True)
    CCGroup = Column(String(45), nullable=True)
    AgentStatus = Column(String(255), nullable=True)
    comments = Column(String(255), nullable=True)
    isDummy  = Column(Integer, nullable=True)
    SFDC = Column(String(255), nullable=True)
    customer_address = Column(String(255), nullable=True)
    #SupportTeam
    #FirstLineSupport



class CountryItem(Base):
    """Countries and Regions"""
    __tablename__ = 'customer_codes'
    code_id = Column(Integer, primary_key=True)
    code = Column(String(80), nullable=False, unique=True)
    country = Column(String(255))
    SupportRegion = Column(String(255))
    #category_id = Column(Integer, ForeignKey('category.category_id',
    #                                         ondelete='CASCADE'))



class CustomerCountry(Base):
    """The Customer Country View"""
    __tablename__ = 'customer_country'
    customer_id = Column(Integer, primary_key=True)
    address_code = Column(String(50), nullable=False, unique=True)
    customer_code = Column(String(120), nullable=True)
    customer_name = Column(String(120), nullable=False)
    account_id = Column(String(120), nullable=True)
    account_name = Column(String(90), nullable=False)
    CustomerNote = Column(String(512), nullable=True)
    renewal_date = Column(DateTime(timezone=True))
    contract_type = Column(String(255), nullable=True)
    country_code = Column(String(10), nullable=True)
    CCGroup = Column(String(45), nullable=True)
    AgentStatus = Column(String(255), nullable=True)
    comments = Column(String(255), nullable=True)
    isDummy  = Column(Integer, nullable=True)
    SFDC = Column(String(255), nullable=True)
    customer_address = Column(String(255), nullable=True)
    country = Column(String(255))
    SupportRegion = Column(String(255))

class User(Base):
    """User class - basic authentication"""
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(120))
    registered = Column(DateTime)
    # def __init__(self, username, password, email, can_edit, edit_note, can_create, is_admin):  # noqa
    #     self.username = username
    #     self.set_password(password)
    #     self.email = email
    #     self.registered_on = datetime.utcnow()
    #     self.can_edit = can_edit
    #     self.edit_note = edit_note
    #     self.can_create = can_create
    #     self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


engine = create_engine("mysql+mysqlconnector://jirauser:jirapass@10.54.1.195/jira_customers")
#create_engine("mysql+pymysql://jirauser:jirapass@10.54.1.195/jira_customers")
Base.metadata.create_all(engine)
