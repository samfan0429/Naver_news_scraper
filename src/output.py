class UserInput():
    def __init__(self,dic_inputs):
        self.searchKey = dic_inputs['keys'].get()
        self.start_date = dic_inputs['start_date'].get()
        self.end_date = dic_inputs['end_date'].get()
        self.name = dic_inputs['name'].get()