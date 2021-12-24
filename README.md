<h1 align="center">
  <a href="https://github.com/thevahidal/hoopoe-core">
    <img src="docs/images/logo.png" alt="Logo" height="125">
  </a>
</h1>

<div align="center">
  Hoopoe - Get notified of important stuff, right away.
  <br />
  <br />
  <a href="https://github.com/thevahidal/hoopoe-core/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/thevahidal/hoopoe-core/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/thevahidal/hoopoe-core/discussions">Ask a Question</a>
</div>

<div align="center">
<br />

[![license](https://img.shields.io/github/license/thevahidal/hoopoe-core.svg?style=flat-square)](LICENSE)

[![PRs welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/thevahidal/hoopoe-core/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![made with hearth by thevahidal](https://img.shields.io/badge/made%20with%20%E2%99%A5%20by-thevahidal-ff1414.svg?style=flat-square)](https://github.com/thevahidal)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
    - [Cloud vs. On-premise](#cloud-vs-on-premise)
    - [Manual setup](#manual-setup)
    - [Environment Variables reference](#environment-variables-reference)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

There are some important stuff that we must be aware of, like when they exceed some sort of limits or when they start setting fire to your house. In the company that I work, we had this burning desire for a system that send us alert when some stuff happens, right away. 
As you already know the only thing that we always carry around is our phones, so we thought what is better than getting a notification in those cases! That's why I started this project, it's supposed to help us and anyone else dealing with these kind of issues. 

**Hoopoe** is meant to be real straight forward, when you want get notified of a certain thing, just call Hoopoe and Hoopoe make sure to send you a notification.

```python
    # In your code...
    if that_thing_happened:
        hoopoe.call("The thing that we don't like happened!", extra={
            "where": "Alex's House",
            "type": "Cops",
            "how_bad": "4/5"
        })

    
    # And right away in your inbox...
    # Hoopoe Upupa | New Notification: The thing that we don't like happened!
    
    # When
    # Thu, Dec 23, 2021, 09:17 PM UTC
    # Info
    # {
    #   "where": "Alex's House",
    #   "type": "Cops",
    #   "how_bad": "4/5"
    # }

```

> NOTICE: This snippet is imaginary. 


Key features of **Hoopoe**:
- Instant notifications
- Support for email
- Support for popular messengers (Coming Soon!)
    - Whatsapp
    - Telegram
    - Slack
    - ...

- Lots of SDKs (Coming Soon!)
    - Python
    - Javascript
    - ...

- Cloud (Coming Soon!) and on-premise 

<details open>
<summary>Why Hoopoe? The story behind the name.</summary>
<br>

Looking for a name that's both beautiful and meaningful, I started to google for ancient gods and heroes that are somehow related to delivering messages. There were some candidates but Hermes was the leading one, but since it's used so many times decided to go with another one, which ended up with **Hoopoe**. Hoopoe served King Solomon as a delivery man (animal?), so I thought why not! It's a cute animal and the name sticks!

</details>


## Getting Started

### Prerequisites

The recommended way to use **Hoopoe** is by using [Hoopoe.app](https://hoopoe.app) which take away the pain of deploying and maintaining Hoopoe on your own (Coming Soon!). For manual usage please refer to [manual setup section](#manual-setup).

### Cloud vs. On-premise

Hoopoe core is a RESTful API. Either you're using the Hoopoe.app or your own deployment, you can refer to [API docs (Coming Soon!)](https://docs.hoopoe.app) to read more about APIs.

<!-- ![Preview](docs/images/preview.svg) -->

#### Manual setup

There are two ways to deploy Hoopoe:

1. Using docker image **(Recommended)** (Coming Soon!)
    - Either build your own docker image using the Dockerfile
    - Or using the latest image on [Dockerhub (Coming Soon!)](https://hub.docker.com/thevahidal/hoopoe-core)
2. Manual deployment, you can use [this awesome article by Digitalocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04) on how to deploy a django project to production environment
    - Please make sure to serve your deployment over HTTPS (Important)
    - This project is actively updating, make sure to update your deployment often
    - Duplicate ```.env_```, rename it to ```.env``` and fill the required environment variables [See here](#variables-reference)
        
        ```bash
            cp .env_ .env
            nano .env
        ```


#### Environment Variables reference

Please note that entered values are case-sensitive.
Default values are provided as an example to help you figure out what should be entered.
As mentioned in manual setup section, you need to duplicate ```.env_```, rename it to ```.env``` and fill the required environment variables.
 

| Name                       | Default (Example)             | Description                                  |
| -------------------------- | ----------------------------- | -------------------------------------------- |
| SECRET_KEY                 | None                          | Django Secret Key                            |
| DEBUG                      | True                          | Make sure to use DEBUG: False in production  |
| EMAIL_HOST                 | None (mail.example.com)       | Mail server host (Required for email driver) |
| EMAIL_HOST_USER            | None (info@example.com)       | Email address for sending emails             |
| EMAIL_HOST_PASSWORD        | None                          | Password for previous email                  |
| EMAIL_PORT                 | 587                           | Mail server port                             |
| EMAIL_USE_TLS              | TRUE                          | Email TLS                                    |
| EMAIL_UPUPA_USER           | None (upupa@example.com)      | We use this email to send notifications      |
| EMAIL_UPUPA_PASSWORD       | None                          | Password for previous email                  |
| DJANGO_ALLOWED_HOSTS       | localhost 127.0.0.1 [::1]     | Django allowed hosts (Space separated)       |
| SQL_ENGINE                 | django.db.backends.postgresql | DB Engine                                    |
| SQL_DATABASE               | hoopoe_dev                    | DB Name                                      |
| SQL_USER                   | hoopoe                        | DB User                                      |
| SQL_PASSWORD               | hoopoe                        | DB User Password                             |
| SQL_HOST                   | localhost                     | DB Host                                      |
| SQL_PORT                   | 5432                          | DB Port                                      |
| REDIS_HOST                 | localhost                     | Redis Host                                   |
| REDIS_PORT                 | 6379                          | Redis Port                                   |


## Roadmap

See the [open issues](https://github.com/thevahidal/hoopoe-core/issues) for a list of proposed features (and known issues).

- Lots of SDKs
    - Python
    - Javascript
    - Cli
    - ...
- Support for popular messengers
    - Telegram
    - Whatsapp
    - Slack
    ...

## Contributing

First off, thanks for taking the time to contribute! Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

Please adhere to this project's [code of conduct](docs/CODE_OF_CONDUCT.md).


## Support

Reach out to the maintainer at one of the following places:

- [GitHub discussions](https://github.com/thevahidal/hoopoe-core/discussions)
- The email which is located [in GitHub profile](https://github.com/thevahidal)

## License

This project is licensed under the **MIT license**. 

See [LICENSE](LICENSE) for more information.

## Acknowledgements

Thanks for **Amazing GitHub template** for the awesome README and code of conduct that saved me a lot of hours:

- <https://github.com/dec0dOS/amazing-github-template>
