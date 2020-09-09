# Contributing
Here you can find details on how you can contribute to wonderwords, the rules and information you need to get started.

## Opening up an issue
If you notice any issues with the software, we would love to know. Please consider [opening up an issue](https://github.com/mrmaxguns/wonderwordsmodule/issues).
Your contributions are greatly appreciated.

### How to open an issue
1. Navigate to the homw page of this repository: https://github.com/mrmaxguns/wonderwordsmodule
2. Go to the `Issues` tab (next to the code tab).
3. Click on the green button on the right side of the screen that says `New issue`.
4. Explain your issue in detail and provide code snippets (if necessary).
5. Submit the issue. We will look into it.

## Forking the repository
Another way to help out is to fork the repository. You can then experiment on the forked repo and submit a pull request once you have made your changes.

### Workflow:
1. Go to the [home page](https://github.com/mrmaxguns/wonderwordsmodule) of the repository and click `Fork` on the top right corner.
2. Now you have a forked repository where you can work at no risk with.
3. **Commiting with git**. Go to the homepage of your forked repository. Then navigate to the `Code` tab.
4. Click on `Clone or download` (the green button in the right side) and copy the url.
5. Go to your command line, navigate to where you want to clone the repository to, and type `git clone` followed by the copied url:
  ```bash
  $ git clone https://github.com/YOUR-USERNAME/wonderwordsmodule
  ```
6. Now navigate into the `wonderordsmodule` directory.
7. Set up the remote by typing the following into the command line:
  ```bash
  $ git remote add upstream https://github.com/mrmaxguns/wonderwordsmodule.git
  ```
8. To set up a virtual environment, you will use python's venv. To create a virtual environment, use the following command:
  ```bash
  $ python3 -m venv venv
  ```
9. Now activate the virtual environment:
  * For cmd.exe (windows):
    ```
    venv\Scripts\activate.bat
    ```
  * For bash:
    ```bash
    source venv/bin/activate
    ```
  * For other shells, [here is a full list of commands](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
10. Install requirements by running:
  ```bash
  pip install -r requirements.txt
  ```
11. Now you have set up the forked repository and set yourself up. You can now create branches, commits, etc. Once you are ready to merge your work to wonderwords, [run tests](#running-tests) and submit a pull request.

## Running tests
To run tests, make sure you are in the main `wonderwords` directory. Testing is done with Pytest, which is automatically installed from `requirements.txt`. To run tests, use the following command:

```bash
pytest tests/
```
