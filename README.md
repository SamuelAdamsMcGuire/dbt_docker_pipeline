## Example ELT using and EL script in pything, postgres, dbt and metabase all in Docker

## how to use

- install docker and docker-compose
- clone repo
- get free account at: https://exchangeratesapi.io/
- save api key in `.env` file in the root repo directory as `API_KEY`
- execute `docker-compose up` in the root directory
- the dbt models will be created
- leaving the containers running you can now access metabase at `http://localhost:3000`
- sign up and regisiter you running postgres db
    - host = mypg
    - port = 5432
    - db = exchange

## To Dos

- refactor into a kubernetes cluster
- fix `.env` so it will also hold the postgres and other secret data (had problems with DBT resolving the postgres credentials)
- add tests in DBT
- add macros in DBT
- add documentation in DBT

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Samuel Adams McGuire - samuelmcguire@engineer.com

Linkedin: [LinkedIn](https://www.linkedin.com/in/samuel-mcguire/)





