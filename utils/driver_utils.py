from botasaurus_driver import Driver


def get_driver(stealth: bool = True, user_agent: str = "desktop") -> Driver:
    """
    Returns a configured Botasaurus driver instance with common defaults.
    Use this instead of creating Driver() directly in scrapers.
    """
    return Driver(stealth=stealth, user_agent=user_agent)