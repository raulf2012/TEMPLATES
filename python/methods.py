

def get_matbench_dataset(
    dataset_name,
    fix_column_names=True,
    test_data='exclude',  # 'include', 'exclude', 'only'
    verbose=False,
    ):
    """Get matbench dataframe saved to pickle.

    I created the pickle files in matbench_save_data.ipynb

    Parameters
    ----------
    dataset_name : {}
        Name of dataset to load
    fix_column_names : {True or False}, default True
        Blah blah blah
    test_data : {'include' or 'exclude' or 'only'}, default exclude
        Controls how test data is handled. Can be included, excluded, or
        only the test data can be returned
    verbose : {True or False}, default False


    Returns
    -------
    DataFrame
        Returns the chosen matbench DataFrame


    """
    #| - get_matbench_dataset


    #  # DEV ------------------------------------------------------
    #  from matbench_ml.project_data import PROJECT_DATA
    #  from matbench_ml.project_methods import _process_test_data_df
    #
    #  # dataset_name='matbench_steels'
    #  dataset_name=dataset_name
    #
    #  fix_column_names=True
    #
    #  # test_data='include'
    #  # test_data='exclude'
    #  test_data='only'
    #
    #  verbose=False
    #  # DEV ------------------------------------------------------


    data_save_dir = os.path.join(
        PROJECT_DATA,
        'matbench_datasets')

    filename_i = dataset_name + '.pickle'
    filepath_i = os.path.join(data_save_dir, filename_i)
    path_i = filepath_i

    if verbose:
        print(path_i)

    with open(path_i, 'rb') as fle:
        df = pickle.load(fle)

    if fix_column_names:

        # Replacing spaces with underscores
        column_rename = dict()
        for col in df.columns:
            if ' ' in col:
                col_new = col.replace(' ', '_')
                column_rename[col] = col_new

        df.rename(columns=column_rename, inplace=True)

        # Fixing parenthesis (Not good for SQL)
        column_rename = dict()
        for col in df.columns:
            modify_col = False
            if '(' in col:
                col_new = col.replace('(', '_')
                modify_col = True
            if ')' in col:
                col_new = col_new.replace(')', '')
                modify_col = True
            if modify_col:
                column_rename[col] = col_new

        df.rename(columns=column_rename, inplace=True)

    # Process the dataframe w.r.t. test_data
    df = _process_test_data_df(df, dataset_name, test_data)

    return(df)
    #__|

