from locust import HttpUser, task, between

class EventsUser(HttpUser):
    # Simulates a user waiting between 1–2 seconds between requests
    wait_time = between(1, 2)

    @task
    def view_events(self):
        # Define endpoint and query params clearly
        endpoint = "/events"
        params = {"user": "locust_user"}
        
        # Send GET request with parameters
        self.client.get(endpoint, params=params)
