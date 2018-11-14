

def test_add_group(app, main_window,  group_name="Test group"):
    # main_window = app.open_app()
    old_list = app.group.get_group_list(main_window)
    app.group.add_new_group(main_window, "%s" % group_name)
    # new_list = app.group.get_group_list(main_window)
    old_list.append(group_name)
    # assert sorted(old_list) == sorted(new_list)
    # app.destroy(main_window)


def test_delete_group(app, group_name="Test group"):
    main_window = app.open_app()
    if len(app.group.get_group_list(main_window)) == 1:
        app.group.add_new_group(main_window, "%s" % group_name)
    old_list = app.group.get_group_list(main_window)
    app.group.delete_first_group(main_window)
    new_list = app.group.get_group_list(main_window)
    old_list.remove(group_name)
    assert sorted(old_list) == sorted(new_list)
    app.destroy(main_window)






    """
    def app(request):
        fixture = My_application()
        request.addfinalizer(fixture.destroy)
        return fixture
        
    def app(request):
        fixture = My_application()
        main_window = fixture.open_app()
        request.addfinalizer(lambda x: fixture.destroy(main_window))
        return fixture
        
    """