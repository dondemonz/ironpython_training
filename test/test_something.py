from fixture.application import My_application
import pytest

@pytest.fixture
def app(request):
    fixture = My_application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    main_window = app.open_app()
    # old_list = app.get_group_list(main_window)
    app.add_new_group(main_window, "Test group")
    # new_list = app.get_group_list(main_window)
    # old_list.append("Test group")
    # assert sorted(old_list) == sorted(new_list)
    app.close_app(main_window)


def test_delete_group(app):
    main_window = app.open_app()
    if len(app.get_group_list(main_window)) == 1:
        app.add_new_group(main_window, "Test group")
    old_list = app.get_group_list(main_window)
    app.delete_first_group(main_window)
    new_list = app.get_group_list(main_window)
    old_list.remove("Test group")
    assert sorted(old_list) == sorted(new_list)
    app.close_app(main_window)




