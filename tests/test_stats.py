from fritz import FritzStats
import pandas as pd


def test_missing_folder():
    fritz = FritzStats("missing_folder", "some_title")
    assert fritz.get_downtime().empty


def test_x():
    fritz = FritzStats("tests/test_log_files", "some_title")
    downtime_df = fritz.get_downtime()

    # num rows
    assert downtime_df.shape[0] == 91

    expected_df = pd.read_pickle("tests/expected_df.pkl")
    assert downtime_df.equals(expected_df)