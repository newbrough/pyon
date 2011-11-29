#!/usr/bin/env python

__author__ = 'Michael Meisinger'

from unittest import SkipTest

from pyon.container.apps import AppManager
from pyon.core.path import resolve
from pyon.service.service import BaseService
from pyon.util.int_test import IonIntegrationTestCase

class FakeContainer(object):
    def __init__(self):
        self.id = "containerid"
        self.node = None

class SampleProcess(BaseService):
    name = 'sample'
    dependencies = []

class TestAppManager(IonIntegrationTestCase):

    def test_appmanager_iso(self):
        fakecc = FakeContainer()
        am = AppManager(fakecc)
        self.assertTrue(hasattr(fakecc, "start_rel_from_url"))
        am.start()
        am.stop()

    def test_appmanager(self):
        with self.container() as cc:
            am = cc.app_manager
            filename = "res/deploy/examples/hello.yml"
            success = am.start_rel_from_url(filename)
            self.assertTrue(success)
            self.assertTrue('hello' in cc.proc_manager.procs_by_name)
            self.assertTrue('hello1' in cc.proc_manager.procs_by_name)