from app import app, models
from models import *
from sqlalchemy.orm import sessionmaker

DBsession = sessionmaker(bind=engine)
session = DBsession()


def getCustomerCountCountry(country, count):
    """Return count of product for specific category"""
    customers = session.query(CustomerCountry).filter(CustomerCountry.country == country).limit(count)
    return customers

def getCustomerCountRegion(region, count):
    """Return count of product for specific category"""
    customers = session.query(CustomerCountry).filter(CustomerCountry.SupportRegion == region).limit(count)
    return customers

def getCustomerByRegion(region):
    """Return count of product for specific category"""
    customers = session.query(CustomerCountry).filter(CustomerCountry.SupportRegion == region).all()
    return customers

def getCustomerByCountry(country):
    """Return count of product for specific category"""
    customers = session.query(CustomerCountry).filter(CustomerCountry.country == country).all()
    return customers

def getCountries():
    """Return all the categories as objects"""
    countries = session.query(CountryItem).all()
    return countries

def getRegions():
    regions = session.query(CountryItem).group_by(CountryItem.SupportRegion).distinct(CountryItem.SupportRegion).all()
    return regions

def getCountriesByRegion(region):
    countries = session.query(CountryItem).filter(CountryItem.SupportRegion == region).all()
    return countries

def countCustomersByRegion(region):
    """Return a count of the number of items in the category"""
    print region
    count = session.query(CustomerCountry).filter(CustomerCountry.SupportRegion == region).count()
    return count

def countCustomersByCountry(name):
    """Return a count of the number of items in the category"""
    count = session.query(CustomerCountry).filter(CustomerCountry.country == name).count()
    return count


def getProductOwner(name):
    """Return the user_id for the product to determine owner"""
    product = session.query(ProductItem)\
        .filter(ProductItem.product_name == name).first()
    return product.user_id


def checkLogin(name, password):
    """Checks for valid user, if fails handles empty value or
    mismatched creds"""
    user = session.query(User).filter(User.username == name).first()
    if user is None:
        return False
    return models.User.check_password(user, password)


def userExists(name):
    return session.query(User).filter(User.username == name).first()  # noqa
