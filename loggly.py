import logging, logging.handlers

class loggyHandler(logging.Handler):
    
    def __init__(self, url):
        logging.Handler.__init__(self)
        self.url = url
        
    def mapLogRecord(self, record):
        return record.__dict__
   
    def emit(self, record):
        try:
            import httplib2
            insert_http = httplib2.Http(timeout=10)
            resp, content = insert_http.request(self.url, "POST", body=self.format(record), headers={'content-type':'text/plain'})
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
