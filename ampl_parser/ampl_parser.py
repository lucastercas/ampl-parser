from parsimonious import Grammar


class AMPLParser(object):

    def __init__(self) -> None:
        super().__init__()
        self.model_content: str = ""
        self.model_parsed = None
        self.data_content: str = ""
        self.data_parsed = None
        self.grammar_model = Grammar(r"""
            expr                        = (entry / emptyline)
            entry                       = (var / objective / constraint)* end

            var                         = "var" ws word ws var_type? endline
            var_type                    = (var_type_continuous / "binary" / "integer")
            var_type_continuous         = var_continuous_lower_bound ws var_ccontinuous_upper_bound
            var_continuous_lower_bound  = ">=" ws number
            var_ccontinuous_upper_bound = "<=" ws number

            objective                   = ("minimize" / "maximize") ws word ws ":" ws equation endline
            constraint                  = "subject" ws "to" ws word ws ":" ws equation ws (">=" / "<=") ws equation endline
            end                         = "end" ws endline

            equation                    = sum
            sum                         = product (("+" / "-") product)*
            product                     = power (("*" / "/") power)*
            power                       = ws value ("^" power)? ws
            value                       = number / word

            word                        = ~r"[-\w]+"
            number                      = ~r"[\d]+" ("." ~r"[\d]+")?

            endline                     = ";" ws

            ws                          = ~r"\s*"
            emptyline                   = ws+
        """)

    def parse(self, model_filename: str):
        self.read_model(model_filename)
        self.model_parsed = self.grammar_model.parse(self.model_content)

    def match(self, model_filename: str):
        self.read_model(model_filename)
        self.model_parsed = self.grammar_model.match(self.model_content)

    def read_model(self, filename: str) -> str:
        with open(filename, 'r') as f:
            self.model_content = f.read()

    def read_data(self, filename: str) -> str:
        with open(filename, 'r') as f:
            self.data_content = f.read()
