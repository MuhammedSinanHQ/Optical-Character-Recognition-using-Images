from app import app
import os

if __name__ == '__main__':
    # Run the Flask app
    # Debug mode should only be enabled in development
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
