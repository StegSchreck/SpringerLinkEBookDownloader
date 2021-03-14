<p align="center">
  <img src="https://raw.githubusercontent.com/StegSchreck/SpringerLinkEBookDownloader/master/SpringerLinkEBookDownloader.png" width="300px">
</p>


# Springer Link eBook Downloader
This script takes a list of URLs of Springer Link pages and automatically downloads both the PDF and the EPUB version
(if available) for a free book. If the book is not for free, it will be ignored.

This project is not associated with the Springer publishing house.

## Preconditions
1. Make sure you have Python3, Firefox and Xvfb installed on your system. This project is designed to run on Linux.
1. Checkout the project
    `git clone https://github.com/StegSchreck/SpringerLinkEBookDownloader.git && cd SpringerLinkEBookDownloader`
1. Install the requirements with pip for Python3
    `pip3 install -r requirements.txt`
1. Install Geckodriver

      * Use your system's package manager (if it contains Geckodriver)
        * Arch Linux: `pacman -S geckodriver`
        * MacOS: `brew install geckodriver`
      * Or execute `sudo ./InstallGeckodriver.sh`.
        For this you will need to have tar and wget installed.

## Running the script
To start the parser run the following command:
```
python3 main.py -f <path_to_file_with_lines_of_urls>
```

## Call arguments / parameters
### Mandatory
`-f` / `--file`: path to file with the list of URLs - separated by linebreak

### Optional
`-d` / `--download_folder`: destination folder for the downloaded eBooks

`-v` / `--verbose`: increase output verbosity

`-x` / `--show_browser`: show the browser doing his work (this might help for debugging)

`-h` / `--help`: Display the help, including all possible parameter options

## Trouble shooting
### Script aborts with `WebDriverException`
If you recently updated your Firefox, you might encounter the following exception during the login attempt of the parser:
```
selenium.common.exceptions.WebDriverException: Message: Expected [object Undefined] undefined to be a string
```

This can be fixed by installing the latest version of [Mozilla's Geckodriver](https://github.com/mozilla/geckodriver)
by running again the _Install Geckodriver_ command mentioned [above](#preconditions).
