from langchain.tools import tool
from pydantic import BaseModel, Field

class CalculationTool():

    @tool("Make a calculation")
    def calculate_budget(operation):
        """Useful to perform any mathematical calculations, 
        like sum, minus, multiplication, division, etc.
        The input to this tool should be a mathematical 
        expression, a couple examples are `200*7` or `5000/2*10`
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"


# #Define a pydantic model for the tool's input parameters
# class CalculationInput(BaseModel):
#     operation: str = Field(..., description="The mathematical operation to perform")
#     factor: float = Field(..., description="A factor by which to multiply the result of the operation")

# #Use the tool decorator with the args_schema parameter pointng to the pydantic model
# @tool("perform_calculatoin", args_schema=CalculationInput, return_direct=True)
# def perform_calculation(operation: str, factor: float) -> str:
#     """
#     Perform a special mathematical operation and multiply the result by a given factor

#     Parameters:
#     - operation (str): A string representing a math operation (e.g., "10+5")
#     - factor (float): A factor by which to multiply the result of the operation

#     Returns:
#     - A string representing the calculation result

#     """
#     # Perform the calculation

#     result = eval(operation) * factor

#     # Return the result as a string
#     return f"The result of '{operation}' multiplied by {factor} is {result}." 