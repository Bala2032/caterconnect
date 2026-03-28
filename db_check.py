# Database Verification Script for CaterConnect
# Run this to check the database status

import sqlite3
import os

print("=" * 50)
print("CATERCONNECT DATABASE VERIFICATION")
print("=" * 50)

# Check if database exists
if os.path.exists("database.db"):
    print("\n✓ Database file exists: database.db")
else:
    print("\n✗ Database file NOT found!")
    exit()

# Connect to database
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Check workers table
print("\n--- WORKERS TABLE ---")
cur.execute("SELECT * FROM workers")
workers = cur.fetchall()

if workers:
    print(f"Total workers: {len(workers)}")
    print("\nWorker Records:")
    for w in workers:
        print(f"  ID: {w[0]}, Name: {w[1]}, Phone: {w[2]}, Area: {w[3]}, Experience: {w[4]}")
else:
    print("No workers registered yet.")

# Check bookings table
print("\n--- BOOKINGS TABLE ---")
cur.execute("SELECT * FROM bookings")
bookings = cur.fetchall()

if bookings:
    print(f"Total bookings: {len(bookings)}")
    print("\nBooking Records:")
    for b in bookings:
        print(f"  ID: {b[0]}, Client: {b[1]}, Phone: {b[2]}, Location: {b[3]}, Workers: {b[4]}, Date: {b[5]}")
else:
    print("No bookings yet.")

# Show table schema
print("\n--- TABLE SCHEMA ---")
cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='workers'")
print("Workers table:", cur.fetchone()[0])

cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='bookings'")
print("Bookings table:", cur.fetchone()[0])

conn.close()

print("\n" + "=" * 50)
print("Database verification complete!")
print("=" * 50)
