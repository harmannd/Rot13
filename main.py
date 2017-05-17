import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

low_alphabet = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y',
                'z']
cap_alphabet = ['A', 'B', 'C', 'D', 'E',
                'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y',
                'Z']

def rot13(str):
    str_list = list(str)
    for i in xrange(len(str_list)):
        if str_list[i] in low_alphabet or str_list[i] in cap_alphabet:
            if str_list[i] in cap_alphabet:
                alphabet = cap_alphabet
            else:
                alphabet = low_alphabet
            char_index = alphabet.index(str_list[i])
            new_index = char_index + 13
            if new_index > 25:
                new_index -= 26
            str_list[i] = alphabet[new_index]


    return ''.join(str_list)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **params):
        self.write(self.render_str(template, **params))

class MainPage(Handler):
    def get(self):
        self.render("base.html")

    def post(self):
        text = self.request.get('text')
        text = rot13(text)
        self.render("base.html", text = text)


app = webapp2.WSGIApplication([('/', MainPage)
                              ],
                                debug=True)
