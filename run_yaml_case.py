# -*- coding: utf-8 -*-

import yaml
from conftest import logger

ActionsMap = dict()


def load_and_execute_test_cases(path):
    def logging_setp_info(inner_step):
        for key in inner_step:
            if key == "step_name":
                continue
            logger.info(f"\t\t-- case {key}: {step[key]}")

    def get_project_action_map(path):
        pass  # 待补充

    with open(path, mode='r', encoding='utf-8') as file:
        test_cases = yaml.safe_load(file)

    for case in test_cases:
        logger.info(f"Executing test case: {case['test_name']}")

        # 执行setup步骤
        for step in case.get('setup', []):
            if step:
                logger.info(f"\t-- case setup: {step['step_name']}")
                logging_setp_info(step)
                execute_step(step)

        # 执行测试步骤
        for step in case.get('steps', []):
            if step:
                logger.info(f"\t-- case step: {step['step_name']}")
                logging_setp_info(step)
                execute_step(step)

        # 执行teardown步骤
        for step in case.get('teardown', []):
            if step:
                logger.info(f"\t-- case teardown: {step['step_name']}")
                logging_setp_info(step)
                execute_step(step)


def execute_step(step_data):
    pass


if __name__ == "__main__":
    load_and_execute_test_cases(r"test_collections/suites_project_b/suite_checklist/test_case_1.yaml")
