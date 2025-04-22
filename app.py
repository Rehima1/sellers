# app.py
from flask import Flask, render_template, request, jsonify
from scrap import run_scraper

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/run-scraper', methods=['POST'])
def api_scraper():
    search_query = request.form.get('search_query')
    max_sellers = int(request.form.get('max_sellers'))

    try:
        file_path = run_scraper(search_query, max_sellers)
        return jsonify({"message": f"✅ Scraping complete. File saved at {file_path}."})
    except Exception as e:
        return jsonify({"message": f"❌ Scraper failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)



