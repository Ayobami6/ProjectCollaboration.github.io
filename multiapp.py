import streamlit as st

class MultiApp:
    """ Combining Streamlit Application
    Usage:
      def foo():
          st.title("Hello Foo")
      def bar():
          st.title("Hello Bar")
      app = MultiApp()
      app.add_app("Foo", foo)
      app.add_app("Bar", bar)
      app.run()
Keeping application in seperate file
      import foo
      import bar
      app = MultiApp()
      app.add_app("Foo", foo.app)
      app.add_app("Bar", bar.app)
      app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """ Adding a new application
        Parameters
        ----------
        func:
           py function to render this app
        title:
           title of app at drop down side bar
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app = st.sidebar.radio(
            'Go To',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
