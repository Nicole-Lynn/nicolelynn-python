from watch import parse


def test_parse_within_frame():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None


def test_parse_out_of_frame():
    assert parse("http://youtube.com/embed/xvFZjo5PgG0") == None
    assert parse("https://youtube.com/embed/xvFZjo5PgG0") == None
    assert parse("https://www.youtube.com/embed/xvFZjo5PgG0") == None
