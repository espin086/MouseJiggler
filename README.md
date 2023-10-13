# 🐀 rodents



🐀 rodents is a command line tool that moves the mouse cursor randomly on the screen and performs random actions such as switching tabs or clicking on buttons. It is designed to simulate user activity and prevent screensavers or idle timeouts from activating.

## 🚀 Installation

You can install 🐀 rodents using pip:

```
pip install rodents
```

🖱## Usage

To use 🐀 rodents, you can run the following command:

```
rodents --delay_mean <mean> --delay_std_dev <std_dev> --move_duration <duration>
```

💡 PROTIP: best if you open up a single browser with multiple tabs you want the program to cycle through.

The available options are:

- `--delay_mean`: Mean value for the delay pressing of keys in seconds. Default is 12.
- `--delay_std_dev`: Standard deviation for the delays. Default is 6.
- `--move_duration`: Duration of the mouse movement in seconds. Default is 0.5, this seems to look most natural.

For example, to run 🐀 rodents with a mean delay of 10, standard deviation of 5, and a movement duration of 1 second, you can use the following command:

```
rodents --delay_mean 10 --delay_std_dev 5 --move_duration 1
```

## 🚨 Disclaimer

🐀 rodents is intended for educational and testing purposes only. It should not be used for any malicious activities. The developers of rodents are not responsible for any misuse or damage caused by this tool.

## License

🐀 rodents is released under the MIT License. 


## 🤝 Contributing

Thank you for considering contributing to 🐀 rodents! We welcome any contributions that can help improve the project and make it even more useful.

To contribute to 🐀 rodents, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your contribution.
4. Make your changes and improvements to the codebase.
5. Test your changes thoroughly.
6. Commit and push your changes to your forked repository.
7. Submit a pull request to the main repository.

Please ensure that your code follows best practices and is well-documented. We appreciate detailed commit messages and clear explanations of the changes you have made.

By contributing to 🐀 rodents, you agree to release your contributions under the MIT License.