def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(text="qqqqqqqqq")
    app.session.logout()
