import urllib.request
import urllib.parse
import json
import sys
import re


def validate_index_number(index_number):
    """Validate the index number format"""
    # Assuming index number should be numeric and have a specific length of 11 digits
    return bool(re.match(r'^\d{11}$', index_number))


def validate_student_name(name):
    """Validate the student name"""
    # Name should be at least 2 words, only letters and spaces
    return bool(re.match(r'^[A-Za-z\s]+$', name))


def check_results(index_number, student_name):
    """
    Check KNEC results for a given student

    Args:
        index_number (str): Student's examination index number
        student_name (str): Student's full name
    """
    if not validate_index_number(index_number):
        raise ValueError(
            "Invalid index number format. Please enter a valid numeric index number.")

    if not validate_student_name(student_name):
        raise ValueError(
            "Invalid name format. Please enter full name using only letters and spaces.")

    try:
        url = "https://results.knec.ac.ke/Home/CheckResults"
        data = {
            "indexNumber": index_number,
            "name": student_name
        }

        data = urllib.parse.urlencode(data).encode('utf-8')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Origin': 'https://results.knec.ac.ke',
            'Referer': 'https://results.knec.ac.ke/'
        }

        req = urllib.request.Request(url, data=data, headers=headers)

        with urllib.request.urlopen(req, timeout=30) as response:
            result = response.read().decode('utf-8')
            try:
                json_result = json.loads(result)
                print("\nResults:")
                print("=" * 50)
                for key, value in json_result.items():
                    print(f"{key}: {value}")
                print("=" * 50)
            except json.JSONDecodeError:
                print("\nRaw Response:")
                print("=" * 50)
                print(result)
                print("=" * 50)

    except urllib.error.URLError as e:
        print(
            f"Network Error: Unable to connect to KNEC servers. Please check your internet connection.\nDetails: {e}")
    except urllib.error.HTTPError as e:
        print(f"Server Error: The KNEC server returned an error (HTTP {
              e.code}).\nDetails: {e.reason}")
    except TimeoutError:
        print("Timeout Error: The server took too long to respond. Please try again later.")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        print("Please ensure your inputs are correct and try again.")


def main():
    print("\nKNEC Results Checker")
    print("=" * 50)
    print("Please enter the student details below:")

    while True:
        try:
            index_number = input("\nIndex Number: ").strip()
            student_name = input("Student's Full Name: ").strip()

            if not index_number or not student_name:
                print("Error: Both Index Number and Name are required!")
                continue

            check_results(index_number, student_name)
            break

        except ValueError as e:
            print(f"\nError: {str(e)}")
            retry = input("\nWould you like to try again? (y/n): ").lower()
            if retry != 'y':
                break


if __name__ == "__main__":
    main()
