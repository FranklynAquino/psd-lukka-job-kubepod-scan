class OpenSearchResponseObject:
    def __init__(self,label_app_name=None, pod_name=None, public_ip=None, job_id=None):
        self.label_app_name = label_app_name
        self.pod_name = pod_name
        self.public_ip = public_ip
        self.job_id = job_id
        
    def to_string(self):
        return (self.label_app_name, self.pod_name, self.public_ip, self.job_id)