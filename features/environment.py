from utils.logger import get_logger

logger = get_logger("BDD")


def before_all(context):
    logger.info("=== Test Execution Started ===")


def before_scenario(context, scenario):
    context.response = None
    context.payload = None


def after_scenario(context, scenario):
    logger.info(f"Finished Scenario: {scenario.name}")


def after_all(context):
    logger.info("=== Test Execution Completed ===")