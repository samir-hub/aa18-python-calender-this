from datetime import datetime, timedelta
from flask import Blueprint, redirect, render_template, url_for
import os
import sqlite3
import contextlib

bp = Blueprint("main", __name__, url_prefix="")
DB_FILE = os.environ.get("DB_FILE")

@bp.route("/")
def main():
    with sqlite3.connect(DB_FILE) as conn:
        with contextlib.closing(conn.cursor()) as select:
            sql = """
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                ORDER BY start_datetime
            """
            select.execute(sql)
            raw_rows = select.fetchall()
            rows = []
            for raw_row in raw_rows:
                row = list(raw_row)
                row[2] = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                row[3] = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                rows.append(row)
            from pprint import pprint
            pprint(rows)
        return render_template("main.html", rows=rows)