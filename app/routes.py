from datetime import datetime
from flask import Blueprint, render_template
import os
import sqlite3
import contextlib

bp = Blueprint("name", __name__, url_prefix="")
DB_FILE = os.environ.get("DB_FILE")

@bp.route('/')
def main(): 
    # Create a SQLite3 connection with the connection parameters
        # Create a cursor from the connection
        # Execute "SELECT id, name, start_datetime, end_datetime
        #          FROM appointments
        #          ORDER BY start_datetime;"
        # Fetch all of the records
    with sqlite3.connect(DB_FILE) as conn:
        with contextlib.closing(conn.cursor()) as select:
            sql = """
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                ORDER BY start_datetime
            """
            select.execute(sql)
            raw_rows = select.fetchall()
            rows=[]
            for raw_row in raw_rows:
                row=list(raw_row)
                row[2] = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                row[3] = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                rows.append(row)
                from pprint import pprint
            pprint(rows)    
        return render_template("main.html", rows=rows)