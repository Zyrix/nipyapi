#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nipyapi` package."""

import pytest
from nipyapi import templates
from nipyapi import canvas


@pytest.fixture(scope="class")
def class_wrapper(request):
    def remove_test_templates():
        test_templates = ['nipyapi_testTemplate_00', 'nipyapi_testTemplate_01']
        for item in test_templates:
            details = templates.get_template_by_name(item)
            if details is not None:
                templates.delete_template(details['id'])

    def remove_test_pgs():
        pg_list = canvas.list_all_process_groups()
        test_pgs = [
            item for item in pg_list
            if 'nipyapi_test' in item['name']
        ]
        for pg in test_pgs:
            canvas.delete_process_group(
                pg['id'], pg['revision']
        )

    remove_test_templates()

    def cleanup():
        remove_test_templates()
        remove_test_pgs()
    request.addfinalizer(cleanup)


@pytest.mark.usefixtures('class_wrapper')
class TestTemplates(object):
    # Note that tests in this class are incremental
    # so consider order when adding new tests or modifying them
    def test_upload_template(self):
        r = templates.upload_template(
            pg_id=canvas.get_root_pg_id(),
            template_file='test_env_config/nipyapi_testTemplate_00.xml'
        )

    def test_get_templates_by_name(self):
        template = templates.get_template_by_name('nipyapi_testTemplate_00')
        assert template is not None

    def test_deploy_template(self):
        r = templates.deploy_template(
            canvas.get_root_pg_id(),
            templates.get_template_by_name('nipyapi_testTemplate_00')['id']
        )

    def test_get_snippet(self):
        from swagger_client import SnippetEntity
        t_id = canvas.get_process_group_by_name('nipyapi_test_0')['id']
        r = templates._make_pg_snippet(t_id)
        assert isinstance(r, SnippetEntity)

    def test_create_template(self):
        from swagger_client import TemplateEntity
        t_id = canvas.get_process_group_by_name('nipyapi_test_0')['id']
        r = templates.create_template(
            pg_id=t_id,
            name='nipyapi_testTemplate_01',
            desc='Nothing Here'
        )
        assert isinstance(r, TemplateEntity)

    def test_delete_template(self):
        template = templates.get_template_by_name('nipyapi_testTemplate_00')
        r = templates.delete_template(template['id'])
        assert r is None