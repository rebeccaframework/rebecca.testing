.. contents::

.. image:: https://travis-ci.org/rebeccaframework/rebecca.testing.png?branch=master
   :target: https://travis-ci.org/rebeccaframework/rebecca.testing

Getting Started
===================

rebecca.testing provides test fixtures for `pyramid <http://www.pylonsproject.org>`_ application using `pytest <http://pytest.org>`_.

install
------------------

install with pip basically::

  $ pip install rebecca.testing


Usage
=====================

config fixture
-------------------------

config fixture provides dummy config with automatic setup and teardown::

  from pyramid import testing
  from rebecca.testing import config

  def test_it(config):
      config.include('your.app')
      from your.app.views import ClassUnderTheTest
      request = testing.DummyRequest()
      result = ClassUnserTheTest(request)

