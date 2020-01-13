import pytest
import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import User


class TestBase(TestCase):

    def create_app(self):
        print("createapp")
        # pass in test configurations
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASSWORD'))+'@'+str(getenv('MYSQL_HOST'))+'/'+str(getenv('MYSQL_TEST_DB')))
        return app

    def setUp(self):
        """    
        Will be called before every test
        """
        print("setup")
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = User(first_name="admin1", last_name="admin1", email="admin@admin.com", password="admin2016")

        # create test non-admin user
        employee = User(first_name="user1", last_name="user1", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class testapp(TestBase):
    # Test that the about page is accessible without the user being logged in
    def test_view_aboutpage(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
    # Tests that the login page is accessible without the user being logged in
    def test_login_view(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)
    # Tests that the register page is accessible without the user being logged in
    def test_register_view(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)
    # Tests that the home page isn't accessible when the user is not logged in
    def test_user_view_home(self):
        target_url = url_for('home', user_id=1)
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)
    # Tests that the account page isn't accessible when the user is not logged in
    def test_user_view_account(self):
        target_url = url_for('account', user_id=1)
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)
    # Tests that a user can register to the app by adding themselves to the users database
    def test_user_Table(self):
        user = User(first_name="test", last_name="test2", email="testemail@gmail.com", password="testpassword")
        db.session.add(user)
        db.session.commit
        self.assertEqual(User.query.filter_by(email="testemail@gmail.com").first().first_name, "test")
