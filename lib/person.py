class Person:
    approved_jobs = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing",
    ]

    def __init__(self, name="John Doe", job="Sales"):
        self.name = name    # use property
        self.job = job      # use property

    # name property
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()   # convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # job property
    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in self.approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
