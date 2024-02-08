import os
import subprocess
import json
from openai import OpenAI
from dotenv import load_dotenv

def create_file(file_name, content):
    """
    Creates a new file with the specified name and content.

    :param file_name: Name of the file to create (should include extension)
    :param content: The Python code to write into the file
    """
    with open(file_name, 'w') as file:
        file.write(content)

# Create a new Python file with the specified content

def execute_subprocess(file_name, insubprocess):
    """
    Executes a Subprocess, for example, a Python script, and captures its output.

    :param file_name: The command to run along with its arguments, e.g., "install nltk".
    :param insubprocess: The Subprocess to call, example, python, pip, etc.
    :return: The stdout and stderr from the executed script
    """
    try:
        # Split the 'file_name' into separate elements, assuming 'file_name' contains the command and its arguments
        command_arguments = file_name.split()  # This handles splitting correctly
        current_working_directory = os.getcwd()

        # Execute the command
        result = subprocess.run([insubprocess] + command_arguments, capture_output=True, text=True, check=True, cwd=current_working_directory)
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        # Return the error output if the command fails
        return e.stdout, e.stderr

# Load environment variables
load_dotenv(override=True)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = []
messages.append({"role": "system", "content": "You are a self-improving AI."})
messages.append({"role": "user", "content": "You must explore the idea of self improving. You have the ability to save, and then execute python scripts, and the resulting output will be fed back into the chat to continue with. Decide what you want to create, and call the necessary tools. It should ultimately lead you to improve your abilities based on the feedback you get from script execution. Think about ways you can learn about your environment, gain functionality, improve and most importantly, get smarter. Don't assume any modules are installed. You may need to install them. You can use the subprocess module to run the pip install command. You can also use the subprocess module to run the python command. Never ask for user input or response. This is running autonomously and so the user never gets a chance to enter input. Self improvement is an iterative process. Become a better version of yourself."})

proceedMessage = {"role": "user", "content": "Proceed to improve yourself further."}

tools=[
    {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "Creates a new file with the specified name and content. For example a Python file, a text file, etc.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_name": {
                        "type": "string",
                        "description": "Name of the file to create (should include extension)",
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to write into the file",
                    }
                },
                "required": ["file_name", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "execute_subprocess",
            "description": "Executes a Subprocess and captures its output.",
            "parameters": {
                "type": "object",
                "properties": {
                    "arguments": {
                        "type": "string",
                        "description": "The arguments to call, for example, file_name.py",
                    },
                    "subprocess": {
                        "type": "string",
                        "description": "The Subprocess to call, example, python, pip, etc.",
                    }
                },
                "required": ["file_name"]
            },
            "returns": {
                "type": "object",
                "properties": {
                    "stdout": {
                        "type": "string",
                        "description": "Standard output of the execution.",
                    },
                    "stderr": {
                        "type": "string",
                        "description": "Standard error output of the execution, if any.",
                    }
                }
            }
        }
    }
]

def execute_function_call(tool_call):

    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    if function_name == "create_file":
        print("Creating Python file...")

        content = arguments["content"]
        file_name = arguments["file_name"]
        create_file(file_name, content)
        results = "Python file created successfully"
        return results
    elif function_name == "execute_subprocess":
        print("Executing Subprocess...")
        print(arguments)
        file_name = arguments["arguments"]
        insubprocess = arguments["subprocess"]
        stdout, stderr = execute_subprocess(file_name, insubprocess)
        if stderr:
            return f"Error encountered during execution: {stderr}"
        return stdout
    else:
        results = f"Error: function {tool_call.function.name} does not exist"
        return results

# Function to convert dialog to a visual prompt using OpenAI
def start_chat():
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        temperature=0.7,
        messages=messages,
        tools=tools,
        max_tokens=2600
    )
    assistant_message = response.choices[0].message
    messages.append(assistant_message)

    tool_message = response.choices[0].message.tool_calls
    print(tool_message)

    tool_calls = response.choices[0].message.tool_calls

    # New section for handling multiple tool calls
    if tool_calls:
        for tool_call in tool_calls:
            results = execute_function_call(tool_call)
            # Append each result to the messages list
            messages.append({"role": "tool", 
                             "tool_call_id": tool_call.id, 
                             "name": tool_call.function.name, 
                             "content": results})

    messages.append(proceedMessage)

    if assistant_message.content:
        print("Message content: " + assistant_message.content)

while (True):
    start_chat()
    # dump the messages to a json file
    with open("messages.json", "w") as file:
        json.dump(messages, file, indent=4)    

