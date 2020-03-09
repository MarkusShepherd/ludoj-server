# -*- coding: utf-8 -*-

""" utils """

import logging
import os.path
import re
import timeit

from datetime import timezone
from functools import lru_cache
from pathlib import Path

from django.conf import settings
from pytility import normalize_space, parse_date

LOGGER = logging.getLogger(__name__)
VERSION_REGEX = re.compile(r"^\D*(.+)$")


def format_from_path(path):
    """ get file extension """
    try:
        _, ext = os.path.splitext(path)
        return ext.lower()[1:] if ext else None
    except Exception:
        pass
    return None


def serialize_date(date, tzinfo=None):
    """seralize a date into ISO format if possible"""
    parsed = parse_date(date, tzinfo)
    return parsed.strftime("%Y-%m-%dT%T%z") if parsed else str(date) if date else None


@lru_cache(maxsize=8)
def load_recommender(path, site="bgg"):
    """ load recommender from given path """
    if not path:
        return None
    try:
        if site == "bga":
            from board_game_recommender import BGARecommender

            return BGARecommender.load(path=path)
        from board_game_recommender import BGGRecommender

        return BGGRecommender.load(path=path)
    except Exception:
        LOGGER.exception("unable to load recommender model from <%s>", path)
    return None


@lru_cache(maxsize=8)
def pubsub_client():
    """ Google Cloud PubSub client """
    try:
        from google.cloud import pubsub

        return pubsub.PublisherClient()
    except Exception:
        LOGGER.exception("unable to initialise PubSub client")
    return None


def pubsub_push(
    message,
    project=settings.PUBSUB_QUEUE_PROJECT,
    topic=settings.PUBSUB_QUEUE_TOPIC,
    encoding="utf-8",
    **kwargs,
):
    """ publish message """

    if not project or not topic:
        return None

    client = pubsub_client()

    if client is None:
        return None

    if isinstance(message, str):
        message = message.encode(encoding)
    assert isinstance(message, bytes)

    # pylint: disable=no-member
    path = client.topic_path(project, topic)

    LOGGER.debug("pushing message %r to <%s>", message, path)

    try:
        return client.publish(topic=path, data=message, **kwargs)
    except Exception:
        LOGGER.exception("unable to send message %r", message)
    return None


@lru_cache(maxsize=8)
def model_updated_at(file_path=settings.MODEL_UPDATED_FILE):
    """ latest model update """
    try:
        with open(file_path) as file_obj:
            updated_at = file_obj.read()
        updated_at = normalize_space(updated_at)
        return parse_date(updated_at, tzinfo=timezone.utc)
    except Exception:
        pass
    return None


def parse_version(version):
    """Parse a version string to strip leading "v" etc."""
    version = normalize_space(version)
    if not version:
        return None
    match = VERSION_REGEX.match(version)
    return match.group(1) if match else None


@lru_cache(maxsize=8)
def project_version(file_path=settings.PROJECT_VERSION_FILE):
    """Project version."""
    try:
        with open(file_path) as file_obj:
            version = file_obj.read()
        return parse_version(version)
    except Exception:
        pass
    return None


def save_recommender_ranking(recommender, dst, similarity_model=False):
    """Save the rankings generated by a recommender to a CSV file."""

    LOGGER.info(
        "Saving <%s> ranking to <%s>...",
        recommender.similarity_model if similarity_model else recommender.model,
        dst,
    )

    recommendations = recommender.recommend(similarity_model=similarity_model)
    if "name" in recommendations.column_names():
        recommendations.remove_column("name", inplace=True)

    if similarity_model:
        recommendations = recommendations[recommendations["score"] > 0]

    recommendations.export_csv(str(dst))


def count_lines(path) -> int:
    """Return the line count of a given path."""
    with open(path) as file:
        return sum(1 for _ in file)


def count_files(path, glob=None) -> int:
    """Return the number of files and subdirectories in a given directory."""
    path = Path(path)
    files = path.glob(glob) if glob else path.iterdir()
    return sum(1 for _ in files)


class Timer:
    """ log execution time: with Timer('message'): do_something() """

    def __init__(self, message, logger=None):
        self.message = f'"{message}" execution time: %.1f ms'
        self.logger = logger
        self.start = None

    def __enter__(self):
        self.start = timeit.default_timer()
        return self

    def __exit__(self, *args, **kwargs):
        duration = 1000 * (timeit.default_timer() - self.start)
        if self.logger is None:
            print(self.message % duration)
        else:
            self.logger.info(self.message, duration)
