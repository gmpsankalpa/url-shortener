# URL Shortener

This is a simple URL shortener application built with Flask and SQLite. It allows users to input long URLs and generates shortened URLs for easier sharing. The application stores the original and shortened URLs in a SQLite database.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Shorten long URLs to easily shareable shortened URLs.
- Validate input URLs for correctness.
- Display flash messages for user feedback.
- Store URLs in a SQLite database.
- Simple and clean user interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine.
- Basic understanding of Flask web framework.
- Basic understanding of SQLite database.

## Installation

To install and run this application locally, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/gmpsankalpa/url-shortener.git

2. Navigate to the project directory:
    ```bash
    cd url-shortener

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt

## Usage

1. To run the application locally, use the following command:
    ```bash
    python app.py

2. Once the application is running, open your web browser and go to `http://localhost:5000` to access the URL shortener interface. You can input a long URL in the provided field and click the "Shorten" button to generate a shortened URL.

## Deployment

This application can be deployed to various platforms, including:

- Heroku
- AWS Elastic Beanstalk
- DigitalOcean
- PythonAnywhere

Refer to the deployment documentation of your chosen platform for specific instructions on deploying Flask applications.

## Contributing
Contributions are welcome! Here's how you can contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT](LICENSE) License.

---

<p align="center">
<b>
  Repo Details 🤙
</b>
</p>

<div align="center">

   ![repo size](https://img.shields.io/github/repo-size/gmpsankalpa/url-shortener?label=Repo%20Size&style=for-the-badge&labelColor=black&color=20bf6b)
   ![GitHub forks](https://img.shields.io/github/forks/gmpsankalpa/url-shortener?&labelColor=black&color=0fb9b1&style=for-the-badge)
   ![GitHub stars](https://img.shields.io/github/stars/gmpsankalpa/url-shortener?&labelColor=black&color=f7b731&style=for-the-badge)
   ![GitHub LastCommit](https://img.shields.io/github/last-commit/gmpsankalpa/url-shortener?logo=github&labelColor=black&color=d1d8e0&style=for-the-badge)

</div>

<p align="center">
<b>
  Deploy status badge 🤖
</b>
</p>  

<div align="center">
   
   [![Netlify Status](https://api.netlify.com/api/v1/badges/f8c54f31-10f6-42a4-80e6-342090a3c60e/deploy-status)](https://app.netlify.com/sites/gmp-url-shortener/deploys)
</div>
