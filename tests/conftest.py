import pytest
import allure
import logging
import json
import datetime


def pytest_addoption(parser):
    parser.addoption(
        "--base_url", default="https://restful-booker.herokuapp.com/", help="base_url"
    )
    parser.addoption(
        "--status_code_200", default=200, help="Status code - 200"
    )
    parser.addoption(
        "--status_code_404", default=404, help="Status code - 404"
    )


# def url(request):
#     base_url = request.config.getoption("--base_url")
#     log_level = request.config.getoption("--log_level")
#
#     logger = logging.getLogger(request.node.name)
#     logger.setLevel(level=log_level)
#     logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))
#
#     allure.attach(
#         name=base_url.session_id,
#         body=json.dumps(base_url.capabilities),
#         attachment_type=allure.attachment_type.JSON)
#     base_url.log_level = log_level
#     base_url.logger = logger
#     base_url.test_name = request.node.name
#     logger.info("Tests %s started" % url)
#
#     def fin():
#         logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))
#
#     request.addfinalizer(fin)

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def status_code_200(request):
    return request.config.getoption("--status_code_200")


@pytest.fixture
def status_code_404(request):
    return request.config.getoption("--status_code_404")
