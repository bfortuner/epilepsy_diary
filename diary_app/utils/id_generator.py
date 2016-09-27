import uuid

USER_CHART_PREFIX = ""
USER_CHART_FILE_EXTENSION = "png"


def generate_random_filename(prefix, extension):
    return prefix + str(uuid.uuid4()).upper().replace('-', '') + extension


def generate_chart_image_filename():
    return generate_random_filename(
        USER_CHART_PREFIX, "." + USER_CHART_FILE_EXTENSION)
