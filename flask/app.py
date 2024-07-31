{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1f783cc2-1071-4900-8cda-31a8d6e034a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in /opt/conda/lib/python3.10/site-packages (3.0.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in /opt/conda/lib/python3.10/site-packages (from flask) (3.1.2)\n",
      "Requirement already satisfied: click>=8.1.3 in /opt/conda/lib/python3.10/site-packages (from flask) (8.1.3)\n",
      "Requirement already satisfied: blinker>=1.6.2 in /opt/conda/lib/python3.10/site-packages (from flask) (1.8.2)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in /opt/conda/lib/python3.10/site-packages (from flask) (3.0.3)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in /opt/conda/lib/python3.10/site-packages (from flask) (2.2.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /opt/conda/lib/python3.10/site-packages (from Jinja2>=3.1.2->flask) (2.1.1)\n",
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "# Install Flask if not already installed\n",
    "!pip install flask\n",
    "\n",
    "# Import necessary modules\n",
    "from flask import Flask\n",
    "from flask import request\n",
    "from IPython.display import display\n",
    "import threading\n",
    "\n",
    "# Create an instance of the Flask class\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Define a route for the homepage\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return \"Hello, World!\"\n",
    "\n",
    "# Define a function to run the Flask app\n",
    "def run_app():\n",
    "    app.run(port=5000, debug=True, use_reloader=False)\n",
    "\n",
    "# Start Flask app in a separate thread\n",
    "thread = threading.Thread(target=run_app)\n",
    "thread.start()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
