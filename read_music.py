# read_music.py
# Reads all items from the DynamoDB Music table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3

from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Music"


def get_table():
    """Return a reference to the DynamoDB Music table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_music(music):
    title = music.get("Title", "Unknown Title")
    artist = music.get("Artist", "Unknown Year")
    seconds = music.get("Seconds", "No ratings")
    
    print(f"  Title             : {title}")
    print(f"  Artist           : {artist}")
    print(f"  Duration (sec)    : {seconds}")
    


def print_all_songs():
    """Scan the entire Music table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No songs found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} songs(s):\n")
    for song in items:
        print_music(song)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_songs()
    
if __name__ == "__main__":
    main()
