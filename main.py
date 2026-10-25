
def check_status_code(status_code):
    if status_code in [200,201]:
        return "Test passed"
    else:
        return "Test failed"

result = check_status_code(201)
print(result)
result = check_status_code(400)
print(result)

def is_valid_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    return False

print(is_valid_email("test@example.com"))

def calculate_pass_rate(passed, total):
    if total == 0:
        return 0
    return (passed / total) * 100


print(calculate_pass_rate(8, 10))  # 80.0


def validate_response(response):
    if response["status_code"] != 200:
        return "Failed: incorrect status code"

    if "name" not in response:
        return "Failed: name is missing"

    if response["name"] == "":
        return "Failed: name is empty"

    return "Response is valid"


response = {
    "status_code": 200,
    "name": "Mick",
    "email": "Mick@example.com"
}

print(validate_response(response))



def validate_testresult(results):
    passed = 0
    failed = 0

    for result in results:
        if result == "passed":
            passed += 1
        elif result == "failed":
            failed += 1

    print("Passed:", passed)
    print("Failed:", failed)


results = ["passed", "failed", "passed", "passed", "failed"]
validate_testresult(results)

