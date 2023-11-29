# Visual Studio Code Extensions List Generator

This Python script generates a list of installed Visual Studio Code extensions and saves the information in HTML, Markdown, and CSV formats.

## How to Use

1. **Clone the Repository**

    ```bash
    git clone https://github.com/allmightyroot/VSCodeExtensions.git
    cd VSCodeExtensions
    ```

2. **Add Extension Names**

2. **Generate `extensions.txt` File**

    - **Using Bash (Linux/Mac):**
    
      Run the following command in your terminal to generate the `extensions.txt` file:
    
      ```bash
      code --list-extensions > extensions.txt
      ```
    
      This command retrieves the list of installed Visual Studio Code extensions and saves them in the `extensions.txt` file.
    
    - **Using Command Prompt (cmd, Windows):**
    
      Run the following command in Command Prompt to generate the `extensions.txt` file:
    
      ```cmd
      code --list-extensions > extensions.txt
      ```
    
      This command retrieves the list of installed Visual Studio Code extensions and saves them in the `extensions.txt` file.
    
    - **Using PowerShell (Windows):**
    
      Use the following PowerShell command to generate the `extensions.txt` file:
    
      ```powershell
      code --list-extensions | Out-File -FilePath extensions.txt -Encoding utf8
      ```
    
      This PowerShell command retrieves the list of installed Visual Studio Code extensions and saves them in the `extensions.txt` file.


3. **Run the Script**

    Ensure you have Python installed. Then run the script:

    ```bash
    python extensions_generator.py
    ```

4. **Generated Files**

    - `extensions.html`: Contains a table of installed extensions in HTML format.
    - `extensions.md`: Contains a list of installed extensions in Markdown format.
    - `extensions.csv`: Contains extension details in a CSV file.

## Requirements

- Python 3.x
- Internet connection to fetch extension details from the Visual Studio Code Marketplace API

## Notes

- Ensure the `extensions.txt` file contains valid extension names for accurate results.
- The script excludes extensions that are part of extension packs from the generated output.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

