from __init__ import create_app
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
