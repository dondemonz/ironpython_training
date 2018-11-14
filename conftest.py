from fixture.application import My_application
import pytest

@pytest.fixture()
def app(request):
    fixture = My_application()
    main_window = fixture.open_app()
    request.addfinalizer(lambda x: fixture.destroy(main_window))
    return fixture