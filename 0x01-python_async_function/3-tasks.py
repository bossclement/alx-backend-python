#!/usr/bin/env python3
"""
Module doc
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes a number max_delay
    Returns an asyncronous task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
