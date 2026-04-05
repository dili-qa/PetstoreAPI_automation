from utils.logger import get_logger

logger = get_logger("BDD")

def before_all(context):
    logger.info("=== Test Execution Started ===")

def after_all(context):
    logger.info("=== Test Execution Completed ===")

def before_scenario(context, scenario):
    logger.info(f"Starting Scenario: {scenario.name}")

def after_scenario(context, scenario):
    logger.info(f"Finished Scenario: {scenario.name}")