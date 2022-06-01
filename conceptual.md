### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is used for web development and emphasizes code readability. Javascript is mainly used for dynamic front-end and back-end development with emphasis on the client facing side .

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  use .get("potentially_missing_key", "message_to-send") method
  use .setdefault("potentially_missing_key", "new value")

- What is a unit test?
tests individual components of an app

- What is an integration test?
tests whether components of the app work together 


- What is the role of web application framework, like Flask?
provides a standard whay to build and deploy web apps  


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  use parameter in a route when sending user to specific resource. Use URL query params when results are filtered or sorted

- How do you collect data from a URL placeholder parameter using Flask?
use variables such  as: @app.route("jerseynumber/<number>") and then defining it in the route  def jerseynumber(number) or use  request.args["number"]


- How do you collect data from the query string using Flask?
add methods=["GET"] to route and use request.args

- How do you collect data from the body of the request using Flask?
request.whatevercollectingdatafrom

- What is a cookie and what kinds of things are they commonly used for?
cookies are temporarily stored data that is used to track data relevant to user experience

- What is the session object in Flask?
Used to track session data; is reset  when browser is closed  or  cookies are  removed

- What does Flask's `jsonify()` do?
returns JSON data
