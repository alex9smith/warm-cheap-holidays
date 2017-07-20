from functions import *


app = Flask(__name__)

'''
#www and https redirects 
@app.before_request
def before_request():
	if request.url.startswith('http://'):
		url = request.url.replace('http://', 'https://', 1)
		code = 301
		return redirect(url, code=code)
	if request.url.startswith('https://www'):
		url = request.url.replace('https://www.', 'https://', 1)
		code = 301
		return redirect(url, code=code)
'''

@app.route('/')
def home_page():
	return render_template('index.html', title = 'Home')

@app.route('/api/v1.0/month/')
def list_months():
	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	return jsonify({'months': months})

@app.route('/api/v1.0/month/<string:month>/<string:low_temp>/<string:high_temp>')
def list_warm_countries(month, low_temp, high_temp):
	data = get_warm_countries(month, low_temp, high_temp)
	return jsonify(data)

@app.route('/form')
def test_form():
	return render_template('test-form.html', title = 'Form')

@app.route('/search', methods=['GET', 'POST'])
def search_handler():
	month = request.form['month']
	low = request.form['low']
	high = request.form['high']
	data = get_warm_countries(month, low, high)
	return render_template('results.html', title = 'Search', data = data)

@app.route('/p/<string:slug>')
def get_static_page(slug):
	return ''

@app.route('/robots.txt')
def robots_txt():
	response = make_response('User Agent:* \nDisallow: /api/\n\nSitemap: http://warmcheapholidays.com/sitemap.xml')
	response.headers["content-type"] = "text/plain"
	return response

@app.route('/sitemap.xml')
def sitemap():
	response = make_response(build_sitemap())
	response.headers["content-type"] = "application/xml"
	return response
	
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not Found'}), 404)
