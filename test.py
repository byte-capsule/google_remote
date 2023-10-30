from flask import Flask, render_template
import psutil
import os
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import time

app = Flask(__name__)

# Initialize lists to store memory usage data
timestamps = []
memory_usage = []

@app.route('/info')
def get_server_info():
    global timestamps, memory_usage

    # Get the total available system memory in bytes
    total_available_memory_bytes = psutil.virtual_memory().available

    # Get the total system memory in bytes
    total_memory_bytes = psutil.virtual_memory().total

    # Convert memory sizes to MB
    total_available_memory_mb = total_available_memory_bytes / 1048576  # 1 MB = 1048576 bytes
    total_memory_mb = total_memory_bytes / 1048576  # 1 MB = 1048576 bytes

    # Calculate memory usage percentage
    memory_usage_percent = (total_memory_bytes - total_available_memory_bytes) / total_memory_bytes * 100

    # Get the memory used by the current process (your Flask app)
    app_memory_info = psutil.Process(os.getpid()).memory_info()
    app_memory_mb = app_memory_info.rss / 1048576  # Convert RSS to MB

    # Get the server's IP address
    server_ip = os.environ.get("SERVER_IP")

    # Get the number of Gunicorn workers
    total_workers = int(os.environ.get("GUNICORN_WORKERS", 1))

    # Create a graph of memory usage over the last 10 minutes
    timestamps.append(time.strftime("%H:%M:%S"))
    memory_usage.append(app_memory_mb)

    if len(timestamps) > 20:
        timestamps.pop(0)
        memory_usage.pop(0)

    plt.figure(figsize=(10, 4))
    plt.plot(timestamps, memory_usage, marker='o')
    plt.title('Memory Usage Over Time (Last 10 minutes)')
    plt.xlabel('Time')
    plt.ylabel('Memory Usage (MB)')

    # Save the graph to a BytesIO object and encode it in base64
    img_data = BytesIO()
    plt.savefig(img_data, format="png")
    img_data.seek(0)
    graph_url = base64.b64encode(img_data.read()).decode()
    img_data.close()

    # Generate an HTML template with the graph
    graph_html = f'<img src="data:image/png;base64, {graph_url}" alt="Memory Usage Graph">'

    # Create a formatted HTML string with the graph
    server_info = f"""
    <html>
    <head>
        <title>Server Information</title>
        <meta http-equiv="refresh" content="3">
    </head>
    <body>
        <h1>Server Information</h1>
        <ul>
            <li><strong>Ram uses:</strong> {total_available_memory_mb:.2f}MB/{total_memory_mb:.2f}MB ({memory_usage_percent:.2f}%)</li>
            <li><strong>Ip address:</strong> {server_ip}</li>
            <li><strong>Total worker:</strong> {total_workers}</li>
            <li><strong>App memory usage:</strong> {app_memory_mb:.2f}MB</li>
        </ul>
        {graph_html}
    </body>
    </html>
    """

    return server_info

if __name__ == '__main__':
    app.run()
