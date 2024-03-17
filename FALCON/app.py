import falcon
import os

class StaticResource:
    def on_get(self, req, resp, file_name=None):
        if file_name:
            try:
                with open(os.path.join('Falcon', 'static', file_name), 'rb') as f:
                    resp.data = f.read()
                
                # Set content type based on file extension
                if file_name.endswith('.html'):
                    resp.content_type = falcon.MEDIA_HTML

            except FileNotFoundError:
                resp.status = falcon.HTTP_404
                resp.text = "File not found"
        else:
            try:
                with open(os.path.join('Falcon', 'static', 'index.html'), 'rb') as f:
                    resp.data = f.read()
                resp.content_type = falcon.MEDIA_HTML
            except FileNotFoundError:
                resp.status = falcon.HTTP_404
                resp.text = "Index file not found"

    def on_post(self, req, resp):
        name = req.get_param('name')
        message = req.get_param('message')
        if name and message:
            output_message = f"{name} : {message}\n"
            with open('output.txt', 'a') as f:
                f.write(output_message)
            resp.text = f"<p>Message received: {output_message}</p>"
        else:
            resp.text = "<p>Please fill out both fields.</p>"

# Create Falcon API instance
app = falcon.API()

# Map the static route to the StaticResource class
app.add_route('/static/{file_name}', StaticResource())

# Default route to serve index.html
app.add_route('/', StaticResource())

# Run Falcon app using the WSGI server
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    print('Serving on http://127.0.0.1:8000')
    httpd.serve_forever()
