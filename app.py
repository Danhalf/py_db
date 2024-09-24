# -*- coding: utf-8 -*-

from db.db_utils import connect_db, execute_schema
from ui.ui_utils import create_main_window

conn = connect_db('db/tech.db')
execute_schema(conn)

root = create_main_window(conn)

root.mainloop()