def create_job_request():
    """
  This function captures employee job request information.
  """
    # Employee Information
    employee_name = input("Enter your name: ")
    employee_id = input("Enter your employee ID: ")

    # Job Request Details
    job_title = input("Enter the job title you are requesting: ")
    reason = input("Enter the reason for your request: ")
    qualification = input("Enter your qualification: ")

    input("Enter level of education")
    input('Enter second level of education')

    # Confirmation
    print(f"\n**Job Request Summary**")
    print(f"Employee Name: {employee_name}")
    print(f"Employee ID: {employee_id}")
    print(f"Job Title Requested: {job_title}")
    print(f"Reason for Request: {reason}")
    print(f"Enter your qualification:: {qualification}")

    confirmation = input("Is this information correct? (y/n): ")

    if confirmation.lower() == "y":
        print("Job request submitted successfully!")
    else:
        print("Please review and re-enter the information.")


create_job_request()
