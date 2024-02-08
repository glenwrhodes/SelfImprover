# SelfImprover

SelfImprover is an experimental project designed to explore the possibilities of AI self-improvement, specifically focusing on OpenAI's ChatGPT. The project investigates how ChatGPT can extend its functionality through dynamic interactions with the environment, including creating and executing Python scripts and subprocesses. By leveraging these capabilities, SelfImprover aims to push the boundaries of what AI can achieve in terms of learning, adapting, and enhancing its capabilities.

## Project Overview

At its core, SelfImprover attempts to make OpenAI ChatGPT introspect and enhance its functionalities based on feedback and interactions within a controlled environment. It does this by using a combination of Python code to dynamically create files, execute subprocesses, and interact with the OpenAI API, thus forming a feedback loop where ChatGPT can attempt to improve upon itself.

The project utilizes the following technologies and libraries:
- OpenAI API for accessing ChatGPT's capabilities.
- Python's `subprocess` module for executing external commands and scripts.
- The `dotenv` library for managing environment variables securely.

## Getting Started

To get started with SelfImprover, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/glenwrhodes/SelfImprover.git
   cd SelfImprover
   ```

2. **Set Up Virtual Environment** (Optional)

   It's recommended to create a virtual environment for Python projects to manage dependencies efficiently.

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Environment Variables**

   Since the `.env` file is ignored by git for security reasons, you'll need to create your own `.env` file in the project root directory and specify your OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Running the Project**

   With the environment set up and the API key in place, you're ready to run the project and explore the self-improvement capabilities of ChatGPT.

   ```bash
   python main.py
   ```

## Project Structure

- `main.py`: The entry point of the SelfImprover experiment, containing the core logic for interacting with OpenAI's API, creating files, and executing subprocesses.
- `.env`: A file to store your OpenAI API key securely. (Remember, this should not be committed to your repository.)
- `.gitignore`: A file specifying untracked files that Git should ignore. (Includes `.env` and `.venv`.)

## Contributing

Contributions to SelfImprover are welcome! Whether it's feature suggestions, bug reports, or code contributions, please feel free to open an issue or submit a pull request.

## License

[MIT License](LICENSE.md)

## Acknowledgments

- OpenAI for providing the powerful ChatGPT API.
- Contributors and the open-source community for ongoing support and inspiration.
