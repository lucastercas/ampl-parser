from parsimonious import Grammar


class AMPLParser(object):

    def __init__(self) -> None:
        super().__init__()
        self.model_content: str = ""
        self.model_parsed = None
        self.data_content: str = ""
        self.data_parsed = None
        self.grammar = Grammar(r"""
            expr        = (entry / emptyline)
            entry       = (variable / objective / constraint / end / ws)*

            variable    = "var" ws word ws endline ws
            objective   = objective_keyword ws word ws ":" ws equation endline ws
            constraint  = "subject" ws "to" ws word ws ":" ws equation ws operator ws equation endline ws
            end         = "end" ws endline ws

            equation    = sum
            sum         = product (("+" / "-") product)*
            product     = power (("*" / "/") power)*
            power       = ws value ("^" power)? ws
            value       = number / word

            word        = ~r"[-\w]+"
            number      = ~r"[\d]+" ("." ~r"[\d]+")?

            operator   = ">=" / "<="
            endline     = ";"

            ws          = ~r"\s*"
            emptyline   = ws+

            objective_keyword     = "minimize" / "maximize"
        """)

    def parse(self, model_filename: str):
        self.read_model(model_filename)
        self.model_parsed = self.grammar.parse(self.model_content)

    def match(self, model_filename: str):
        self.read_model(model_filename)
        self.model_parsed = self.grammar.match(self.model_content)

    def read_model(self, filename: str) -> str:
        # To-Do: Check if file exists
        # To-Do: Check if file is .mod
        with open(filename, 'r') as f:
            self.model_content = f.read()

    def read_data(self, filename: str) -> str:
        # To-Do: Check if file exists
        # To-Do: Check if file is .data
        with open(filename, 'r') as f:
            self.data_content = f.read()
