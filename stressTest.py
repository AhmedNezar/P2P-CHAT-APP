import subprocess
import threading
import time
import pandas as pd


logs = []


def stress_test(script, count, delay=0, stop_request=None):
    try:
        for i in range(count):
            if stop_request and stop_request.is_set():
                print(
                    f'Stopping thread for script {script} at iteration {i+1}')
                break  # Stop the thread if the stop_request event is set

            time.sleep(delay)

            start_time = round(time.time(), 2)  # start time

            process = subprocess.Popen(
                ['python', './' + script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            end_time = round(time.time(), 2)  # end time

            # execution time
            exec_time = round(end_time - start_time, 2)

            logs.append({
                'Script': script,
                'Thread': i + 1,
                'Execution Time (s)': exec_time
            })

            print(f'Successfully executed script {script} at iteration {i+1}')

    except Exception as e:
        print(f'Error in stress_test for script {script}: {e}')


# Added delay for peer.py
scripts = [('registry.py', 1, 0), ('peer.py', 100, 0)]
threads = []

try:
    for script, count, delay in scripts:
        stop_request = threading.Event()  # Create a stop event for each thread
        thread = threading.Thread(
            target=stress_test, args=(script, count, delay, stop_request))
        threads.append((thread, stop_request))

    # Start all threads
    for thread, _ in threads:
        thread.start()

    # Wait for all threads to finish
    for thread, _ in threads:
        thread.join()

except KeyboardInterrupt:
    print("Received KeyboardInterrupt. Stopping threads...")

    # Set the stop_request flag in case of a KeyboardInterrupt
    for _, stop_request in threads:
        stop_request.set()

    # Wait for all threads to finish after setting the stop_request flag
    for thread, _ in threads:
        thread.join()

finally:
    # Convert the logs list to a DataFrame
    logs_df = pd.DataFrame(logs)

    # Save the logs DataFrame to an Excel file
    logs_df.to_excel('stress_test.xlsx', index=False)

print("Script execution completed.")
