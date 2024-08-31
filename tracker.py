"""
This module contains a Telegram message tracker that calculates the time spent 
based on messages in a specific Telegram group.
"""

import asyncio
import re
from telethon.sync import TelegramClient


async def spent_tracker(name, month):
    """
    Tracks the amount of time spent based on messages in a Telegram channel.
    
    Args:
        name (str): The name of the sender in the Telegram group.
        month (str): The month to track the time spent.

    Returns:
        str: The total time spent in hours, formatted as a string with one decimal place.
    """
    api_id = 'YOUR API_ID'
    api_hash = 'YOUR API_HASH'

    time_spent = 0

    async with TelegramClient('session_name', api_id, api_hash) as client:
        async for message in client.iter_messages('https://t.me/+9gK63uD6IbViMDc6'):
            if message.sender and (message.post_author == name):

                month_pattern = rf'\b{month}\b'
                if re.findall(month_pattern, message.text, re.IGNORECASE):
                
                    hours_pattern = (
                        r'(?<=time spent)(\:|\s:).*?(?P<hours>(\d|\.|\,|\+)+)\s?(h)'
                    )
                    hours_match = re.finditer(hours_pattern, message.text, re.IGNORECASE)

                    for match in hours_match:
                        if match.group('hours'):
                            hours = float(re.match(
                                r'(?P<digit>(\d|\.)+)', match.group('hours')
                            ).group('digit'))
                            time_spent += hours

                    minutes_pattern = (
                        r'(?<=time spent)(\:|\s:).*?(?P<minutes>(\d|\.|\,|\+)+)\s?(m)'
                    )
                    minutes_match = re.finditer(minutes_pattern, message.text, re.IGNORECASE)

                    for match in minutes_match:
                        if match.group('minutes'):
                            minutes = (
                                float(re.match(r'\d+', match.group('minutes')).group()) / 60
                            )
                            time_spent += minutes

        return f'{time_spent:.1f}'
    

def sync_spent_tracker(name, month):
    """
    Synchronously runs the spent_tracker coroutine.

    Args:
        name (str): The name of the sender in the Telegram group.
        month (str): The month to track the time spent.

    Returns:
        str: The total time spent in hours, formatted as a string with one decimal place.
    """
    return asyncio.run(spent_tracker(name, month))
