from db_autotest.m_lib.m_utils.generate_tab_cols import GenerateTabCols


def script_generate_TabColsCode():
    print("Started Gen")
    GenerateTabCols.delete_prev_tables()
    GenerateTabCols.insert_tables()

    GenerateTabCols.delete_prev_rows()
    GenerateTabCols.insert_rows()   

    