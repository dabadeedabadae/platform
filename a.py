import streamlit as st

def main():
    st.title("Neuromorphic Algorithms and Chips Testing Platform")
    st.sidebar.title("Navigation")

    menu = ["Home", "Download Applications", "Compare Processors", "Test Algorithms", "Learn Algorithms"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        home()
    elif choice == "Download Applications":
        download_applications()
    elif choice == "Compare Processors":
        compare_processors()
    elif choice == "Test Algorithms":
        test_algorithms()
    elif choice == "Learn Algorithms":
        learn_algorithms()

def home():
    st.header("Welcome to the Neuromorphic Research Platform")
    st.write("This platform provides tools for testing neuromorphic algorithms and chips.")
    st.write("Navigate through the menu to explore applications, compare processors, and test your algorithms.")
    st.write("Created by Yelnur Ayagan")
    st.write("ISU-US-23-2a")

def download_applications():
    st.header("Download Applications")
    st.write("Below are the applications available for download:")

    apps = [
        {"name": "Speccy", "description": "Speccy is a convenient program that provides detailed information about the operation of the main components of the computer", "link": "#"},
    ]

    for app in apps:
        st.subheader(app["name"])
        st.write(app["description"])
        st.markdown(f"[Download]({app['link']})")

def compare_processors():
    st.header("Compare Neuromorphic Processors")

    st.write("Use the table below to compare different neuromorphic processors.")

    data = {
        "Processor": ["Processor A", "Processor B", "Processor C"],
        "Speed (GHz)": [3.2, 3.5, 2.9],
        "Power Consumption (W)": [95, 85, 110],
        "Number of Cores": [4, 8, 6]
    }

    st.table(data)

    st.write("Upload your own comparison data:")
    uploaded_file = st.file_uploader("Choose a file", type=["csv"])
    if uploaded_file:
        import pandas as pd
        user_data = pd.read_csv(uploaded_file)
        st.write(user_data)

def test_algorithms():
    st.header("Test Neuromorphic Algorithms")

    st.write("Input your algorithm's code and test its performance.")
    st.text_area("Enter your code here:", height=200, key="code_input")

    input_data = st.text_input("Enter input data for the algorithm:")
    if st.button("Run Algorithm"):
        try:
            exec_code(input_data)
        except Exception as e:
            st.error(f"Error: {e}")

def exec_code(input_data):
    code = st.session_state["code_input"]
    local_vars = {"input_data": input_data, "result": None}
    exec(code, {}, local_vars)
    result = local_vars.get("result", "No result defined")  # Default message if 'result' is not defined
    st.write("Execution Result:")
    st.write(local_vars)
    st.success(f"Result: {result}")

def learn_algorithms():
    st.header("Learn Algorithms")

    algorithms = {
        "Euclidean Algorithm": {
            "description": "The Euclidean algorithm calculates the greatest common divisor (GCD) of two integers.",
            "code": """
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
input_data = "48 18"  # Two numbers separated by space
nums = [int(x) for x in input_data.split()]
result = gcd(nums[0], nums[1])
output = f"GCD of {nums[0]} and {nums[1]}: {result}"
"""
        },
        "Binary Search": {
            "description": "Binary search efficiently finds the position of a target value in a sorted array.",
            "code": """
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
arr = sorted([int(x) for x in input_data.split()])  # Convert input data to sorted list
result = binary_search(arr, 10)  # Searching for 10 as an example
output = f"Index of target (10): {result}" if result != -1 else f"Value 10 not found"
"""
        },
        "Bubble Sort": {
            "description": "Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.",
            "code": """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
arr = [int(x) for x in input_data.split()]
result = bubble_sort(arr)
output = f"Sorted array: {result}"
"""
        }
    }

    selected_algorithm = st.selectbox("Choose an algorithm to learn:", list(algorithms.keys()))

    if selected_algorithm:
        algo = algorithms[selected_algorithm]
        st.subheader(selected_algorithm)
        st.write(algo["description"])
        st.code(algo["code"], language="python")


if __name__ == "__main__":
    main()
